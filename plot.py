from Graph import Graph
from error import raiseError


def plot(self):
    try:
        graph_plot = Graph(self.expression.text(), self.min.text(), self.max.text())
    except ValueError as err:
        error_message = err.args[0]
        raiseError(self, error_message)
        return
    self.graph.clear()
    self.graph.plot(graph_plot.x, graph_plot.y, pen="r")
