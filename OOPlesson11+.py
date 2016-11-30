import Euclid
class Fraction:

    def __init__(self, numerator, denominator, simplify=True):
        if denominator == 0:
            raise ZeroDivisionError
        self.numerator = int(numerator)
        self.denominator = int(denominator)
        if simplify:
            self.minify()

    def __repr__(self):
        return "Fraction(%s/%s)" % (self.numerator, self.denominator)

    def minify(self):
        gcf = Euclid.gcf(self.numerator, self.denominator)
        if gcf > 1:
            self.numerator //= gcf
            self.denominator //= gcf

class Item:

    def __init__ (self, name, price):
        self.price = float(price)
        self.name = str(name)

    def __repr__(self):
        return "Item({item.name}, {item.price})".format(item=self)

class Cart:
    def __init__(self):
        self.items = []
        self.coupons = []

    def add(self, item, amount=1):
        for i in range(amount):
            self.items.append(item)

    def add_coupon(coupon):
        self.coupons.append(coupon)

    def total(self):
        return sum(item.price for item in self.items)

    def final_amount(self):
        return self.total() - self.total_coupon_reductions()

    def calculate_coupon_reduction(self, coupon):
        items = [item for item in cart if item.name == coupon.item_name]
        reduction = 0.0
        if len(items) >= mininum_amount:
            if coupon.reduction_type == 'percent':
                item_amount = sum(item.price for item in items)
                reduction += item_amount * coupon.reduction_amount
            elif coupon.reduction_type == 'absolute':
                reduction += coupon.reduction_amount
            elif reduction_type == 'per-item':
                reduction += coupon.reduction_amount * len(items)
        return reduction

    def total_coupon_reductions(self):
        total = 0
        for coupon in self.coupons:
            total += self.calculate_coupon_reduction(coupon)
        return total

class Coupon:
    def __init__(self, item_name, mininum_amount=1, reduction_type, reduction_amount):
        self.item_name = item_name
        self.mininum_amount = mininum_amount
        self.reduction_type = reduction_type
        self.reduction_amount = reduction_amount
