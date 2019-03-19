INSERT INTO `Tasks`
    (`task_id`, `task_title`, `description`, `new`, `in_progress`, `done`, `client`)
VALUES
    (1, 'Count unique words', 'Count all unique words in file', true, false, false, NULL),
    (2, 'Make folder', 'Make folder ~/home/user/new_folder', true, false, false, NULL),
    (3, 'Delete folder', 'Delete folder ~/home/user/new_folder', true, false, false, NULL),
    (4, 'Dump specific info', 'Dump info about result of shell command ps', true, false, false, NULL);

