"""Welcome to Nextpy!."""

from demoapp import styles

# Import all the pages.
from demoapp.pages import *

import nextpy as xt

# Create the app and compile it.
app = xt.App(style=styles.base_style)
app.compile()
