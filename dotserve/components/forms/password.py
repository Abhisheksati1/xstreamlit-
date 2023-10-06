"""A password input component."""

from dotserve.components.forms.input import Input
from dotserve.vars import Var


class Password(Input):
    """A password input component."""

    # The type of input.
    type_: Var[str] = "password"  # type: ignore