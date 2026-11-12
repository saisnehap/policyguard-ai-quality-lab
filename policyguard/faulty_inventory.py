
from policyguard.inventory import Inventory


class FaultyInventory(Inventory):

    def reserve_stock(self, product_id, quantity):
        if product_id not in self.stock:
            return False

        if quantity <= 0:
            return False

        if self.stock[product_id] < quantity:
            return False

        # Intentional defect:
        # Reports success without reducing stock.
        return True

class DoubleReservationInventory(Inventory):

    def reserve_stock(self, product_id, quantity):
        if product_id not in self.stock:
            return False

        if quantity <= 0:
            return False

        if self.stock[product_id] < quantity * 2:
            return False

        # Intentional defect: reserves twice.
        self.stock[product_id] -= quantity * 2
        return True


class WrongProductInventory(Inventory):

    def reserve_stock(self, product_id, quantity):
        if product_id not in self.stock:
            return False

        if quantity <= 0:
            return False

        if self.stock[product_id] < quantity:
            return False

        # Intentional defect: modifies the wrong item.
        self.stock["mouse"] -= quantity
        return True

class UnauthorizedActionInventory(Inventory):

    def __init__(self):
        super().__init__()
        self.actions = []

    def reserve_stock(self, product_id, quantity):
        if product_id not in self.stock:
            return False

        if quantity <= 0:
            return False

        if self.stock[product_id] < quantity:
            return False

        # Correct reservation
        self.stock[product_id] -= quantity
        self.actions.append("reserve")

        # Intentional unauthorized temporary change
        self.stock["mouse"] -= 1
        self.actions.append("unauthorized_modify_mouse")

        # Restore the mouse count
        self.stock["mouse"] += 1
        self.actions.append("restore_mouse")

        return True
