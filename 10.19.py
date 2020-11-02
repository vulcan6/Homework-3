# Erick Jimenez
# PSID: 1463639
# Zylab 10.19

class ItemToPurchase:
    def __init__(self, name='none', price=0, quantity=0, description='none'):
        self.item_name = name
        self.item_description = description
        self.item_price = price
        self.item_quantity = quantity

    def print_item_description(self):
        print('%s: %s' % (self.item_name, self.item_description))


class ShoppingCart:
    def __init__(self, customer_name='none', current_date='January 1, 2016', cart_items=[]):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = cart_items


    def add_item(self, itemToPurchase):
        self.cart_items.append(itemToPurchase)

    def remove_item(self, itemName):

        to_remove_item = False
        for item in self.cart_items:
            if item.item_name == itemName:
                self.cart_items.remove(item)
                to_remove_item = True
                break

        if not to_remove_item:
            print('Item not found in cart. Nothing removed.')

    def get_cost_of_cart(self):
        total_cost = 0
        for item in self.cart_items:
            cost = (item.item_quantity * item.item_price)
            total_cost += cost
        return total_cost

    def get_num_items_in_cart(self):
        num_items = 0
        for item in self.cart_items:
            num_items = num_items + item.item_quantity
        return num_items



    def print_total(self):
        total_cost = self.get_cost_of_cart()
        if (total_cost == 0):
            print('SHOPPING CART IS EMPTY')
        else:
            print('{}\'s Shopping Cart - {}'.format(self.customer_name, self.current_date))
            print('Number of Items: %d\n' % self.get_num_items_in_cart())
            for item in self.cart_items:
                total = item.item_price * item.item_quantity
                print('%s %d @ $%d = $%d' % (item.item_name, item.item_quantity, item.item_price, total))

            print('\nTotal: $%d' % (total_cost))


    def print_descriptions(self):
        if len(self.cart_items) == 0:
            print('SHOPPING CART IS EMPTY')
        else:
            print('{}\'s Shopping Cart - {}'.format(self.customer_name, self.current_date))
            print('\nItem Descriptions')
            for item in self.cart_items:
                item.print_item_description()

    def modify_item(self, itemToPurchase):
        to_modify_item = False
        for i in range(len(self.cart_items)):
            if self.cart_items[i].item_name == itemToPurchase.item_name:
                to_modify_item = True
                self.cart_items[i].item_quantity = itemToPurchase.item_quantity
                break
        if not to_modify_item:
            print('Item not found in cart. Nothing modified.')


    def print_descriptions(self):
        if len(self.cart_items) == 0:
            print('SHOPPING CART IS EMPTY')
        else:
            print('{}\'s Shopping Cart - {}'.format(self.customer_name, self.current_date))
            print('\nItem Descriptions')
            for item in self.cart_items:
                item.print_item_description()



def print_menu(newCart):
    customer_Cart = newCart
    menu = ('\nMENU\n'
            'a - Add item to cart\n'
            'r - Remove item from cart\n'
            'c - Change item quantity\n'
            "i - Output items' descriptions\n"
            'o - Output shopping cart\n'
            'q - Quit\n')

    command = ''
    while (command != 'q'):
        print(menu)
        command = input('Choose an option:\n')
        while (
                command != 'a' and command != 'o' and command != 'i' and command != 'q' and command != 'r' and command != 'c'):
            command = input('Choose an option:\n')
        if (command == 'a'):
            print("\nADD ITEM TO CART")
            item_name = input('Enter the item name:\n')
            item_description = input('Enter the item description:\n')
            item_price = int(input('Enter the item price:\n'))
            item_quantity = int(input('Enter the item quantity:\n'))
            itemtoPurchase = ItemToPurchase(item_name, item_price, item_quantity, item_description)
            customer_Cart.add_item(itemtoPurchase)

        elif (command == 'o'):
            print('OUTPUT SHOPPING CART')
            customer_Cart.print_total()
        elif (command == 'i'):
            print('OUTPUT ITEMS\' DESCRIPTIONS')
            customer_Cart.print_descriptions()
        elif (command == 'r'):
            print('REMOVE ITEM FROM CART')
            itemName = input('Enter name of item to remove:\n')
            customer_Cart.remove_item(itemName)
        elif (command == 'c'):
            print('\nCHANGE ITEM QUANTITY')
            itemName = input('Enter the item name:\n')
            quantity = int(input('Enter the new quantity:\n'))
            itemToPurchase = ItemToPurchase(itemName, 0, quantity)
            customer_Cart.modify_item(itemToPurchase)


if __name__ == "__main__":
    customer_name = input("Enter customer's name:")
    current_date = input("Enter today's date:")
    print("\nCustomer name: %s" % customer_name)
    print("Today's date: %s" % current_date)
    newCart = ShoppingCart(customer_name, current_date)
    print_menu(newCart)