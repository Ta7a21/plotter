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
        expression = expression.replace(" ", "")
        
        if expression == "":
            raise ValueError("Function is empty")


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

        x, y = self.convertStringToMathExpression()

        function_of_x = self.convertMathExpressionToFunction(x, y)

        return function_of_x(self.x)

    def convertStringToMathExpression(self):
        x = symbols("x")
        y = sympify(self.expression)

        return x, y

    def convertMathExpressionToFunction(self, x, y):
        return lambdify(x, y, modules=["numpy"])
