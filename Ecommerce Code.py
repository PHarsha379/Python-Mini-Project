# ============================================================
#            MINI E-COMMERCE SYSTEM
# ============================================================

users = []
current_user = None

products = [
    {"id": 1, "name": "iPhone 15", "price": 65000, "stock": 10},
    {"id": 2, "name": "Samsung Galaxy S24", "price": 72000, "stock": 8},
    {"id": 3, "name": "HP Laptop", "price": 55000, "stock": 6},
    {"id": 4, "name": "Dell Laptop", "price": 62000, "stock": 5},
    {"id": 5, "name": "Sony Headphones", "price": 8000, "stock": 15},
    {"id": 6, "name": "Boat Earbuds", "price": 1500, "stock": 25},
    {"id": 7, "name": "Nike Shoes", "price": 4500, "stock": 12},
    {"id": 8, "name": "Adidas T-Shirt", "price": 1800, "stock": 20},
]

cart = []  # list of {"id", "name", "price", "qty"}
PAYMENT_METHODS = ("UPI", "CARD", "COD")


def find_product(pid):
    for p in products:
        if p["id"] == pid:
            return p
    return None


def is_valid_username(username):
    # Must start with a letter, and must contain at least one
    # special symbol somewhere in the middle or at the end.
    if not username or not username[0].isalpha():
        return False
    if not any(not ch.isalnum() for ch in username[1:]):
        return False
    return True


def is_valid_password(password):
    # Must contain letters, numbers, and special symbols together.
    has_letter = any(ch.isalpha() for ch in password)
    has_digit = any(ch.isdigit() for ch in password)
    has_special = any(not ch.isalnum() for ch in password)
    return has_letter and has_digit and has_special


def register():
    username = input("Choose username: ")
    if not is_valid_username(username):
        print("Invalid username. Must start with a letter and include a special symbol in the middle/end (e.g. harsha_1).")
        return
    for u in users:
        if u["username"] == username:
            print("User already exists.")
            return
    password = input("Choose password: ")
    if not is_valid_password(password):
        print("Invalid password. Must include letters, numbers, and a special symbol (e.g. Harsha@123).")
        return
    users.append({"username": username, "password": password})
    print("Registered successfully! Please login.")


def login():
    global current_user
    username = input("Username: ")
    password = input("Password: ")
    for u in users:
        if u["username"] == username and u["password"] == password:
            current_user = u
            print(f"Welcome, {username}!")
            return
    print("Invalid credentials.")


def show_products():
    print("\nID  Name                 Price     Stock")
    print("-" * 45)
    for p in products:
        print(f"{p['id']:<4}{p['name']:<21}₹{p['price']:<9}{p['stock']}")


def add_to_cart():
    show_products()
    pid = int(input("Enter product ID to add: "))
    product = find_product(pid)
    if not product:
        print("Product not found.")
        return
    qty = int(input("Enter quantity: "))
    if qty <= 0 or qty > product["stock"]:
        print("Invalid quantity.")
        return
    for item in cart:
        if item["id"] == pid:
            item["qty"] += qty
            print("Cart updated.")
            return
    cart.append({"id": pid, "name": product["name"], "price": product["price"], "qty": qty})
    print("Added to cart.")


def remove_from_cart():
    if not cart:
        print("Cart is empty.")
        return
    view_cart()
    pid = int(input("Enter product ID to remove: "))
    for item in cart:
        if item["id"] == pid:
            cart.remove(item)
            print("Removed from cart.")
            return
    print("Item not in cart.")
#-----------------------------------------------------------------------------------------------

def view_cart():
    if not cart:
        print("\nCart is empty.")
        return
    print("\n--- CART ---")
    total = 0
    for item in cart:
        subtotal = item["price"] * item["qty"]
        total += subtotal
        print(f"{item['name']} x{item['qty']} = ₹{subtotal}")
    print(f"Total: ₹{total}")


def checkout():
    if not cart:
        print("Cart is empty. Add products first.")
        return
    view_cart()
    total = sum(item["price"] * item["qty"] for item in cart)

    print("\nPayment Methods:", ", ".join(PAYMENT_METHODS))
    method = input("Choose payment method: ").upper()
    if method not in PAYMENT_METHODS:
        print("Invalid payment method.")
        return

    print(f"\nOrder placed successfully using {method}! Total paid: ₹{total}")
    cart.clear()


def user_menu():
    while True:
        print("\n===== MENU =====")
        print("1. Show Products")
        print("2. Add to Cart")
        print("3. View Cart")
        print("4. Remove from Cart")
        print("5. Checkout")
        print("6. Logout")

        choice = input("Enter choice: ")

        if choice == "1":
            show_products()
        elif choice == "2":
            add_to_cart()
        elif choice == "3":
            view_cart()
        elif choice == "4":
            remove_from_cart()
        elif choice == "5":
            checkout()
            cont = input("Continue shopping? (y/n): ").lower()
            if cont != "y":
                break
        elif choice == "6":
            break
        else:
            print("Invalid choice.")


def main():
    global current_user
    while True:
        print("\n===== E-COMMERCE SYSTEM =====")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            register()
        elif choice == "2":
            login()
            if current_user:
                user_menu()
                current_user = None
        elif choice == "3":
            print("Thank you for shopping!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
