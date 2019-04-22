class ItemToPurchase:
    item_name = str()
    item_price = float()
    item_quantity = int()

    def __init__(self, item_name="none", item_price=float(0), item_quantity=int(0)):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self):
        print(self.item_name, self.item_quantity, "@", "$" + str(self.item_price * self.item_quantity))


if __name__ == "__main__":
    print("Item 1")
    item_one = ItemToPurchase(input("Enter the item name; "), float(input("Enter the item price: ")),
                              int(input("Enter the item quantity")))

    print("Item 2")
    item_two = ItemToPurchase(input("Enter the item name; "), float(input("Enter the item price: ")),
                              int(input("Enter the item quantity")))

    total_price = (item_one.item_price * item_one.item_quantity) + (item_two.item_price * item_two.item_quantity)
    print("TOTAL COST")
    item_one.print_item_cost()
    item_two.print_item_cost()
    print("Total: ", "$" + str(total_price))
