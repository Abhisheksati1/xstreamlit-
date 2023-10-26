"""Welcome to Nextpy! This file outlines the steps to create a basic app."""
import numpy as np
import pandas as pd

import random

import nextpy as xt 
from xtconfig import config
from nextpy.core.state import State
from nextpy.core.vars import Var
from typing import Dict, Union, List, Any




class MotionComponent(xt.Component):
    library = "framer-motion"
    tag = "motion" + ".div"
    is_default = False
    
    whileHover: Var[Dict[str, Any]]
    whileTap: Var[Dict[str, Any]]

    

motion_component = MotionComponent.create



def index() -> xt.Component:
    return xt.container(
            
             motion_component(
                 xt.box(
                        width="100px",
                        height="100px", 
                        background_color = "blue"
                    ),
                    whileHover = {"scale": 1.2},
                    whileTap = {"scale": 0.8},
                ),
            spacing="1.5em",
            font_size="2em",
            padding_top="10%",  
        )

# Add state and page to the app.
app = xt.App()
app.add_page(index)
app.compile()