import pytest

from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from Graph import Graph
from plot import plot
import app as gui_app
import numpy as np


@pytest.fixture
def app(qtbot):
    test_app = gui_app.Ui()
    qtbot.addWidget(test_app)

    return test_app


def test_format_1(app, qtbot):
    app.expression.setText("")
    app.min_value.setText("0")
    app.max_value.setText("10")

    with pytest.raises(ValueError, match="Function is empty"):
        Graph(app.expression.text(), app.min_value.text(), app.max_value.text())


def test_format_2(app, qtbot):
    app.expression.setText("3*x^3+6*x^2+x*3")
    app.min_value.setText("0")
    app.max_value.setText("10")

    with pytest.raises(ValueError, match="Invalid format"):
        Graph(app.expression.text(), app.min_value.text(), app.max_value.text())


def test_min_value_max_value_1(app, qtbot):
    app.expression.setText("3*x^3+6*x^2+x")
    app.min_value.setText("a")
    app.max_value.setText("10")

    with pytest.raises(ValueError,match="Min and max values should be integers"):
        Graph(app.expression.text(), app.min_value.text(), app.max_value.text())


def test_min_value_max_value_2(app, qtbot):
    app.expression.setText("3*x^3+6*x^2+x")
    app.min_value.setText("")
    app.max_value.setText("10")

    with pytest.raises(ValueError,match="Min and max values should be given"):
        Graph(app.expression.text(), app.min_value.text(), app.max_value.text())


def test_min_value_max_value_3(app, qtbot):
    app.expression.setText("3*x^3+6*x^2+x")
    app.min_value.setText("10")
    app.max_value.setText("0")

    with pytest.raises(ValueError,match="Max value should be greater than min value"):
        Graph(app.expression.text(), app.min_value.text(), app.max_value.text())


def test_pass(app, qtbot):
    app.expression.setText("3*x^3+6*x^2+x")
    app.min_value.setText("0")
    app.max_value.setText("10")

    try:
        Graph(app.expression.text(), app.min_value.text(), app.max_value.text())
    except ValueError as err:
        pytest.fail(err.args[0])
