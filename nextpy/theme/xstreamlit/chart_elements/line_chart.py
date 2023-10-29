from nextpy.components.graphing import *
from nextpy.components.graphing import recharts

def line_chart(data,X=None,y=None):            # st.line_chart()
    return recharts.line_chart( 
    recharts.line(
        data_key="pv",
        stroke="#8884d8",
    ),
    recharts.line(
        data_key="uv",
        stroke="#82ca9d",
    ),
    recharts.x_axis(data_key="name"),
    recharts.y_axis(),
    data=data,
    )