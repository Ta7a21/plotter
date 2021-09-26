from sympy import *
import re
import numpy as np


class Graph:
    def __init__(self, expression, min_value, max_value):
        self.expression = self.validateExpression(expression)
        self.min_value = self.validateInteger(min_value)
        self.max_value = self.validateInteger(max_value)
        self.checkMinLessThanMax()
        self.x = np.linspace(self.min_value, self.max_value)
        self.y = self.generateFunction()

    def validateExpression(self, expression):
        if expression == "":
            raise ValueError("Function is empty")

        expression = expression.replace(" ", "")

        pattern = "^(-)?((\d([*\/][xX])?)*|(([xX])(\^\d)?)|((\d)*[*\/][xX])(\^\d)?)([-\+]((\d([*\/][xX])?)*|(([xX])(\^\d)?)|((\d)*[*\/][xX])(\^\d)?))*$"
        result = re.match(pattern, expression)
        if not result:
            raise ValueError("Invalid format")

        return expression

    def validateInteger(self, value):
        if value == "":
            raise ValueError("Min and max values should be given")
        try:
            integer = int(value)
            return integer
        except:
            raise ValueError("Min and max values should be integers")

    def checkMinLessThanMax(self):
        if self.max_value <= self.min_value:
            raise ValueError("Max value should be greater than min value")

    def generateFunction(self):
        self.expression = self.expression.replace("^", "**")

        # Convert the expression of string type to general mathematical expression
        x = symbols("x")
        y = sympify(self.expression)

        # Convert the SymPy expression to an expression that can be numerically evaluated
        lam_x = lambdify(x, y, modules=["numpy"])

        return lam_x(self.x)
