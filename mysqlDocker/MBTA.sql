CREATE DATABASE IF NOT EXISTS MBTAdb;

USE MBTAdb;

DROP TABLE IF EXISTS mbta_buses;

CREATE TABLE mbta_buses (
    record_num INT AUTO_INCREMENT PRIMARY KEY,
    id varchar(255) not null,
    latitude decimal(11,8) not null,
    longitude decimal(11,8) not null,
    trip_id varchar(255) not null,
    updated_at datetime,
    current_stop_sequence INT,
    occupancy_status varchar(255),
    direction_id INT,
    UNIQUE(id,trip_id, latitude, longitude, current_stop_sequence, updated_at)
    
);

