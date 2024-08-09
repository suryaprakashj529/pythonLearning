class Inventory:
    def __init__(self, max_capacity):
        # Write your code here.
        self.max_capacity = max_capacity
        self.items = {}
        self.item_count =0
        

    def add_item(self, name, price, quantity):
        # Write your code here.
        if name in self.items:
            return False

        if self.item_count + quantity > self.max_capacity:
            return False

        self.items[name] = {"name": name, "price": price, "quantity": quantity}
        self.item_count += quantity
        return True
        

    def delete_item(self, name):
        # Write your code here.
        if name not in self.items:
            return False

        self.item_count -= self.items[name]["quantity"]
        del self.items[name]
        return True

    def get_items_in_price_range(self, min_price, max_price):
        # Write your code here.
        item_names =[]

        for item in self.items.values():
            name = item["name"]
            price = item["price"]

            if min_price <= price <= max_price:
                item_names.append(name)

        return item_names

    def get_most_stocked_item(self):
        # Write your code here.
        most_stocked_item_name = None
        largest_quantity = 0

        for item in self.items.values():
            name = item["name"]
            quantity = item["quantity"]

            if quantity > largest_quantity:
                most_stocked_item_name = name
                largest_quantity = quantity
        return most_stocked_item_name