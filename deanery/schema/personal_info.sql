CREATE TABLE Personal_info (
    `personal_info_id` int(10) unsigned NOT NULL auto_increment,
    `first_name` varchar(50) NOT NULL,
    `last_name` varchar(50) NOT NULL,
    `age` int(3) unsigned,
    `country` varchar(100),
    `city` varchar(40),
    `address` varchar(100),
    `phone` varchar(12),
    PRIMARY KEY (`personal_info_id`)
);
