class Bank:
    def __init__(self):
        self.inf = 0
        self._observers = []

    def register_observer(self, observer):
        self._observers.append(observer)

    def notify_observers(self):
        print("Inflacja na poziomie: ", format(self.inf, '.2f'))
        for observer in self._observers:
            observer.notify(self)
