# Robert Stewart
# CSC500
# 2021/03/07


class ItemToPurchase:
    def __init__(self):
        self.item_name = str('none')
        self.item_cost = float(0)
        self.item_quantity = int(0)

    def print_item_cost(self):
        print (self.item_name + " - " + str(self.item_quantity) + " @ $" + str("{:.2f}".format(self.item_cost)) + " = $" + str("{:.2f}".format(self.item_quantity * self.item_cost)))

class ShoppingCart:
    def __init__(self):
        self.customer_name = str('none')
        self.current_date = str('January 1, 2020')
        self.cart_items = list([])
    
    def add_item(self):
        item_to_purchase = ItemToPurchase()
        item_to_purchase.item_name = str(input("Enter the name of the item: "))
        item_to_purchase.item_cost = float(input("Enter the cost of the item: $"))
        item_to_purchase.item_quantity = int(input("Enter the count of this item: "))
        self.cart_items.append(item_to_purchase)
        self.print_menu()

    def remove_item(self):
        self.print_items()
        item_removed = int(input('Which item would you like to remove? Enter the corresponding number:'))
        self.cart_items.pop(item_removed)
        self.print_menu()


    def print_total(self):
        k = 0
        total_cost = 0.0
        print(self.customer_name + '\'s shopping cart - ' + self.current_date)
        item_count = self.get_num_items_in_cart()
        if item_count == 0:
            print('SHOPPING CART IS EMPTY')
            self.print_menu()
        else:
            for k in range(0,item_count):
                self.cart_items[k].print_item_cost() 
            self.get_cost_of_cart()
        self.print_menu()

    def get_cost_of_cart(self):
        k = 0
        total_cost = 0.0
        item_count = self.get_num_items_in_cart()
        for k in range(0,item_count):
            total_cost += (self.cart_items[k].item_quantity * self.cart_items[k].item_cost)
        print("The total cost is $" + str("{:.2f}".format(total_cost)))

    def print_menu(self):
        print('MENU')
        print('a - Add item to cart')
        print('r - Remove item from cart')
        print('c - Change item')
        print('i - Output items descriptions')
        print('o - Output shoppingcart')
        print('q - Quit')
        choice = input('Choose an item:')
        if choice == 'a':
            self.add_item()
        if choice == 'r':
            self.remove_item()
        if choice == 'c':
            self.modify_item()
        if choice == 'i':
            self.print_descriptions()
        if choice == 'o':
            self.print_total()
        if choice == 'q':
            print('quitting')
            
    def print_items(self):
        list_length = len(self.cart_items)
        for i in range(0,list_length):
            print(str(i) +' - ' +self.cart_items[i].item_name)

    def get_num_items_in_cart(self):
        list_length = len(self.cart_items)
        return list_length

    def print_descriptions(self):
        print('OUTPUT ITEMS DESCRIPTIONS')
        print(self.customer_name + '\'s shopping cart - ' + self.current_date)
        list_length = self.get_num_items_in_cart()
        for i in range(0,list_length):
            print(self.cart_items[i].item_name)
        self.print_menu()

    def modify_item(self):
        self.print_items()
        item_number = int(input('Which item would you like to modify? Enter the corresponding number:'))
        this_item = self.cart_items[item_number]
        print('What attribute would you like to modify?')
        print('1 - Item name')
        print('2 - Item quantity')
        print('3 - Item cost')
        item_attribute = int(input('Enter your choice: '))
        if item_attribute == 1:
            this_item.item_name = input('What is the new item name? ')
        elif item_attribute == 2:
            this_item.item_quantity = input('What is the new item quantity? ')
        elif item_attribute == 3:
            this_item.item_cost = input('What is the new item cost? $')
        self.print_menu()

def Main():

    print("This program will allow you to manage a shopping cart. Follow each instruction and hit enter.")

    this_customer = ShoppingCart()
    this_customer.customer_name = input("What is the customer name? ")
    this_customer.current_date = input("Enter the date: ")
    print('Let\'s add your first item')
    this_customer.add_item()
    
    
#offer to start a new order
    print("Do you want to make another order?")
    usr1 = input("Y/N: ")
    if usr1.upper() == "Y":
        Main()
    else:
        print("Thank you!")







Main()
