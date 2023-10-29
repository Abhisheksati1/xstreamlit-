from nextpy.components.graphing import *
from nextpy.components.graphing import recharts

def area_chart(data, x=None, y=None, **kwargs):         # st.area_chart()
    area_key = None
    x_axis_key = None 
    stroke = None

    if "area_key" in kwargs:
        area_key = kwargs["area_key"]
    else:
        area_key = "y"
    
    if "x_axis_key" in kwargs:
        x_axis_key = kwargs["x_axis_key"]
    else:
        x_axis_key = "x"
    if "stroke" in kwargs:
        stroke = kwargs["stroke"]
    else:
        stroke = "#8884d8"
    if "fill" in kwargs:
        fill = kwargs["fill"]
    else:
        fill = "#8884d8"
    width = kwargs.get("width", "40%")
    height = kwargs.get("height", 300)

    return recharts.area_chart(
        recharts.area(data_key=area_key, stroke=stroke, fill=fill),
        recharts.x_axis(data_key=x_axis_key),
        recharts.y_axis(),
        data = data ,
        width=width,
        height=height,
    )

# area_chart(data, area_key = "x", x_axis_key = "y")