import nextpy as xt
import numpy as np
import pandas as pd
from test_app.templates import template
from xtconfig import config
from ..state import State
from nextpy.theme import xstreamlit as st
@template(route="/my_app", title="my_app")
def my_app() -> xt.Component:
    
    return xt.container(

        st.highlight(
            "St.table",
            query=["st.table"],
            styles={
                "px": "2",
                "py": "1",
                "rounded": "full",
                "bg": "grey",
            },
        ),   
        st.table(
            st.thead(
            st.tr(
                st.th("Name"),
                st.th("Age"),
                st.th("Location"),
            )
        ),
        st.tbody(
            st.tr(
                st.td("John"),
                st.td(30),
                st.td("New York"),
            ),
            st.tr(
                st.td("Jane"),
                st.td(31),
                st.td("San Francisco"),
            ),
            st.tr(
                st.td("Joe"),
                st.td(32),
                st.td("Los Angeles"),
            ),
        ),
        variant="striped",
        color_scheme="teal",
        ),
        st.highlight(
            "St.latex",
            query=["""st.latex """],
            styles={
                "px": "2",
                "py": "1",
                "rounded": "full",
                "bg": "grey",
            },
        ),
        st.latex(State.eq),
        st.highlight(
            "St.dataframe",
            query=["st.dataframe \n"],
            styles={
                "px": "2",
                "py": "1",         
                "rounded": "full",
                "bg": "grey",
            },
        ),        
        st.dataframe(
            data=State.data,
           # columns=State.columns,
            pagination=True,
            search=True,
            sort=False,
        ),
        st.highlight(
            "St.areachart",
            query=["st.chart"],
            styles={
                "px": "2",
                "py": "1",
                "rounded": "full",
                "bg": "grey",
            },
        ),
        st.area_chart(data=State.data_list, area_key="x", x_axis_key="y"),
        st.header("Hii") ,
       
        st.line_chart(data=State.data2),
        st.write("Hello"),
        st.highlight(
            "St.colorpicker",
            query=["st.colorpicker"],
            styles={
                "px": "2",
                "py": "1",
                "rounded": "full",
                "bg": "grey",
            },
        ),
        st.text("Color: ",State.color),
        st.color_picker(
            on_change = State.set_color
        ),

# Call st.bar_chart with data and area_key specified in kwargs
        st.bar_chart(State.data, **{"area_key": "x"}),
    )     #bar chart kaa args kwargs shi krne h