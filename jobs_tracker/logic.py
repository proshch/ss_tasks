import os


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
