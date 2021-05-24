from Visitor import *
import random


class VisitorSeller(Visitor):
    def visit(self, element, nn):
        number = random.uniform(0.01, 0.5)
        if nn >= 0.75:
            element.marza += number
        else:
            element.marza -= number
            if element.marza < 0:
                element.marza = 0.01
