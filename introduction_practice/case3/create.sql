DROP DATABASE IF EXISTS TourismDB;
CREATE DATABASE TourismDB;
USE TourismDB;

CREATE TABLE Туры (
    tour_id INT AUTO_INCREMENT PRIMARY KEY,
    tour_name VARCHAR(255) NOT NULL,
    tour_description TEXT,
    duration INT,
    price DECIMAL(10, 2)
);

CREATE TABLE Услуги (
    service_id INT AUTO_INCREMENT PRIMARY KEY,
    service_name VARCHAR(255) NOT NULL,
    service_description TEXT,
    price DECIMAL(10, 2)
);

CREATE TABLE Клиенты (
    client_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    phone_number VARCHAR(20)
);

CREATE TABLE Туроператоры (
    operator_id INT AUTO_INCREMENT PRIMARY KEY,
    operator_name VARCHAR(255) NOT NULL,
    contact_info VARCHAR(255)
);

CREATE TABLE Заказы (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    client_id INT,
    tour_id INT,
    operator_id INT,
    order_date DATE,
    total_price DECIMAL(10, 2),
    FOREIGN KEY (client_id) REFERENCES Клиенты(client_id),
    FOREIGN KEY (tour_id) REFERENCES Туры(tour_id),
    FOREIGN KEY (operator_id) REFERENCES Туроператоры(operator_id)
);
