"""Welcome to Nextpy! This file outlines the steps to create a basic app."""
# import numpy as np
# import pandas as pd

import random

import nextpy as xt 
from xtconfig import config
# from .state import State
# from nextpy.theme import xstreamlit as st
from nextpy.core.vars import Var
from typing import Dict, Union, List, Any




class MotionComponent(xt.Component):
    library = "framer-motion"
    tag = "motion" + ".div"
    is_default = False
    
    whileHover: Var[Dict[str, Any]]
    whileTap: Var[Dict[str, Any]]
    # style: Var[Any]
    className:Var[str]

    

motion_component = MotionComponent.create



def index() -> xt.Component:
    return xt.container(
            # xt.header("Hii") ,
            #  xt.text("Color: ",State.color),
             motion_component(
                    whileHover = {"scale": 1.2},
                    whileTap = {"scale": 0.8},
                    className = "w-28 h-28 bg-white"
                ),
                
            spacing="1.5em",
            font_size="2em",
            padding_top="10%",  
        )

# Add state and page to the app.
app = xt.App()
app.add_page(index)
app.compile()