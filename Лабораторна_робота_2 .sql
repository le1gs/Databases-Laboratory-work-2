
CREATE DATABASE Store;
USE Store;

CREATE TABLE categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(255) NOT NULL
);

CREATE TABLE products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(255) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    stock INT NOT NULL,
    category_id INT,
    FOREIGN KEY (category_id) REFERENCES categories(category_id)
);

CREATE TABLE customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    phone VARCHAR(15)
);

CREATE TABLE orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    order_date DATE NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE order_details (
    order_detail_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT,
    product_id INT,
    quantity INT NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

INSERT INTO categories (category_name) VALUES ('Electronics'), ('Books'), ('Clothing');
INSERT INTO products (product_name, price, stock, category_id) 
VALUES 
    ('Smartphone', 699.99, 50, 1),
    ('Laptop', 999.99, 30, 1),
    ('Fiction Book', 19.99, 100, 2),
    ('T-Shirt', 15.99, 200, 3);
INSERT INTO customers (customer_name, email, phone) 
VALUES 
    ('Alice Smith', 'alice@example.com', '1234567890'),
    ('Bob Johnson', 'bob@example.com', '0987654321');
INSERT INTO orders (customer_id, order_date) 
VALUES 
    (1, '2023-12-01'),
    (2, '2023-12-02');
INSERT INTO order_details (order_id, product_id, quantity) 
VALUES 
    (1, 1, 1),
    (1, 3, 2),
    (2, 2, 1),
    (2, 4, 3);
