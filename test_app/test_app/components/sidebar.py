"""Sidebar component for the app."""

from test_app import styles
from test_app.state import State

import nextpy as xt


def sidebar_header() -> xt.Component:
    """Sidebar header.

    Returns:
        The sidebar header component.
    """
    return xt.hstack(
        # The logo.
        xt.image(
            src="/icon.svg",
            height="2em",
        ),
        xt.spacer(),
        # Link to Nextpy GitHub repo.
        xt.link(
            xt.center(
                xt.image(
                    src="/github.svg",
                    height="3em",
                    padding="0.5em",
                ),
                box_shadow=styles.box_shadow,
                bg="transparent",
                border_radius=styles.border_radius,
                _hover={
                    "bg": styles.accent_color,
                },
            ),
            href="https://github.com/dot-agent",
        ),
        width="100%",
        border_bottom=styles.border,
        padding="1em",
    )


def sidebar_footer() -> xt.Component:
    """Sidebar footer.

    Returns:
        The sidebar footer component.
    """
    return xt.hstack(
        xt.link(
            xt.center(
                xt.image(
                    src="/paneleft.svg",
                    height="2em",
                    padding="0.5em",
                ),
                bg="transparent",
                border_radius=styles.border_radius,
                **styles.hover_accent_bg,
            ),
            on_click=State.toggle_sidebar_displayed,
            transform=xt.cond(~State.sidebar_displayed, "rotate(180deg)", ""),
            transition="transform 0.5s, left 0.5s",
            position="relative",
            left=xt.cond(State.sidebar_displayed, "0px", "20.5em"),
            **styles.overlapping_button_style,
        ),
        xt.spacer(),
        xt.link(
            xt.text(
                "Docs",
            ),
            href="https://docs.dotagent.dev/nextpy/getting-started/introduction/",
        ),
        xt.link(
            xt.text(
                "Blog",
            ),
            href="https://dotagent.dev/blog/",
        ),
        width="100%",
        border_top=styles.border,
        padding="1em",
    )


def sidebar_item(text: str, icon: str, url: str) -> xt.Component:
    """Sidebar item.

    Args:
        text: The text of the item.
        icon: The icon of the item.
        url: The URL of the item.

    Returns:
        xt.Component: The sidebar item component.
    """
    # Whether the item is active.
    active = (State.router.page.path == f"/{text.lower()}") | (
        (State.router.page.path == "/") & text == "Home"
    )

    return xt.link(
        xt.hstack(
            xt.image(
                src=icon,
                height="2.5em",
                padding="0.5em",
            ),
            xt.text(
                text,
            ),
            bg=xt.cond(
                active,
                styles.accent_color,
                "transparent",
            ),
            color=xt.cond(
                active,
                styles.accent_text_color,
                styles.text_color,
            ),
            border_radius=styles.border_radius,
            box_shadow=styles.box_shadow,
            width="100%",
            padding_x="1em",
        ),
        href=url,
        width="100%",
    )


def sidebar() -> xt.Component:
    """The sidebar.

    Returns:
        The sidebar component.
    """
    # Get all the decorated pages and add them to the sidebar.
    from nextpy.core.page import get_decorated_pages

    return xt.box(
        xt.vstack(
            sidebar_header(),
            xt.vstack(
                *[
                    sidebar_item(
                        text=page.get("title", page["route"].strip("/").capitalize()),
                        icon=page.get("image", "/github.svg"),
                        url=page["route"],
                    )
                    for page in get_decorated_pages()
                ],
                width="100%",
                overflow_y="auto",
                align_items="flex-start",
                padding="1em",
            ),
            xt.spacer(),
            sidebar_footer(),
            height="100dvh",
        ),
        min_width=styles.sidebar_width,
        height="100%",
        position="sticky",
        top="0px",
        border_right=styles.border,
    )
