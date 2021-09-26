import numpy as np
from Function import Function
from error import raiseError

def plot(self):
    try:
        graph_plot = Function(self.function.text(),self.min.text(),self.max.text())
    except ValueError as err:
        error_message = err.args[0]
        raiseError(self,error_message)
        return
    x = np.linspace(graph_plot.min_value,graph_plot.max_value)
    y = x**2
    self.graph.plot(x,y, pen='b')
