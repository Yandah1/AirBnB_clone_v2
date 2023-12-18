-- this script prepares a MySQL server for the project
-- create project testing database with the name : hbnb_test_db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- creating new user named : hbnb_test with all privileges on the db hbnb_test_db
-- with the password : hbnb_test_pwd if it dosen't exist, the user is created for connectios from the localhost host
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- granting the SELECT privilege for the user hbnb_test on the db performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
-- reloads the grant tables and applies the privilege changes immediately
FLUSH PRIVILEGES;
-- granting all privileges to the new user on hbnb_test_db
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
