DROP TABLE cities; 
DROP TABLE countries; 

CREATE TABLE countries (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE cities (
    id SERIAL PRIMARY KEY,
    name VARCHAR (255),
    film_locations VARCHAR(255),
    visited BOOLEAN,
    country_id INT REFERENCES countries(id) ON DELETE CASCADE
);