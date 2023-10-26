from nextpy.components.component import Component, NoSSRComponent
from nextpy.core.vars import Var
from typing import Any, Dict, List, Union
from nextpy.constants import EventTriggers


class FramerMotion(Component):
    """A component that wraps all the framer motion components."""

    library = "framer-motion"

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
