"""Stub file for link.py"""
# ------------------- DO NOT EDIT ----------------------
# This file was generated by `scripts/pyi_generator.py`!
# ------------------------------------------------------

from typing import Optional, Union, overload
from dotserve.components.libs.chakra import ChakraComponent
from dotserve.components.component import Component
from dotserve.vars import Var, BaseVar, ComputedVar
from dotserve.event import EventHandler, EventChain, EventSpec

class Link(ChakraComponent):
    @overload
    @classmethod
    def create(cls, *children, rel: Optional[Union[Var[str], str]] = None, href: Optional[Union[Var[str], str]] = None, text: Optional[Union[Var[str], str]] = None, as_: Optional[Union[Var[str], str]] = None, is_external: Optional[Union[Var[bool], bool]] = None, on_blur: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_click: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_context_menu: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_double_click: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_focus: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mount: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_down: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_enter: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_leave: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_move: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_out: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_over: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_up: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_scroll: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_unmount: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, **props) -> "Link":  # type: ignore
        """Create a Link component.

        Args:
            *children: The children of the component.
            rel: The rel.
            href: The page to link to.
            text: The text to display.
            as_: What the link renders to.
            is_external: If true, the link will open in new tab.
            **props: The props of the component.

        Raises:
            ValueError: in case of missing children

        Returns:
            Component: The link component
        """
        ...
