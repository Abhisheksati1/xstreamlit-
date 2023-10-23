from __future__ import annotations

from typing import Any, Dict, List, Union

from nextpy.components.component import Component
from nextpy.constants import EventTriggers
from nextpy.core.vars import Var

from .framerMotion import FramerMotion

class Motion(FramerMotion):
    """A component that wraps Framer Motion"""

    html_element: Var[str]
    tag = "motion" + html_element
    is_default = False

    # animate prop of motion component, decides to where it should animate from initial position
    animate: Var[Any]

    # initial prop of motion component, defines the initial position of the component
    initial: Var[Any]

    # transformTemplate lets you change the order of the transform values(by default the are applied in this order: translate, scale, rotate, skew.)
    transformTemplate: Var[str]

    # exit prop is used as a target to animate to when the component is removed from the tree.
    exit: Var[Dict[str, Any]]

    # transition prop
    transition: Var[Dict[str, Any]]

    # variant prop
    variant: Var[Dict[Any, Any]]

    # layout prop
    layout: Var[Any]

    # layoutId prop
    layoutId: Var[str]

    # layoutDependency prop
    layoutDependency: Var[Any]

    # layoutScroll prop
    layoutScroll: Var[bool]

    # inherit prop to either inherit or not inherit from parent component
    inherit: Var[bool]

    # whileFocus event prop
    whileHover: Var[Dict[str, Any]]

    # whileFocus event prop
    whileFocus: Var[Dict[str, Any]]

    # drag event prop
    drag: Var[bool | str]

    # whileDrag event prop
    whileDrag: Var[Any]

    # dragConstraints event prop
    dragConstraints: Var[Any]

    # dragSnapToOrigin event prop
    dragSnapToOrigin: Var[bool]

    # dragElastic event prop
    dragElastic: Var[int]

    # dragMomentum event prop
    dragMomentum: Var[bool]

    # dragTransition event prop
    dragTransition: Var[Dict[str, any]]

    # dragPropagation event prop
    dragPropagation: Var[bool]

    #dragControls event prop
    dragControls: Var[Any]

    #dragListener: event prop
    dragListener: Var[bool]

    # whileInView event prop
    whileInView: Var[Any]