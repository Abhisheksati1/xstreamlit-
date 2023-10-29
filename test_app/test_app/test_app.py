"""Welcome to Nextpy!."""

from test_app import styles

# Import all the pages.
from test_app.pages import *

import nextpy as xt

# Create the app and compile it.
app = xt.App(style=styles.base_style)
app.compile()
