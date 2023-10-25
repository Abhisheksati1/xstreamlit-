import nextpy as xt
import pandas as pd
import numpy as np
from typing import List
class State(xt.State):
    """The app state."""
    data = pd.DataFrame(np.random.randn(10, 10), columns=("col %d" % i for i in range(10)))
    initial={ "opacity": 0, "scale": 0.5 }
    animate={ "opacity": 1, "scale": 1 }
    transition={ "duration": 0.5 }
    #data: List = [
     #   ["Lionel", "Messi", "PSG"],
      #  ["Christiano", "Ronaldo", "Al-Nasir"],
    #]
    #columns: List[str] = ["First Name", "Last Name"]

    #print(df)
    color: str = "#db114b"
    eq: str = (r''' a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)''')
    data_list = xt.data('area', x=[1, 2, 3, 4, 5], y=[1, 4, 9, 16, 10])
    