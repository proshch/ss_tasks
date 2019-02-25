CREATE TABLE `Students` (
    `student_id` int(10) unsigned NOT NULL auto_increment,
    `groupID` int unsigned NOT NULL,
    `personal_info_id` int unsigned NOT NULL, 
    PRIMARY KEY (`student_id`),
    FOREIGN KEY(`groupID`) REFERENCES `Groups`(`groupID`),
    FOREIGN KEY(`personal_info_id`) REFERENCES `Personal_info`(`personal_info_id`)
);

