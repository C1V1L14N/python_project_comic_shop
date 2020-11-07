DROP TABLE IF EXISTS publishers
DROP TABLE IF EXISTS comics

CREATE TABLE comics(
    name VARCHAR(255),
    author VARCHAR(255),
    genre VARCHAR(255),
    wholesale_price INT,
    markup INT,
    stock_count INT,
    min_count INT,
    out_of_stock BOOLEAN,
    pulisher_id INT REFERENCES publishers(id)
);

CREATE TABLE publishers(
    id SERIAL PRIMARY KEY
    name VARCHAR(255)
);