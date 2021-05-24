class Buyer:
    def __init__(self, observable):
        self.need = 1
        observable.register_observer(self)

    def notify(self, observable):
        print("Wskaznik potrzeb kupujacego: ", format(self.need, '.2f'))

    def accept(self, visitor, value):
        visitor.visit(self, value)
