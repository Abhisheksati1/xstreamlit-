"""Base state for the app."""

import nextpy as xt


class State(xt.State):
    """State for the app."""
    sidebar_displayed: bool = True

    @xt.var
    def origin_url(self) -> str:
        """Get the url of the current page.

        Returns:
            str: The url of the current page.
        """
        return self.router_data.get("asPath", "")
    
    def toggle_sidebar_displayed(self) -> None:
        """Toggle the sidebar displayed."""
        self.sidebar_displayed = not self.sidebar_displayed
