CREATE DATABASE idlewardb;
GRANT ALL PRIVILEGES ON DATABASE idlewardb TO idleuser;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    user_name character varying(255) NOT NULL UNIQUE
);
