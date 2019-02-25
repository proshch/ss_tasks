CREATE TABLE `Marks` (
    `mark_id` int(10) unsigned NOT NULL auto_increment,
    `student_id` int unsigned NOT NULL,
    `subject_id` int unsigned NOT NULL,
    `mark` int,
    PRIMARY KEY (`mark_id`),
    FOREIGN KEY(`student_id`) REFERENCES `Students`(`student_id`),
    FOREIGN KEY(`subject_id`) REFERENCES `Subjects`(`subject_id`)
 );

