CREATE TABLE `Jobs` (
    `job_id` int(10) unsigned NOT NULL auto_increment,
    `job_type` int(10),
    `status` varchar(100),
    `result` text,
    `ctime` datetime,
    `mtime` datetime,
    `config` text,
    PRIMARY KEY (`job_id`)
);

