from sympy import *
import re
import numpy as np


class Graph:
    def __init__(self, function, min_value, max_value):
        self.poly_function = self.validateFunction(function)
        self.min_value = self.validateNumber(min_value)
        self.max_value = self.validateNumber(max_value)
        self.validateMinMax()
        self.x = np.linspace(self.min_value, self.max_value)
        self.y = self.generateCoeffs(self.poly_function)

    def validateFunction(self, function):
        if function == "":
            raise ValueError("Function is empty")
        poly_function = function.replace(" ", "")

        pattern = "^(-)?((\d([*\/][xX])?)*|(([xX])(\^\d)?)|((\d)*[*\/][xX])(\^\d)?)([-\+]((\d([*\/][xX])?)*|(([xX])(\^\d)?)|((\d)*[*\/][xX])(\^\d)?))*$"

        result = re.match(pattern, poly_function)
        if not result:
            raise ValueError("Invalid format")

        return poly_function

    def validateNumber(self, value):
        if value == "":
            raise ValueError("Min and max values should be given")
        try:
            numeric_value = int(value)
            return numeric_value
        except:
            raise ValueError("Min and max values should be integers")

    def validateMinMax(self):
        if self.max_value <= self.min_value:
            raise ValueError("Max value should be greater than min value")

    def generateCoeffs(self, poly_function):
        terms = []
        for term in re.findall(r"[+-]?\d*[*\/]?\w+\^?\d*", poly_function):
            print(term)
            term = term.replace("^", "**")
            terms.append(term)

        terms = "".join(terms)
        x = symbols("x")
        y = sympify(terms)
        lam_x = lambdify(x, y, modules=["numpy"])
        return lam_x(self.x)
