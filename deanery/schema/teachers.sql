CREATE TABLE `Teachers` (
    `teacher_id` int(10) unsigned NOT NULL auto_increment,
    `department_id` int unsigned NOT NULL,
    `personal_info_id` int unsigned NOT NULL,     
    `teacher_rank` varchar(50),
    `position` varchar(50),
    PRIMARY KEY (`teacher_id`),
    FOREIGN KEY(`department_id`) REFERENCES `Departments`(`department_id`),
    FOREIGN KEY(`personal_info_id`) REFERENCES `Personal_info`(`personal_info_id`)
);

