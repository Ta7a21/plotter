from Graph import Graph
from error import errorPOPUP


def plot(self):
    try:
        graph_plot = Graph(
            expression=self.expression.text(),
            min_value=self.min_value.text(),
            max_value=self.max_value.text(),
        )
    except ValueError as err:
        error_message = err.args[0]
        errorPOPUP(self, error_message)
        return

    self.graph.clear()
    self.graph.plot(graph_plot.x, graph_plot.y, pen="r")
