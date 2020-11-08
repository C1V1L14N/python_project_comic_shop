DROP TABLE IF EXISTS comics;
DROP TABLE IF EXISTS publishers;

CREATE TABLE publishers(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE comics(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    author VARCHAR(255),
    genre VARCHAR(255),
    wholesale_price INT,
    markup INT,
    stock_count INT,
    min_count INT,
    out_of_stock BOOLEAN,
    publisher_id INT REFERENCES publishers(id)
);

