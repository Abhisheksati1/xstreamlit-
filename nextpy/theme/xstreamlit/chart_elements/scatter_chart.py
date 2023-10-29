from nextpy.components.graphing import *
from nextpy.components.graphing import recharts

def scatter_chart(data,X=None,y=None,**kwargs):
    y_axis_key = None
    x_axis_key = None 
    name = None

    if "y_axis_key" in kwargs:
        y_axis_key = kwargs["y_axis_key"]
    else:
        y_axis_key = "y"
    
    if "x_axis_key" in kwargs:
        x_axis_key = kwargs["x_axis_key"]
    else:
        x_axis_key = "x"
    
    if "name_y_axis" in kwargs:
        name = kwargs["name_y_axis"]
    else:
        name = None

    if "name_x_axis" in kwargs:
        name = kwargs["name_x_axis"]
    else:
        name = None
    return recharts.scatter_chart(
        recharts.scatter(data=data,fill="#8884d8",name= name,),
        recharts.x_axis(data_key=x_axis_key, type_="number"),
        recharts.y_axis(data_key=y_axis_key),
    )