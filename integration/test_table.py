"""Integration tests for table and related components."""
from typing import Generator

import pytest
from selenium.webdriver.common.by import By

from dotserve.testing import AppHarness


def Table():
    """App using table component."""
    from typing import List

    import dotserve as ds

    class TableState(ds.State):
        rows: List[List[str]] = [
            ["John", "30", "New York"],
            ["Jane", "31", "San Fransisco"],
            ["Joe", "32", "Los Angeles"],
        ]

        headers: List[str] = ["Name", "Age", "Location"]

        footers: List[str] = ["footer1", "footer2", "footer3"]

        caption: str = "random caption"

        @ds.var
        def token(self) -> str:
            return self.get_token()

    app = ds.App(state=TableState)

    @app.add_page
    def index():
        return ds.center(
            ds.input(id="token", value=TableState.token, is_read_only=True),
            ds.table_container(
                ds.table(
                    headers=TableState.headers,
                    rows=TableState.rows,
                    footers=TableState.footers,
                    caption=TableState.caption,
                    variant="striped",
                    color_scheme="blue",
                    width="100%",
                ),
            ),
        )

    @app.add_page
    def another():
        return ds.center(
            ds.table_container(
                ds.table(  # type: ignore
                    ds.thead(  # type: ignore
                        ds.tr(  # type: ignore
                            ds.th("Name"),
                            ds.th("Age"),
                            ds.th("Location"),
                        )
                    ),
                    ds.tbody(  # type: ignore
                        ds.tr(  # type: ignore
                            ds.td("John"),
                            ds.td(30),
                            ds.td("New York"),
                        ),
                        ds.tr(  # type: ignore
                            ds.td("Jane"),
                            ds.td(31),
                            ds.td("San Francisco"),
                        ),
                        ds.tr(  # type: ignore
                            ds.td("Joe"),
                            ds.td(32),
                            ds.td("Los Angeles"),
                        ),
                    ),
                    ds.tfoot(  # type: ignore
                        ds.tr(ds.td("footer1"), ds.td("footer2"), ds.td("footer3"))  # type: ignore
                    ),
                    ds.table_caption("random caption"),
                    variant="striped",
                    color_scheme="teal",
                )
            )
        )

    app.compile()


@pytest.fixture()
def table(tmp_path_factory) -> Generator[AppHarness, None, None]:
    """Start Table app at tmp_path via AppHarness.

    Args:
        tmp_path_factory: pytest tmp_path_factory fixture

    Yields:
        running AppHarness instance

    """
    with AppHarness.create(
        root=tmp_path_factory.mktemp("table"),
        app_source=Table,  # type: ignore
    ) as harness:
        assert harness.app_instance is not None, "app is not running"
        yield harness


@pytest.fixture
def driver(table: AppHarness):
    """GEt an instance of the browser open to the table app.

    Args:
        table: harness for Table app

    Yields:
        WebDriver instance.
    """
    driver = table.frontend()
    try:
        token_input = driver.find_element(By.ID, "token")
        assert token_input
        # wait for the backend connection to send the token
        token = table.poll_for_value(token_input)
        assert token is not None

        yield driver
    finally:
        driver.quit()


@pytest.mark.parametrize("route", ["", "/another"])
def test_table(driver, table: AppHarness, route):
    """Test that a table component is rendered properly.

    Args:
        driver: Selenium WebDriver open to the app
        table: Harness for Table app
        route: Page route or path.
    """
    driver.get(f"{table.frontend_url}/{route}")
    assert table.app_instance is not None, "app is not running"

    thead = driver.find_element(By.TAG_NAME, "thead")
    # poll till page is fully loaded.
    table.poll_for_content(element=thead)
    # check headers
    assert thead.find_element(By.TAG_NAME, "tr").text == "NAME AGE LOCATION"
    # check first row value
    assert (
        driver.find_element(By.TAG_NAME, "tbody")
        .find_elements(By.TAG_NAME, "tr")[0]
        .text
        == "John 30 New York"
    )
    # check footer
    assert (
        driver.find_element(By.TAG_NAME, "tfoot")
        .find_element(By.TAG_NAME, "tr")
        .text.lower()
        == "footer1 footer2 footer3"
    )
    # check caption
    assert driver.find_element(By.TAG_NAME, "caption").text == "random caption"
