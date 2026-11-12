 
class Inventory:
    def __init__(self):
        self.stock = {
            "laptop": 10,
            "mouse": 20,
            "keyboard": 15
        }

    def check_stock(self, product_id):
        return self.stock.get(product_id, 0)

    def reserve_stock(self, product_id, quantity):
        if product_id not in self.stock:
            return False

        if quantity <= 0:
            return False

        if self.stock[product_id] < quantity:
            return False

        self.stock[product_id] -= quantity
        return True

    def get_inventory_state(self):
        return self.stock.copy()
