
import mysql.connector

def connect_to_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="lab_database"
    )

def create_table():
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            price DECIMAL(10, 2) NOT NULL,
            description TEXT
        )
    """)
    conn.close()

def create_product(name, price, description):
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO products (name, price, description)
        VALUES (%s, %s, %s)
    """, (name, price, description))
    conn.commit()
    conn.close()

def read_products():
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    for row in cursor.fetchall():
        print(row)
    conn.close()

def update_product(product_id, name, price, description):
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE products
        SET name = %s, price = %s, description = %s
        WHERE id = %s
    """, (name, price, description, product_id))
    conn.commit()
    conn.close()

def delete_product(product_id):
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM products WHERE id = %s", (product_id,))
    conn.commit()
    conn.close()

def main():
    create_table()
    while True:
        print("Choose an action:")
        print("1. Create product")
        print("2. Read products")
        print("3. Update product")
        print("4. Delete product")
        print("5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            name = input("Enter name: ")
            price = float(input("Enter price: "))
            description = input("Enter description: ")
            create_product(name, price, description)
        elif choice == "2":
            read_products()
        elif choice == "3":
            product_id = int(input("Enter product ID: "))
            name = input("Enter new name: ")
            price = float(input("Enter new price: "))
            description = input("Enter new description: ")
            update_product(product_id, name, price, description)
        elif choice == "4":
            product_id = int(input("Enter product ID to delete: "))
            delete_product(product_id)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
