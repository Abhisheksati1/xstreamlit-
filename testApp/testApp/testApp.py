"""Welcome to Nextpy! This file outlines the steps to create a basic app."""
# import numpy as np
import pandas as pd
from typing import Dict, Any

import nextpy as xt
from nextpy.components.component import Component
from nextpy.core.vars import Var
from xtconfig import config
from .state import State
# from nextpy.theme import xstreamlit as st

# class FramerMotion(Component):
#     """A component that wraps all the framer motion components."""

#     library = "framer-motion"
#     tag = "motion.div"
#     animate: Var[Dict[str, Any]] = None
#     initial: Var[Dict[str, Any]] = None
#     transition: Var[Dict[str, Any]] = None

#     def get_event_triggers(self) -> dict[str, Any]:
#         return {
#             **super().get_event_triggers(),
#     }

# motion = FramerMotion.create

def index() -> xt.Component:
    
    return xt.container(

        # xt.motion(
        #         State.initial,
        #         State.animate,
        #         State.transition,
        #         # initial={ "opacity": 0, "scale": 0.5 },
        #         # animate={ "opacity": 1, "scale": 1 },
        #         # transition={ "duration": 0.5 },
        #         class_name="w-28 h-28 bg-white",
        # ),

        xt.framer_motion.motion_div(
                initial={ "opacity": 0, "scale": 0.5 },
                animate={ "opacity": 1, "scale": 1 },
                transition={ "duration": 0.1 },
                whileHover={ "scale": 1.2 },
                whileTap={ "scale": 0.8 },
                drag="x",
                dragConstraints={ "left": -100, "right": 100 },
                class_name="w-28 h-28 bg-white rounded-xl mt-28",
        )
        
        # st.highlight(
        #     "St.table",
        #     query=["st", "table"],
        #     styles={
        #         "px": "2",
        #         "py": "1",
        #         "rounded": "full",
        #         "bg": "grey",
        #     },
        # ),   
        # st.table(
        #     st.thead(
        #     st.tr(
        #         st.th("Name"),
        #         st.th("Age"),
        #         st.th("Location"),
        #     )
        # ),
        # st.tbody(
        #     st.tr(
        #         st.td("John"),
        #         st.td(30),
        #         st.td("New York"),
        #     ),
        #     st.tr(
        #         st.td("Jane"),
        #         st.td(31),
        #         st.td("San Francisco"),
        #     ),
        #     st.tr(
        #         st.td("Joe"),
        #         st.td(32),
        #         st.td("Los Angeles"),
        #     ),
        # ),
        # variant="striped",
        # color_scheme="teal",
        # ),
        # st.highlight(
        #     "St.latex",
        #     query=["st", "latex"],
        #     styles={
        #         "px": "2",
        #         "py": "1",
        #         "rounded": "full",
        #         "bg": "grey",
        #     },
        # ),
        # st.latex(State.eq),
        # st.highlight(
        #     "St.dataframe",
        #     query=["st", "dataframe"],
        #     styles={
        #         "px": "2",
        #         "py": "1",
        #         "rounded": "full",
        #         "bg": "grey",
        #     },
        # ),        
        # st.dataframe(
        #     data=State.data,
        #     #columns=State.columns,
        #     pagination=True,
        #     search=True,
        #     sort=False,
        # ),
        # st.highlight(
        #     "St.areachart",
        #     query=["st", "chart"],
        #     styles={
        #         "px": "2",
        #         "py": "1",
        #         "rounded": "full",
        #         "bg": "grey",
        #     },
        # ),
        # st.area_chart(data=State.data_list),
        # st.header("Hiii") ,
        # st.write("Hello"),
        # st.highlight(
        #     "St.colorpicker",
        #     query=["st", "colorpicker"],
        #     styles={
        #         "px": "2",
        #         "py": "1",
        #         "rounded": "full",
        #         "bg": "grey",
        #     },
        # ),
        # st.text("Color: ",State.color),
        # st.color_picker(
        #          on_change = State.set_color
        # ),
        #     spacing="1.5em",
        #     font_size="2em",
        #     padding_top="10%",  
    )

# Add state and page to the app.
app = xt.App()
app.add_page(index)
app.compile()