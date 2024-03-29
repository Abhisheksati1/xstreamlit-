"""Stub file for badge.py"""
# ------------------- DO NOT EDIT ----------------------
# This file was generated by `scripts/pyi_generator.py`!
# ------------------------------------------------------

from typing import Optional, Union, overload
# from nextpy.components.libs.chakra import ChakraComponent
from nextpy.components.component import Component
from nextpy.core.vars import Var, BaseVar, ComputedVar
from nextpy.core.event import EventHandler, EventChain, EventSpec

from nextpy.components.component import Component
#from sympy import Basic
from typing import Any

class Latex(Component):
    library: str
    tag: str
    equation_string: str


    def get_event_triggers(self, equation: str) -> None:
        """
        Update the parsed equation and equation string based on the given LaTeX equation.

        Args:
            equation (str): The LaTeX equation to parse.
        """
        pass

