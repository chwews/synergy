USE TourismAppDB;
INSERT INTO tourism_app_tour (tour_name, tour_description, duration, price) VALUES
('Beach Paradise', 'Relax on the beautiful sandy beaches of Maldives.', 7, 1500.00),
('Mountain Adventure', 'Explore the stunning landscapes of the Swiss Alps.', 10, 2000.00),
('City Lights', 'Experience the vibrant culture and nightlife of New York.', 5, 1200.00),
('Historical Journey', 'Discover the ancient wonders of Egypt.', 8, 1800.00),
('Tropical Escape', 'Enjoy the tropical climate and vibrant wildlife of Costa Rica.', 9, 1700.00);

INSERT INTO tourism_app_service (service_name, service_description, price) VALUES
('Airport Transfer', 'Private transfer from the airport to your hotel.', 50.00),
('Guided Tour', "A guided tour of the city\'s main attractions.", 100.00),
('Dinner Cruise', 'A luxurious dinner cruise with stunning views.', 150.00),
('Spa Treatment', 'Relaxing spa treatment at a 5-star facility.', 80.00),
('Adventure Activities', 'Includes activities like zip-lining and white-water rafting.', 200.00);

INSERT INTO tourism_app_client (first_name, last_name, email, phone_number) VALUES
('John', 'Doe', 'john.doe@example.com', '+1234567890'),
('Jane', 'Smith', 'jane.smith@example.com', '+0987654321'),
('Emily', 'Johnson', 'emily.johnson@example.com', '+1122334455'),
('Michael', 'Brown', 'michael.brown@example.com', '+5566778899'),
('Linda', 'Williams', 'linda.williams@example.com', '+6677889900');

INSERT INTO tourism_app_operator (operator_name, contact_info) VALUES
('TravelCo', 'contact@travelco.com'),
('ExploreTours', 'info@exploretours.com'),
('HolidayExperts', 'support@holidayexperts.com'),
('AdventureWorld', 'contact@adventureworld.com'),
('VoyageMasters', 'hello@voyagemasters.com');

INSERT INTO tourism_app_order (client_id, tour_id, operator_id, order_date, total_price) VALUES
(1, 1, 1, '2024-06-15', 1500.00),
(2, 2, 2, '2024-07-20', 2000.00),
(3, 3, 3, '2024-08-05', 1200.00),
(4, 4, 4, '2024-09-12', 1800.00),
(5, 5, 5, '2024-10-25', 1700.00);
