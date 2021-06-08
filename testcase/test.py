class Person(object):
    def __init__(self):
        print(r'i\'m class')
    def cry(self):
        print('cry')
dsx = Person()
dsx.cry()

class Cay(object):
    def __init__(self,color,pl,pz):
        self.color = color
        self.pl = pl
        self.pz = pz
    def run(self):
        print(r'car\'s color is:{}'.format(self.color))
        print('run')
    def driver(self):
        print('driver')
    def movie(self):
        print('movie')
ywn_car = Cay('red','5.0','hanma')
ywn_car.run()

class BuyCar(object):
    def sale(self):
        print('sale car')
    def insurance(self):
        print('insurance')
    def check(self):
        print('check')
    def card(self):
        print('card')
    def pay(self):
        print('pay')
    def done(self):
        print('done')
me = BuyCar()
me.sale()