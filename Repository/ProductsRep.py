class ProductsRep(object):

    def __init__(self):
        self.products = []

    def add(self, product):
        self.products.append(product)

    def delete(self, product):
        self.products.remove(product)

    def change(self, product):
        for i in range(0, len(self.products)):
            if self.products[i].getIds() == product.getIds():
                self.products[i] = product

    def getRep(self):
        return self.products
