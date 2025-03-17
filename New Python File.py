import sqlite3


conn = sqlite3.connect("inventory.db")
cursor = conn.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    price REAL NOT NULL
)
''')
conn.commit()

def add_product(name, quantity, price):
    """Adds a new product to the inventory."""
    cursor.execute("INSERT INTO products (name, quantity, price) VALUES (?, ?, ?)", (name, quantity, price))
    conn.commit()
    print(f"Product '{name}' added successfully!")

def update_product(product_id, quantity):
    """Updates the stock of an existing product."""
    cursor.execute("UPDATE products SET quantity = ? WHERE id = ?", (quantity, product_id))
    conn.commit()
    print(f"Product ID {product_id} updated successfully!")

def view_products():
    """Displays all products in the inventory."""
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    print("\nID | Name | Quantity | Price")
    print("-"*30)
    for product in products:
        print(f"{product[0]} | {product[1]} | {product[2]} | ${product[3]}")

def delete_product(product_id):
    """Deletes a product from the inventory."""
    cursor.execute("DELETE FROM products WHERE id = ?", (product_id,))
    conn.commit()
    print(f"Product ID {product_id} deleted successfully!")


if __name__ == "__main__":
    add_product("Laptop", 10, 750.00)
    add_product("Mouse", 50, 20.00)
    view_products()
    update_product(1, 8)
    view_products()
    delete_product(2)
    view_products()

conn.close()
