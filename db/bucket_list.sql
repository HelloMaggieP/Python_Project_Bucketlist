DROP TABLE cities; 
DROP TABLE countries; 

CREATE TABLE countries (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE cities (
    id SERIAL PRIMARY KEY,
    name VARCHAR (255),
    film_location: VARCHAR(255),
    country_id INT REFERENCES countries(id) ON DELETE CASCADE,
);