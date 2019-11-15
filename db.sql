CREATE DATABASE scraperdb;
USE scraperdb;
ALTER DATABASE scraperdb CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;
CREATE TABLE listings (id BIGINT(7) NOT NULL AUTO_INCREMENT,
agency VARCHAR(100), region VARCHAR(100), position VARCHAR(100), plantilla VARCHAR(100), postingDate VARCHAR(100), closingDate VARCHAR(100),PRIMARY KEY(id));
ALTER TABLE listings CONVERT TO CHARACTER SET utf8mb4 COLLATE
utf8mb4_unicode_ci;
