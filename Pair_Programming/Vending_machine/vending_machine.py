def purchase_product(stock, price, quantity, balance):
    cost = price * quantity
    print(cost, 'is the cost')
    if balance >= cost and stock >= quantity:
        print("Thank you!")
        balance = balance - cost
        change = balance
        if coin_combination(change) == True:
            balance = 0
            print('Here\'s your change', change)
        elif coin_combination(change) == False:
            print('EXACT CHANGE ONLY!!')
        stock = stock - quantity
    elif balance < cost:
        print('you haven\'t given me enough money!!!')
        change = balance
    elif stock < quantity:
        print('out of stock!')
        change = balance
    return stock, change

def coin_combination(change):
    combination = []
    while len(combination) == 0:
        for a in range(10):
            for b in range(10):
                for c in range(10):
                    for d in range(10):
                        for e in range(10):
                            for f in range(10):
                                if a*0.05 + b*0.1 + c*0.20 + d*0.5 + e*1 + f*2 == change:
                                    combination.append((a, b, c, d, e, f))
    if len(combination) != 0:
        return True
    else:
        return False

class vendingMachine:
    def __init__(self, choc_stock, crisp_stock, cola_stock,balance=0, change=0):
        self.balance = balance
        self.choc_stock = choc_stock
        self.crisp_stock = crisp_stock
        self.cola_stock = cola_stock
        self.change = change

    def get_balance(self):
        return self.balance

    def get_choc_stock(self):
        return self.choc_stock

    def get_crisp_stock(self):
        return self.crisp_stock

    def get_cola_stock(self):
        return self.cola_stock

    def take_money(self, cash):
        '''
        This function will convert valid coin inputs into balance to be spent on products.
        If the coins are invalid, they are returned to the coin tray
        param cash: input coin
        return: balance increase (if valid coin inserted), otherwise coin returned
        '''
        if cash == 0.05 or cash == 0.10 or cash == 0.20 or cash == 0.5 or cash == 1 or cash == 2:
            self.balance += cash
            print('Your balance is:', self.balance)
            return self.balance
        else:
            print('Enter valid coins only!')
            return self.balance


    def purchase_cola(self, quantity):
        price = 1
        return purchase_product(self.cola_stock, price, quantity, self.balance)

    def purchase_choc(self, quantity):
        price = 0.50
        return purchase_product(self.choc_stock, price, quantity, self.balance)

    def purchase_crisp(self, quantity):
        price = 0.50
        return purchase_product(self.crisp_stock, price, quantity, self.balance)


if __name__ == '__main__':
    print('Welcome to our vending machine :)')
    v = vendingMachine(10, 10, 10)
    cash = 0
    while True:
        money = input('INSERT COINS AND PRESS ENTER WHEN FINISHED ')
        if money == '':
            break
        balance = v.take_money(float(money))
        cash += float(money)
        print(cash)
        print(balance)

    v.take_money(cash)
    product = input('Select the product you want:')
    if product == 'cola':
        quantity = int(input('Please enter the quantity: '))
        v.purchase_cola(quantity)
    if product == 'choc':
        quantity = int(input('Please enter the quantity: '))
        v.purchase_choc(quantity)
    if product == 'crisp':
        quantity = int(input('Please enter the quantity: '))
        v.purchase_crisp(quantity)
