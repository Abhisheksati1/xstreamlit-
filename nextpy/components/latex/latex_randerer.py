from nextpy.components.component import Component
from typing import Any
#from sympy import parse_expr

class Latex(Component):
    library = "react-katex"
    tag = "InlineMath"

    equation_string: str = None
    parsed_equation: Any = None

    def get_event_triggers(self):
        return {
            **super().get_event_triggers(),
        }