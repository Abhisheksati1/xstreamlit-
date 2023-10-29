"""Base state for the app."""

import nextpy as xt
import pandas as pd
import numpy as np
from typing import List

class State(xt.State):
    """State for the app."""

    # Whether the sidebar is displayed.
    sidebar_displayed: bool = True
    data = pd.DataFrame(np.random.randn(10, 10), columns=("col %d" % i for i in range(10)))
    #data: List = [
     #   ["Lionel", "Messi", "PSG"],
      #  ["Christiano", "Ronaldo", "Al-Nasir"],
    #]
    #columns: List[str] = ["First Name", "Last Name"]

    data2 = [
    {"name": "Page A", "uv": 4000, "pv": 2400, "amt": 2400},
    {"name": "Page B", "uv": 3000, "pv": 1398, "amt": 2210},
    {"name": "Page C", "uv": 2000, "pv": 9800, "amt": 2290},
    {"name": "Page D", "uv": 2780, "pv": 3908, "amt": 2000},
    {"name": "Page E", "uv": 1890, "pv": 4800, "amt": 2181},
    {"name": "Page F", "uv": 2390, "pv": 3800, "amt": 2500},
    {"name": "Page G", "uv": 3490, "pv": 4300, "amt": 2100},
]
    data01 = [
    {"x": 100, "y": 200, "z": 200},
    {"x": 120, "y": 100, "z": 260},
    {"x": 170, "y": 300, "z": 400},
    {"x": 170, "y": 250, "z": 280},
    {"x": 150, "y": 400, "z": 500},
    {"x": 110, "y": 280, "z": 200},
]

    #print(df)
    color: str = "#db114b"
    eq: str = (r''' a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)''')
    data_list = xt.data('area', x=[1, 2, 3, 4, 5], y=[1, 4, 9, 16, 10])
    

    def toggle_sidebar_displayed(self) -> None:
        """Toggle the sidebar displayed."""
        self.sidebar_displayed = not self.sidebar_displayed
