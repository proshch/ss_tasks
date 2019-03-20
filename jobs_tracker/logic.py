"""Module for implementing class Solve with jobs logic"""


import os
import random
import MySQLdb


class Solve:
    """Class Solve to describe logic of jobs"""
    @staticmethod
    def count_unique_words(config):
        """Count all unique words in file"""

        count = {}
        words = []
        separators = [',', '.', '!', '?', ':', ';', ' ']
        with open(config['path'], 'r') as text_file:
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

        os.mkdir(config['path'])
        result = f"{config['path']} is created"
        return result

    @staticmethod
    def remove_dir(config):
        """Remove directory job_dir"""

        os.rmdir(config['path'])
        result = f"Directory {config['path']} was deleted!"
        return result

    @staticmethod
    def dump_command(config):
        """Dump result of shell command"""

        result = os.popen(config["command"]).read()
        return result

    @staticmethod
    def generate_random_job(config):
        """Generate random job with shell commands"""

        key = random.choice(list(commands))
        db_tasks = MySQLdb.connect("localhost", "oleksandr", "K@tchi1899", "jobs_tracker")
        cursor = db_tasks.cursor()
        sql = """INSERT INTO Tasks(task_title, description, new, in_progress, done)
                 VALUES (%s, %s, %s, %s, %s)"""
        cursor.execute(sql, (commands[key]['title'],
                             commands[key]['description'],
                             commands[key]['new'],
                             commands[key]['in_progress'],
                             commands[key]['done'])
        )

        db_tasks.commit()
        db_tasks.close()

        result = f"{commands[key]} command task is created"
        return result
