import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox

DB_NAME = "inventory.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def setup_database():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL,
            stock INTEGER NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sales (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_id INTEGER NOT NULL,
            quantity INTEGER NOT NULL,
            total REAL NOT NULL
        )
    """)

    conn.commit()
    conn.close()


def add_product():
    name = name_entry.get().strip()
    category = category_entry.get().strip()
    price_text = price_entry.get().strip()
    stock_text = stock_entry.get().strip()

    if not name or not category or not price_text or not stock_text:
        messagebox.showwarning("Input Error", "Please fill all fields.")
        return

    try:
        price = float(price_text)
        stock = int(stock_text)

        if price < 0 or stock < 0:
            raise ValueError

    except ValueError:
        messagebox.showerror("Input Error", "Enter a valid price and stock.")
        return

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO products (name, category, price, stock) VALUES (?, ?, ?, ?)",
        (name, category, price, stock)
    )

    conn.commit()
    conn.close()

    clear_fields()
    load_products()
    messagebox.showinfo("Success", "Product added successfully.")


def load_products(search=""):
    for item in product_table.get_children():
        product_table.delete(item)

    conn = get_connection()
    cursor = conn.cursor()

    if search:
        cursor.execute(
            """SELECT id, name, category, price, stock
               FROM products
               WHERE name LIKE ? OR category LIKE ?""",
            (f"%{search}%", f"%{search}%")
        )
    else:
        cursor.execute(
            "SELECT id, name, category, price, stock FROM products"
        )

    for row in cursor.fetchall():
        product_table.insert("", tk.END, values=row)

    conn.close()


def update_stock():
    selected = product_table.selection()

    if not selected:
        messagebox.showwarning("Selection", "Select a product first.")
        return

    product_id = product_table.item(selected[0])["values"][0]

    quantity_text = quantity_entry.get().strip()

    try:
        quantity = int(quantity_text)
        if quantity <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Input Error", "Enter a positive quantity.")
        return

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE products SET stock = stock + ? WHERE id = ?",
        (quantity, product_id)
    )

    conn.commit()
    conn.close()

    quantity_entry.delete(0, tk.END)
    load_products()
    messagebox.showinfo("Success", "Stock updated successfully.")


def record_sale():
    selected = product_table.selection()

    if not selected:
        messagebox.showwarning("Selection", "Select a product first.")
        return

    product_id, name, category, price, stock = product_table.item(
        selected[0]
    )["values"]

    quantity_text = quantity_entry.get().strip()

    try:
        quantity = int(quantity_text)
        if quantity <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Input Error", "Enter a positive quantity.")
        return

    if quantity > int(stock):
        messagebox.showerror("Stock Error", "Not enough stock available.")
        return

    total = float(price) * quantity

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE products SET stock = stock - ? WHERE id = ?",
        (quantity, product_id)
    )

    cursor.execute(
        "INSERT INTO sales (product_id, quantity, total) VALUES (?, ?, ?)",
        (product_id, quantity, total)
    )

    conn.commit()
    conn.close()

    quantity_entry.delete(0, tk.END)
    load_products()

    messagebox.showinfo(
        "Sale Recorded",
        f"Product: {name}\nQuantity: {quantity}\nTotal: ₹{total:.2f}"
    )


def delete_product():
    selected = product_table.selection()

    if not selected:
        messagebox.showwarning("Selection", "Select a product first.")
        return

    product_id = product_table.item(selected[0])["values"][0]

    confirm = messagebox.askyesno(
        "Confirm Delete",
        "Are you sure you want to delete this product?"
    )

    if not confirm:
        return

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM products WHERE id = ?", (product_id,))

    conn.commit()
    conn.close()

    load_products()
    messagebox.showinfo("Success", "Product deleted.")


def clear_fields():
    name_entry.delete(0, tk.END)
    category_entry.delete(0, tk.END)
    price_entry.delete(0, tk.END)
    stock_entry.delete(0, tk.END)


def search_products():
    load_products(search_entry.get().strip())


def clear_search():
    search_entry.delete(0, tk.END)
    load_products()


setup_database()

root = tk.Tk()
root.title("E-Commerce Product & Inventory Management")
root.geometry("900x600")

title = ttk.Label(
    root,
    text="E-Commerce Product & Inventory Management",
    font=("Arial", 18, "bold")
)
title.pack(pady=15)

form = ttk.Frame(root)
form.pack(pady=5)

ttk.Label(form, text="Product Name").grid(row=0, column=0, padx=5, pady=5)
name_entry = ttk.Entry(form, width=22)
name_entry.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(form, text="Category").grid(row=0, column=2, padx=5, pady=5)
category_entry = ttk.Entry(form, width=22)
category_entry.grid(row=0, column=3, padx=5, pady=5)

ttk.Label(form, text="Price").grid(row=1, column=0, padx=5, pady=5)
price_entry = ttk.Entry(form, width=22)
price_entry.grid(row=1, column=1, padx=5, pady=5)

ttk.Label(form, text="Stock").grid(row=1, column=2, padx=5, pady=5)
stock_entry = ttk.Entry(form, width=22)
stock_entry.grid(row=1, column=3, padx=5, pady=5)

ttk.Button(form, text="Add Product", command=add_product).grid(
    row=2, column=0, columnspan=4, pady=10
)

search_frame = ttk.Frame(root)
search_frame.pack(pady=10)

ttk.Label(search_frame, text="Search").pack(side=tk.LEFT, padx=5)
search_entry = ttk.Entry(search_frame, width=30)
search_entry.pack(side=tk.LEFT, padx=5)

ttk.Button(search_frame, text="Search", command=search_products).pack(
    side=tk.LEFT, padx=5
)

ttk.Button(search_frame, text="Clear", command=clear_search).pack(
    side=tk.LEFT, padx=5
)

columns = ("ID", "Name", "Category", "Price", "Stock")

product_table = ttk.Treeview(
    root,
    columns=columns,
    show="headings",
    height=15
)

for column in columns:
    product_table.heading(column, text=column)
    product_table.column(column, width=140)

product_table.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

action_frame = ttk.Frame(root)
action_frame.pack(pady=10)

ttk.Label(action_frame, text="Quantity").pack(side=tk.LEFT, padx=5)
quantity_entry = ttk.Entry(action_frame, width=10)
quantity_entry.pack(side=tk.LEFT, padx=5)

ttk.Button(
    action_frame,
    text="Add Stock",
    command=update_stock
).pack(side=tk.LEFT, padx=5)

ttk.Button(
    action_frame,
    text="Record Sale",
    command=record_sale
).pack(side=tk.LEFT, padx=5)

ttk.Button(
    action_frame,
    text="Delete Product",
    command=delete_product
).pack(side=tk.LEFT, padx=5)

load_products()

root.mainloop()
