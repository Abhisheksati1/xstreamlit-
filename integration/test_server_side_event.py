"""Integration tests for special server side events."""
import time
from typing import Generator

import pytest
from selenium.webdriver.common.by import By

from dotserve.testing import AppHarness


def ServerSideEvent():
    """App with inputs set via event handlers and set_value."""
    import dotserve as ds

    class SSState(ds.State):
        def set_value_yield(self):
            yield ds.set_value("a", "")
            yield ds.set_value("b", "")
            yield ds.set_value("c", "")

        def set_value_yield_return(self):
            yield ds.set_value("a", "")
            yield ds.set_value("b", "")
            return ds.set_value("c", "")

        def set_value_return(self):
            return [
                ds.set_value("a", ""),
                ds.set_value("b", ""),
                ds.set_value("c", ""),
            ]

        def set_value_return_c(self):
            return ds.set_value("c", "")

        @ds.var
        def token(self) -> str:
            return self.get_token()

    app = ds.App(state=SSState)

    @app.add_page
    def index():
        return ds.fragment(
            ds.input(id="token", value=SSState.token, is_read_only=True),
            ds.input(default_value="a", id="a"),
            ds.input(default_value="b", id="b"),
            ds.input(default_value="c", id="c"),
            ds.button(
                "Clear Immediate",
                id="clear_immediate",
                on_click=[
                    ds.set_value("a", ""),
                    ds.set_value("b", ""),
                    ds.set_value("c", ""),
                ],
            ),
            ds.button(
                "Clear Chained Yield",
                id="clear_chained_yield",
                on_click=SSState.set_value_yield,
            ),
            ds.button(
                "Clear Chained Yield+Return",
                id="clear_chained_yield_return",
                on_click=SSState.set_value_yield_return,
            ),
            ds.button(
                "Clear Chained Return",
                id="clear_chained_return",
                on_click=SSState.set_value_return,
            ),
            ds.button(
                "Clear C Return",
                id="clear_return_c",
                on_click=SSState.set_value_return_c,
            ),
        )

    app.compile()


@pytest.fixture(scope="session")
def server_side_event(tmp_path_factory) -> Generator[AppHarness, None, None]:
    """Start ServerSideEvent app at tmp_path via AppHarness.

    Args:
        tmp_path_factory: pytest tmp_path_factory fixture

    Yields:
        running AppHarness instance
    """
    with AppHarness.create(
        root=tmp_path_factory.mktemp("server_side_event"),
        app_source=ServerSideEvent,  # type: ignore
    ) as harness:
        yield harness


@pytest.fixture
def driver(server_side_event: AppHarness):
    """Get an instance of the browser open to the server_side_event app.


    Args:
        server_side_event: harness for ServerSideEvent app

    Yields:
        WebDriver instance.
    """
    assert server_side_event.app_instance is not None, "app is not running"
    driver = server_side_event.frontend()
    try:
        token_input = driver.find_element(By.ID, "token")
        assert token_input
        # wait for the backend connection to send the token
        token = server_side_event.poll_for_value(token_input)
        assert token is not None

        yield driver
    finally:
        driver.quit()


@pytest.mark.parametrize(
    "button_id",
    [
        "clear_immediate",
        "clear_chained_yield",
        "clear_chained_yield_return",
        "clear_chained_return",
    ],
)
def test_set_value(driver, button_id: str):
    """Call set_value as an event chain, via yielding, via yielding with return.

    Args:
        driver: selenium WebDriver open to the app
        button_id: id of the button to click (parametrized)
    """
    input_a = driver.find_element(By.ID, "a")
    input_b = driver.find_element(By.ID, "b")
    input_c = driver.find_element(By.ID, "c")
    btn = driver.find_element(By.ID, button_id)

    assert input_a
    assert input_b
    assert input_c
    assert btn

    assert input_a.get_attribute("value") == "a"
    assert input_b.get_attribute("value") == "b"
    assert input_c.get_attribute("value") == "c"
    btn.click()
    time.sleep(0.2)
    assert input_a.get_attribute("value") == ""
    assert input_b.get_attribute("value") == ""
    assert input_c.get_attribute("value") == ""


def test_set_value_return_c(driver):
    """Call set_value returning single event.

    Args:
        driver: selenium WebDriver open to the app
    """
    input_a = driver.find_element(By.ID, "a")
    input_b = driver.find_element(By.ID, "b")
    input_c = driver.find_element(By.ID, "c")
    btn = driver.find_element(By.ID, "clear_return_c")

    assert input_a
    assert input_b
    assert input_c
    assert btn

    assert input_a.get_attribute("value") == "a"
    assert input_b.get_attribute("value") == "b"
    assert input_c.get_attribute("value") == "c"
    btn.click()
    time.sleep(0.2)
    assert input_a.get_attribute("value") == "a"
    assert input_b.get_attribute("value") == "b"
    assert input_c.get_attribute("value") == ""
