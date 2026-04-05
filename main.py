# Define a class Order
class Order:
    def __init__(self, order_number, order_type, order_amount):
        # Initialize an Order object with order number, order type, and order amount
        self.order_number = order_number
        self.order_type = order_type
        self.order_amount = order_amount

# Define a class OrderManager
class OrderManager:
    def __init__(self):
        self.orders = []
    # Function to add a new order to the list
    def add_order(self):
        # Prompt the user to input order details
        order_number = input("Enter Order Number: ")
        order_type = input("Enter Order Type: ")
        order_amount = float(input("Enter Order Amount: "))
        # Create an Order object and add it to the list of orders
        order = Order(order_number, order_type, order_amount)
        self.orders.append(order)
        print("Order added successfully.")
    # Function to delete an order from the list
    def delete_order(self):
        # Prompt the user to enter the order number to be deleted
        order_number = input("Enter Order Number to delete: ")
        # Iterate through the list of orders
        for order in self.orders:
            # Check if the order number matches
            if order.order_number == order_number:
                # Remove the matching order from the list
                self.orders.remove(order)
                print("Order deleted successfully.")
                break
        else:
            # If the order is not found, display a message
            print("Order not found.")
    # Function to edit the details of an existing order
    def edit_order(self):
        # Prompt the user to enter the order number to be edited
        order_number = input("Enter Order Number to edit: ")
        # Iterate through the list of orders
        for order in self.orders:
            # Check if the order number matches
            if order.order_number == order_number:
                # Prompt the user to input new order type and amount
                order_type = input("Enter new Order Type: ")
                order_amount = float(input("Enter new Order Amount: "))
                # Update the order's type and amount
                order.order_type = order_type
                order.order_amount = order_amount
                print("Order edited successfully.")
                break
        else:
            # If the order is not found, display a message
            print("Order not found.")
    # Function to display all orders in the list
    def display_orders(self):
        print("\n--- Orders ---")
        for order in self.orders:
            # Print the details of each order
            print(f"Order Number: {order.order_number}, Order Type: {order.order_type}, Order Amount: {order.order_amount}")
    # Function to save orders to a text file
    def save_orders_to_file(self):
        with open("orders.txt", "w") as file:
            for order in self.orders:
                print("Orders saved to text file")
                # Write each order's details to a text file
                file.write(f"{order.order_number},{order.order_type},{order.order_amount}\n")
# Function to display the main menu to the user
def display_menu():
    print("\n------Welcome to Malik Goggins Steakhouse------")
    print("1. Add Order")
    print("2. Delete Order")
    print("3. Edit Order")
    print("4. Display Orders")
    print("5. Save Orders to File")
    print("6. Exit the Program")
if __name__ == "__main__":
    order_manager = OrderManager()
    choice = 0
    while choice != 6:
        display_menu()
        # Prompt the user to enter their choice
        choice = int(input("Enter your choice: "))
        if choice == 1:
            order_manager.add_order()
        elif choice == 2:
            order_manager.delete_order()
        elif choice == 3:
            order_manager.edit_order()
        elif choice == 4:
            order_manager.display_orders()
        elif choice == 5:
            order_manager.save_orders_to_file()
        elif choice == 6:
            print("Exiting the program.")
        else:
            # If an invalid choice is entered, display a message
            print("Invalid choice. Please try again.")
