CREATE TABLE `Schedule` (
    `schedule_id` int(10) unsigned NOT NULL auto_increment,
    `teacher_id` int unsigned NOT NULL,
    `groupID` int unsigned NOT NULL,
    `subject_id` int unsigned NOT NULL,
    `lesson_date` date,
    `lesson_time` time,
    `campus` varchar(20),
    `audience` varchar(10),
    `is_exam` boolean,
    PRIMARY KEY (`schedule_id`),
    FOREIGN KEY(`teacher_id`) REFERENCES `Teachers`(`teacher_id`),
    FOREIGN KEY(`groupID`) REFERENCES `Groups`(`groupID`),
    FOREIGN KEY(`subject_id`) REFERENCES `Subjects`(`subject_id`)
);

