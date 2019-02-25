CREATE TABLE `Departments` (
    `department_id` int(10) unsigned NOT NULL auto_increment,
    `faculty_id` int unsigned NOT NULL,
    `department_title` varchar(100) NOT NULL,
    `campus` varchar(20),
    `department_floor` int,
    PRIMARY KEY (`department_id`),
    FOREIGN KEY(`faculty_id`) REFERENCES `Faculties`(`faculty_id`)
);

