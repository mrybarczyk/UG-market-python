from abc import ABCMeta, abstractmethod

NOT_IMPLEMENTED = "You should implement this."


class Visitor:
    __metaclass__ = ABCMeta

    @abstractmethod
    def visit(self, element, value):
        raise NotImplementedError(NOT_IMPLEMENTED)

