class Product:
    # constructor
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.stock = 0
    
    # to string function
    def __str__(self):
        return "Name: " + self.name + "\nPrice: " + str(self.price) \
                + "\nStock: " + str(self.stock)
    
    # update product name
    def chName(self, new_name):
        temp, self.name = self.name, new_name
        return temp
    
    # update product price
    def chPrice(self, new_price):
        temp, self.price = self.price, new_price
        return temp
    
    # update stock(+ or -)
    def chStock(self, amt): 
        self.stock += amt
        return self.stock
    
    # sell a product
    def sell(self, qt):
        if self.stock <= 0: return "Sorry, we dont have any more " + self.name + " in stock."
        elif qt > self.stock: return "Sorry, we only have " + str(self.stock) + " " + self.name + " in stock"
        else:
            self.stock -= qt
            return str(qt) + " " + self.name + " were sold"

class CustomerAccount:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name
p1 = Product("banana", 2.50)
print(p1.chStock(50))
print(p1.sell(10))
p2 = Product("apples", 1.50)
print(p2.chStock(90))
print(p2.sell(80))
print(p2.sell(50))
c1 = CustomerAccount("Johnny Test")
print(c1)

