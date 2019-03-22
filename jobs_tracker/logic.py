"""Module for implementing class Solve with jobs logic"""


import random
import MySQLdb
import subprocess


class Solve:
    """Class Solve to describe logic of jobs"""
    @staticmethod
    def count_unique_words(config):
        """Count all unique words in file"""

        count = {}
        words = []
        separators = [',', '.', '!', '?', ':', ';', ' ']
        with open(config, 'r') as text_file:
            for line in text_file:
                for s in separators:
                    words = line.split(s)
                for word in words:
                    if word in count:
                        count[word] += 1
                    else:
                        count[word] = 1
        return count

    @staticmethod
    def make_dir(config):
        """Make directory job_dir"""
        proc = subprocess.run('mkdir {}'.format(config), shell=True)
        if proc.returncode == 0:
            result = f'Dir {config} was created'
        else:
            result = None
        return result


    @staticmethod
    def remove_dir(config):
        """Remove directory job_dir"""
        proc = subprocess.run('rm -r {}'.format(config), shell=True)
        if proc.returncode == 0:
            result = f'Dir {config} was deleted'
        else:
            result = None
        return result

    @staticmethod
    def dump_command(config):
        """Dump result of shell command"""

        proc = subprocess.Popen(config, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        result = proc.communicate()
        return result

    @staticmethod
    def generate_random_job(config):
        """Generate random job with shell commands"""

        db_jobs = MySQLdb.connect("localhost", "username", "password", "jobs_tracker")
        cursor = db_jobs.cursor()

        file_path = [
            "/home/oleksandr/jobs_tracker/working_dir/test3.txt",
            "/home/oleksandr/jobs_tracker/working_dir/text2.txt",
            "/home/oleksandr/jobs_tracker/working_dir/text1.txt"]
        dir_path = [
            "/home/oleksandr/jobs_tracker/working_dir/new_dir1",
            "/home/oleksandr/jobs_tracker/working_dir/new_dir2",
            "/home/oleksandr/jobs_tracker/working_dir/new_dir3"]

        command = random.choice(['whoami', 'date', 'pwd'])
        for i in range(config):
            task_type = random.randint(1, 5)
            if task_type == 1:
                conf = '{"path": "%s"}' % random.choice(file_path)
            elif task_type == 2:
                conf = '{"path": "%s"}' % random.choice(dir_path)
            elif task_type == 3:
                conf = '{"path": "%s"}' % random.choice(dir_path)
            elif task_type == 4:
                conf = '{"command": "%s"}' % command
            elif task_type == 5:
                conf = '{"count": %d}' % random.randint(1, 5)

            sql = """INSERT INTO Jobs(job_type, status, ctime, config)
                    VALUES (%s, 'new', now(), %s)"""

            cursor.execute(sql, (task_type, conf))
            db_jobs.commit()
        result = f"{config} tasks was created"

        db_jobs.close()

        return result
