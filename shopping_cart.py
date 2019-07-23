
class ShoppingCart:
    # write your code here
    def __init__(self, total=0, employee_discount=None, items=[]):
        self.total = total
        self.employee_discount = employee_discount
        self.items = items
        self.total_spent = sum([i['price']*i['quantity'] for i in items])
#         self.discount_item = discount_item
#         self.discount_price = sum([i['price'] for i in items])
    def add_item(self, name=None, price=None, quantity=1):
        if quantity == 1:
            self.items.append({'name': name, 'price': price})
        else:
            for i in range(0, quantity):
                self.items.append({'name': name, 'price': price})
        self.total_spent += price * quantity
        return self.total_spent
    def mean_item_price(self):
        x = [p['price'] for p in self.items] 
        x.sort()
        mean = sum(x) / len(x)
        return mean

    def median_item_price(self):
        x = [p['price'] for p in self.items] 
        x.sort()
        half = len(x)//2
        b = x[half]
        c = x[-half-1]
        median = (b + c) / 2
        return median

    def apply_discount(self):
        x = [p['price'] for p in self.items] 
        discount = sum(x) * .8
        if discount != 0:
            return discount
        else:
            return "sorry"
    def void_last_item(self):
        pass
    def remove_item(self,list,index):
        return list.pop(index)
        
       