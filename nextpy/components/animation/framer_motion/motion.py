from __future__ import annotations

from typing import Any, Dict, List, Union

from nextpy.components.component import Component
from nextpy.constants import EventTriggers
from nextpy.core.vars import Var

from .framerMotion import FramerMotion


class MotionBase(FramerMotion):
    """A component that wraps Framer Motion"""

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

    # whileTap event prop
    whileTap: Var[Dict[str, Any]]

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
    dragTransition: Var[Dict[str, Any]]

    # dragPropagation event prop
    dragPropagation: Var[bool]

    # dragControls event prop
    dragControls: Var[Any]

    # dragListener: event prop
    dragListener: Var[bool]

    # whileInView event prop
    whileInView: Var[Any]

    def get_event_triggers(self) -> dict[str, Union[Var, Any]]:
        """Get the event triggers that pass the component's value to the handler.

        Returns:
            A dict mapping the event trigger to the var that is passed to the handler.
        """
        return {
            EventTriggers.ON_CLICK: lambda: [],
            EventTriggers.ON_MOUSE_ENTER: lambda: [],
            EventTriggers.ON_MOUSE_MOVE: lambda: [],
            EventTriggers.ON_MOUSE_LEAVE: lambda: [],
        }


class MotionA(MotionBase):
    """A framer motion component that wraps motion.a element"""
    tag = "motion.a"
    is_default = False


class MotionArticle(MotionBase):
    """A framer motion component that wraps motion.Article element"""
    tag = "motion.article"
    is_default = False


class MotionAside(MotionBase):
    """A framer motion component that wraps motion.aside element"""
    tag = "motion.aside"
    is_default = False


class MotionButton(MotionBase):
    """A framer motion component that wraps motion.button element"""
    tag = "motion.button"
    is_default = False


class MotionDiv(MotionBase):
    """A framer motion component that wraps motion.div element"""
    tag = "motion.div"
    is_default = False


class MotionFieldset(MotionBase):
    """A framer motion component that wraps motion.fieldset element"""
    tag = "motion.fieldset"
    is_default = False


class MotionFooter(MotionBase):
    """A framer motion component that wraps motion.footer element"""
    tag = "motion.footer"
    is_default = False


class MotionForm(MotionBase):
    """A framer motion component that wraps motion.form element"""
    tag = "motion.form"
    is_default = False


class MotionH1(MotionBase):
    """A framer motion component that wraps motion.h1 element"""
    tag = "motion.h1"
    is_default = False


class MotionH2(MotionBase):
    """A framer motion component that wraps motion.h2 element"""
    tag = "motion.h2"
    is_default = False


class MotionH3(MotionBase):
    """A framer motion component that wraps motion.h3 element"""
    tag = "motion.h3"
    is_default = False


class MotionH4(MotionBase):
    """A framer motion component that wraps motion.h4 element"""
    tag = "motion.h4"
    is_default = False


class MotionH5(MotionBase):
    """A framer motion component that wraps motion.h5 element"""
    tag = "motion.h5"
    is_default = False


class MotionH6(MotionBase):
    """A framer motion component that wraps motion.h6 element"""
    tag = "motion.h6"
    is_default = False


class MotionHeader(MotionBase):
    """A framer motion component that wraps motion.header element"""
    tag = "motion.header"
    is_default = False


class MotionImg(MotionBase): 
    """A framer motion component that wraps motion.img element"""
    tag = "motion.img"
    is_default = False


class MotionInput(MotionBase):
    """A framer motion component that wraps motion.input element"""
    tag = "motion.input"
    is_default = False


class MotionLabel(MotionBase):
    """A framer motion component that wraps motion.label element"""
    tag = "motion.label"
    is_default = False


class MotionLi(MotionBase):
    """A framer motion component that wraps motion.li element"""
    tag = "motion.li"
    is_default = False


class MotionMain(MotionBase):
    """A framer motion component that wraps motion.main element"""
    tag = "motion.main"
    is_default = False


class MotionNav(MotionBase):
    """A framer motion component that wraps motion.nav element"""
    tag = "motion.nav"
    is_default = False


class MotionOl(MotionBase):
    """A framer motion component that wraps motion.ol element"""
    tag = "motion.ol"
    is_default = False


class MotionOption(MotionBase):
    """A framer motion component that wraps motion.option element"""
    tag = "motion.option"
    is_default = False


class MotionP(MotionBase):
    """A framer motion component that wraps motion.p element"""
    tag = "motion.p"
    is_default = False


class MotionSection(MotionBase):
    """A framer motion component that wraps motion.section element"""
    tag = "motion.section"
    is_default = False


class MotionSelect(MotionBase):
    """A framer motion component that wraps motion.select element"""
    tag = "motion.select"
    is_default = False


class MotionSpan(MotionBase):
    """A framer motion component that wraps motion.span element"""
    tag = "motion.span"
    is_default = False


class MotionTable(MotionBase):
    """A framer motion component that wraps motion.table element"""
    tag = "motion.table"
    is_default = False


class MotionTd(MotionBase):
    """A framer motion component that wraps motion.td element"""
    tag = "motion.td"
    is_default = False


class MotionTextArea(MotionBase):
    """A framer motion component that wraps motion.textarea element"""
    tag = "motion.textarea"
    is_default = False


class MotionTh(MotionBase):
    """A framer motion component that wraps motion.th element"""
    tag = "motion.th"
    is_default = False


class MotionTr(MotionBase):
    """A framer motion component that wraps motion.tr element"""
    tag = "motion.tr"
    is_default = False


class MotionUl(MotionBase):
    """A framer motion component that wraps motion.ul element"""
    tag = "motion.ul"
    is_default = False