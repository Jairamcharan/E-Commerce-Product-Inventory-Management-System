# E-Commerce Product & Inventory Management System

A moderate-level desktop application developed using Python, Tkinter, and SQLite.

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
- Tkinter
- SQLite
- SQL
- CRUD Operations

## Project Structure

```text
ecommerce-product-inventory/
├── app.py
├── README.md
└── .gitignore
```

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
  |
  v
Tkinter GUI
  |
  +--> Add Product
  |
  +--> Search Product
  |
  +--> Add Stock
  |
  +--> Record Sale
  |
  +--> Delete Product
  |
  v
SQLite Database
  |
  +--> Products Table
  |
  +--> Sales Table
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

## Resume Description

**E-Commerce Product & Inventory Management System | Python, Tkinter, SQLite**

Developed a desktop-based inventory management application using Python and Tkinter with SQLite for persistent data storage. Implemented product management, search, stock updates, sales recording, automatic stock reduction, and input validation. Used SQL queries and CRUD operations to manage product and sales data.

**Technologies:** Python, Tkinter, SQLite, SQL

## Interview Explanation

"I developed an E-Commerce Product and Inventory Management System using Python, Tkinter, and SQLite. The GUI allows users to add products with their category, price, and stock quantity. Products are stored in an SQLite database and displayed in a table. Users can search products, add stock, and record sales. When a sale is recorded, the application checks whether enough stock is available and automatically reduces the stock quantity. I used SQL queries for inserting, searching, updating, and deleting records."

## Important Concepts Demonstrated

- Python functions
- GUI programming
- SQLite database
- SQL queries
- CRUD operations
- Input validation
- Event-driven programming
- Basic database design

## Possible Future Improvements

- Shopping cart
- Customer management
- Login system
- Sales dashboard
- Monthly sales reports
- Export reports to CSV
