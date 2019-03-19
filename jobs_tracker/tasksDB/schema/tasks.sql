CREATE TABLE `Tasks` (
    `task_id` int(10) unsigned NOT NULL auto_increment,
    `task_title` varchar(100),
    `description` text,
    `new` boolean,
    `in_progress` boolean,
    `done` boolean,
    `client` varchar(100),
    PRIMARY KEY (`task_id`)
);

