CREATE TABLE `Tasks` (
    `task_id` int(10) unsigned NOT NULL auto_increment,
    `task_title` varchar(100),
    `description` text,
    `is_solved` boolean,
    PRIMARY KEY (`task_id`)
);

