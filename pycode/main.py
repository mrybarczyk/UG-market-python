from Product import *
from Seller import *
from Bank import *
from Buyer import *
from VisitorSeller import *
from VisitorBuyer import *
import matplotlib.pyplot as plt
import pandas as pd


def makro():
    s1marza.append(s1.marza)
    s2marza.append(s2.marza)
    b1need.append(b1.need)
    inflacja.append(bank.inf)


def liczba(productlist, seller):
    return sum(list(p.kp + p.kp * seller.marza for p in productlist))


s1marza = []
s2marza = []
b1need = []
inflacja = []
p1 = Product(300)
p2 = Product(200)
plist1 = [p1, p2]
p3 = Product(10)
p4 = Product(15)
p5 = Product(20)
plist2 = [p3, p4, p5]
bank = Bank()
s1 = Seller(0.1, plist1, bank)
s2 = Seller(0.5, plist2, bank)
b1 = Buyer(bank)
makro()
a = liczba(plist1, s1)
b = liczba(plist2, s2)
value = ((a + a * bank.inf) + (b + b * bank.inf))
s1.accept(VisitorSeller(), b1.need)
s2.accept(VisitorSeller(), b1.need)
i = 0
bank.notify_observers()
print("///")
makro()
while True:
    a = liczba(plist1, s1)
    b = liczba(plist2, s2)
    temp = ((a + a * bank.inf) + (b + b * bank.inf))
    print("temp: ", format(temp, '.2f'))
    print("value: ", format(value, '.2f'))
    perdiv = value/temp
    perdiv = 1-perdiv
    b1.accept(VisitorBuyer(), perdiv)
    s1.accept(VisitorSeller(), b1.need)
    s2.accept(VisitorSeller(), b1.need)
    if value >= temp:
        bank.inf += 0.01
        bank.notify_observers()
    else:
        bank.inf -= 0.01
        bank.notify_observers()
    value = temp
    print("///")
    makro()
    i += 1
    if i >= 20:
        break
axismax = max([max(s1marza), max(s1marza), max(inflacja), max(b1need)])
axislist = []
for i in range(0, len(b1need)):
    axislist.append(i*axismax/len(b1need))
df = pd.DataFrame({'x_values': axislist, 'Zapotrzebowanie klientów': b1need, 'Marża sprzedawcy1': s1marza, 'Marża sprzedawcy2': s2marza, 'Wartość inflacji': inflacja})
plt.plot('x_values', 'Zapotrzebowanie klientów', data=df)
plt.plot('x_values', 'Marża sprzedawcy1', data=df)
plt.plot('x_values', 'Marża sprzedawcy2', data=df)
plt.plot('x_values', 'Wartość inflacji', data=df)
plt.legend()
plt.show()

