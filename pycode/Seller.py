class Seller:
    def __init__(self, m, ps, observable):
        self.marza = m
        self.products = ps
        observable.register_observer(self)

    def notify(self, observable):
        print("Marza sprzedawcy: ", format(self.marza, '.2f'))

    def accept(self, visitor, nn):
        visitor.visit(self, nn)
