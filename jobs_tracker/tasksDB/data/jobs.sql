INSERT INTO `Jobs`
    (`job_type`, `status`, `ctime`, `config`)
VALUES
    (1, 'new', now(), '{"path": "/home/oleksandr/jobs_tracker/working_dir/text.txt"}'),
    (2, 'new', now(), '{"path": "/home/oleksandr/jobs_tracker/working_dir/test_dir"}'),
    (3, 'new', now(), '{"path": "/home/oleksandr/jobs_tracker/working_dir/test_dir"}'),
    (4, 'new', now(), '{"command": "time"}'),
    (5, 'new', now(), '{"count": 3}');
