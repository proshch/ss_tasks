import os
import random
import MySQLdb

class Solve:
    """Class Solve to describe logic of jobs"""
    @staticmethod
    def count_unique_words():
        """Count all unique words in file

        Positional argument:
        file_name -- name of file
        """
        count = {}
        words = []
        separators = [',', '.', '!', '?', ':', ';', ' ']
        with open('count_words.txt', 'r') as text_file:
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
    def make_dir():
        """Make directory for path
        Positional argument:
        path -- path to dir what you want to create
        """
        os.mkdir('job_dir')
        result = 'job_dir is created'
        return result

    @staticmethod
    def remove_dir():
        """Remove directory for path
        Positional argument:
        path -- path to dir what you want to delete
        """
        os.rmdir('job_dir')
        result = 'Directory job_dir was deleted!'
        return result

    @staticmethod
    def dump_command():
        """Dump result of shell command"""

        result = os.popen('ps').read()
        return result

    @staticmethod
    def generate_random_job():
        """Generate random job"""

        commands = {'ps': {'title': 'Dump ps shell command',
                           'description': 'Report a snapshot of the current processes.',
                           'new': 1,
                           'in_progress': 0,
                           'done': 0,
                          },
                    'ls': {'title': 'Dump ls shell command',
                           'description': 'Lists directory contents of files and directories..',
                           'new': 1,
                           'in_progress': 0,
                           'done': 0,
                          },
                    'date': {'title': 'Dump date shell command',
                           'description': 'Show current date',
                           'new': 1,
                           'in_progress': 0,
                           'done': 0,
                          },
                    'time': {'title': 'Dump time shell command',
                           'description': 'Show current time',
                           'new': 1,
                           'in_progress': 0,
                           'done': 0,
                          },
                    'pwd': {'title': 'Dump pwd shell command',
                           'description': 'Print the current working directory',
                           'new': 1,
                           'in_progress': 0,
                           'done': 0,
                          }
                    }
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
