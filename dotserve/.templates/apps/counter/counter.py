"""Welcome to Dotserve! This file creates a counter app."""
import random

import dotserve as ds


class State(ds.State):
    """The app state."""

    count = 0

    def increment(self):
        """Increment the count."""
        self.count += 1

    def decrement(self):
        """Decrement the count."""
        self.count -= 1

    def random(self):
        """Randomize the count."""
        self.count = random.randint(0, 100)


def index() -> ds.Component:
    return ds.center(
        ds.vstack(
            ds.heading(State.count),
            ds.hstack(
                ds.button("Decrement", on_click=State.decrement, color_scheme="red"),
                ds.button(
                    "Randomize",
                    on_click=State.random,
                    background_image="linear-gradient(90deg, rgba(255,0,0,1) 0%, rgba(0,176,34,1) 100%)",
                    color="white",
                ),
                ds.button("Increment", on_click=State.increment, color_scheme="green"),
            ),
            padding="1em",
            bg="#ededed",
            border_radius="1em",
            box_shadow="lg",
        ),
        padding_y="5em",
        font_size="2em",
        text_align="center",
    )


# Add state and page to the app.
app = ds.App()
app.add_page(index, title="Counter")
app.compile()
