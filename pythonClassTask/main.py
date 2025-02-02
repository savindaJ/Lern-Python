# from product import Product # type: ignore
# from customer import Customer # type: ignore
# from order import Order # type: ignore
# from inventory import Inventory # type: ignore




class ECommerceSystem:
   def __init__(self):
       self.products = []
       self.customers = []
       self.orders = []
       self.inventory = []


   def main_menu(self):
       while True:
           print("\n--- E-Commerce Management System ---")
           print("1. Product Management")
           print("2. Customer Management")
           print("3. Order Management")
           print("4. Inventory Management")
           print("5. Exit")


           try:
               choice = input("Enter your choice (1-4): ")


               if choice == '1':
                   self.product_menu()
               elif choice == '2':
                   self.customer_menu()
               elif choice == '3':
                   self.order_menu()
               elif choice == '4':
                   self.inventory_menu()
               elif choice == '5':
                   print("Exiting the system. Goodbye!")
                   break
               else:
                   print("Invalid choice. Please enter a number between 1-4.")


           except Exception as e:
               print(f"An error occurred: {e}")


   def product_menu(self):
       while True:
           print("\n--- Product Management ---")
           print("1. Add Product")
           print("2. Update Product")
           print("3. View Products")
           print("4. Back")


           try:
               choice = input("Enter your choice (1-4): ")


               if choice == '1':
                   name = input("Enter product name: ")
                   price = float(input("Enter product price: "))
                   quantity = int(input("Enter product quantity: "))
                   new_product = product(name, price, quantity)
                   self.products.append(new_product)
                   print("Product added successfully!")


               elif choice == '2':
                   if not self.products:
                       print("No products available to update.")
                       continue


                   for i, p in enumerate(self.products, 1):
                       print(f"{i}. {p.get_details()}")


                   index = int(input("Enter product number to update: ")) - 1
                   if 0 <= index < len(self.products):
                       product = self.products[index]
                       print("1. Update Price\n2. Update Quantity")
                       update_choice = input("Enter choice: ")


                       if update_choice == '1':
                           new_price = float(input("Enter new price: "))
                           product.update_price(new_price)
                       elif update_choice == '2':
                           new_quantity = int(input("Enter new quantity: "))
                           product.update_quantity(new_quantity)
                       print("Product updated successfully!")


               elif choice == '3':
                   for p in self.products:
                       print(p.get_details())


               elif choice == '4':
                   break


               else:
                   print("Invalid choice. Please enter a number between 1-4.")


           except ValueError:
               print("Invalid input. Please enter a valid number.")
           except Exception as e:
               print(f"An error occurred: {e}")


   def customer_menu(self):
       while True:
           print("\n--- Customer Management ---")
           print("1. Add Customer")
           print("2. Update Customer")
           print("3. View Customers")
           print("4. Back")


           try:
               choice = input("Enter your choice (1-4): ")


               if choice == '1':
                   name = input("Enter customer name: ")
                   address = input("Enter customer address: ")
                   contact = input("Enter customer contact: ")
                   new_customer = Customer(name, address, contact)
                   self.customers.append(new_customer)
                   print("Customer added successfully!")


               elif choice == '2':
                   if not self.customers:
                       print("No customers available to update.")
                       continue


                   for i, c in enumerate(self.customers, 1):
                       print(f"{i}. {c.get_details()}")


                   index = int(input("Enter customer number to update: ")) - 1
                   if 0 <= index < len(self.customers):
                       customer = self.customers[index]
                       print("1. Update Address\n2. Update Contact")
                       update_choice = input("Enter choice: ")


                       if update_choice == '1':
                           new_address = input("Enter new address: ")
                           customer.address = new_address
                       elif update_choice == '2':
                           new_contact = input("Enter new contact: ")
                           customer.contact = new_contact
                       print("Customer updated successfully!")


               elif choice == '3':
                   for c in self.customers:
                       print(c.get_details())


               elif choice == '4':
                   break


               else:
                   print("Invalid choice. Please enter a number between 1-4.")


           except ValueError:
               print("Invalid input. Please enter a valid number.")
           except Exception as e:
               print(f"An error occurred: {e}")


   def order_menu(self):
       while True:
           print("\n--- Order Management ---")
           print("1. Create Order")
           print("2. Add Product to Order")
           print("3. View Orders")
           print("4. Back")


           try:
               choice = input("Enter your choice (1-4): ")


               if choice == '1':
                   if not self.customers or not self.products:
                       print("Need customers and products first.")
                       continue


                   print("Select Customer:")
                   for i, c in enumerate(self.customers, 1):
                       print(f"{i}. {c.get_details()}")


                   customer_index = int(input("Enter customer number: ")) - 1
                   customer = self.customers[customer_index]


                   order = Order(customer, len(self.orders) + 1)


                   while True:
                       print("Select Product:")
                       for i, p in enumerate(self.products, 1):
                           print(f"{i}. {p.get_details()}")


                       product_index = int(input("Enter product number (0 to finish): ")) - 1


                       if product_index == -1:
                           break


                       quantity = int(input("Enter quantity: "))
                       order.add_product(self.products[product_index], quantity)


                   order.calculate_total()
                   self.orders.append(order)
                   print("Order created successfully!")


               elif choice == '2':
                   if not self.orders:
                       print("No orders available.")
                       continue


                   print("Select Order:")
                   for i, o in enumerate(self.orders, 1):
                       print(f"{i}. Order ID: {o.order_id}, Customer: {o.customer.name}")


                   order_index = int(input("Enter order number: ")) - 1
                   order = self.orders[order_index]


                   print("Select Product:")
                   for i, p in enumerate(self.products, 1):
                       print(f"{i}. {p.get_details()}")


                   product_index = int(input("Enter product number: ")) - 1
                   quantity = int(input("Enter quantity: "))
                   order.add_product(self.products[product_index], quantity)
                   order.calculate_total()
                   print("Product added to order successfully!")


               elif choice == '3':
                   for order in self.orders:
                       print(order.generate_summary())


               elif choice == '4':
                   break


               else:
                   print("Invalid choice. Please enter a number between 1-4.")


           except ValueError:
               print("Invalid input. Please enter a valid number.")
           except Exception as e:
               print(f"An error occurred: {e}")


   def inventory_menu(self):


       while True:
           print("\n--- Inventory Management ---")
           print("1. Add Product to Inventory")
           print("2. Remove Product from Inventory")
           print("3. Check Stock")
           print("4. Back")


           try:
               choice = input("Enter your choice (1-4): ")


               if choice == '1':
                   if not self.products:
                       print("No products available to add to inventory.")
                       continue


                   print("Select Product:")
                   for i, p in enumerate(self.products, 1):
                       print(f"{i}. {p.get_details()}")


                   product_index = int(input("Enter product number: ")) - 1
                   product = self.products[product_index]
                   self.inventory.add_product(product)
                   print("Product added to inventory successfully!")


               elif choice == '2':
                   product_name = input("Enter product name: ")
                   quantity = int(input("Enter quantity: "))
                   self.inventory.remove_product(product_name, quantity)


               elif choice == '3':
                   product_name = input("Enter product name: ")
                   stock = self.inventory.check_stock(product_name)
                   print(f"Stock for {product_name}: {stock}")


               elif choice == '4':
                   break


               else:
                   print("Invalid choice. Please enter a number between 1-4.")


           except ValueError:
               print("Invalid input. Please enter a valid number.")
           except Exception as e:
               print(f"An error occurred: {e}")




def main():
   system = ECommerceSystem()
   system.main_menu()




if __name__ == "__main__":
   main()