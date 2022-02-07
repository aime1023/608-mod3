dinner = 240

class Purchase(object):
    def __init__(self, amount):
        self.amount = amount
    def caltax(self, taxPerc):
        return self.amount * taxPerc/100.0
    def caltip(self, tipPerc):
        return self.amount * tipPerc/100.0  
    def caltot(self, taxPerc, tipPerc):
        return self.amount * (1 + taxPerc/100.0 + tipPerc/100.0)

purchase = Purchase(dinner)
taxPerc = 7.5
tipPerc = 20.0

tax = purchase.caltax(taxPerc)
tip = purchase.caltip(tipPerc)

print('Tax: ', tax)
print('tip', tip)
print('Total:', purchase.caltot(taxPerc, tipPerc))