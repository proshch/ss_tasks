CREATE TABLE `Results` (
    `result_id` int(10) unsigned NOT NULL auto_increment,
    `task_id` int unsigned NOT NULL,
    `result` text,
    `client` varchar(100),
    PRIMARY KEY (`result_id`),
    FOREIGN KEY (`task_id`) REFERENCES `Tasks`(`task_id`)
);

