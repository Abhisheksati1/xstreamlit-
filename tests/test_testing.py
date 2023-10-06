"""Unit tests for the included testing tools."""
from dotserve.constants import IS_WINDOWS
from dotserve.testing import AppHarness


def test_app_harness(tmp_path):
    """Ensure that AppHarness can compile and start an app.

    Args:
        tmp_path: pytest tmp_path fixture
    """
    # Skip in Windows CI.
    if IS_WINDOWS:
        return

    def BasicApp():
        import dotserve as ds

        app = ds.App()
        app.add_page(lambda: ds.text("Basic App"), route="/", title="index")
        app.compile()

    with AppHarness.create(
        root=tmp_path,
        app_source=BasicApp,  # type: ignore
    ) as harness:
        assert harness.app_instance is not None
        assert harness.backend is not None
        assert harness.frontend_url is not None
        assert harness.frontend_process is not None
        assert harness.frontend_process.poll() is None

    assert harness.frontend_process.poll() is not None
