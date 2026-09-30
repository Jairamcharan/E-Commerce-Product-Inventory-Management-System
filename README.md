# E-Commerce Product & Inventory Management System


## Features

- Add new products
- Store product name, category, price, and stock
- View products in a graphical table
- Search products by name or category
- Add stock
- Record sales
- Automatically reduce stock after a sale
- Delete products
- Store data permanently using SQLite
- Validate user input

## Technologies

- Python 3
- SQL
- CRUD Operations


`inventory.db` is automatically created when the application is run.

## How to Run

No external Python packages are required.

Run:

```bash
python app.py
```

The application will automatically create the SQLite database.

## How It Works

```text
User
Tkinter GUI
 Add Product
Search Product
 Add Stock
 Record Sale
 Delete Product
 SQLite Database
 Products Table
 Sales Table
```

## Database Design

### Products

| Column | Purpose |
|---|---|
| id | Unique product ID |
| name | Product name |
| category | Product category |
| price | Product price |
| stock | Available quantity |

### Sales

| Column | Purpose |
|---|---|
| id | Sale ID |
| product_id | Related product |
| quantity | Quantity sold |
| total | Total sale value |


**E-Commerce Product & Inventory Management System | Python, SQLite**

Developed a desktop-based inventory management application using Python and Tkinter with SQLite for persistent data storage. Implemented product management, search, stock updates, sales recording, automatic stock reduction, and input validation. Used SQL queries and CRUD operations to manage product and sales data.

**Technologies:** Python, SQLite, SQL


## Possible Future Improvements

- Shopping cart
- Customer management
- Login system
- Sales dashboard
- Monthly sales reports
- Export reports to CSV
