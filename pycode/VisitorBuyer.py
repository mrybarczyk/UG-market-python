from Visitor import *


class VisitorBuyer(Visitor):
    def visit(self, element, value):
        element.need = element.need - element.need*value
