use startersql;

INSERT INTO addresses (user_id, street, city, state, pincode)
VALUES
  (1, '123 Oak Street', 'Springfield', 'IL', '62704'),
  (2, '45 Pine Avenue', 'Austin', 'TX', '73301'),
  (3, '800 Market Street', 'San Francisco', 'CA', '94103'),
  (4, '27 Maple Road', 'Portland', 'OR', '97201');

SELECT * FROM addresses;