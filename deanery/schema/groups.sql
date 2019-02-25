CREATE TABLE `Groups` (
    `groupID` int(10) unsigned NOT NULL auto_increment,
    `department_id` int unsigned NOT NULL,
    `group_title` varchar(100) NOT NULL,
    PRIMARY KEY (`groupID`),
    FOREIGN KEY(`department_id`) REFERENCES `Departments`(`department_id`)
);

