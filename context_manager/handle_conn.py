"""Module for implementing context manager (as a class) for handling
DB Pool connections."""

import MySQLdb


class DBConn:
    """Context manager for handling
    DB Pool connections"""

    def __init__(self, host, username, password, database):
        """Parameters:
            host (str) - host name
            username (str) - user login
            password (str) - user password
            database (str) - database name
        """

        self.host = host
        self.username = username
        self.password = password
        self.database = database

    def __enter__(self):
        """Connect database"""

        self.db = MySQLdb.connect(self.host,
                                  self.username,
                                  self.password,
                                  self.database)

        return self.db

    def __exit__(self, exc_type, exc_value, traceback):
        """Close connection with database"""

        self.db.close()

with DBConn('localhost', 'oleksandr', 'K@tchi1899', 'jobs_tracker') as db:
    cursor = db.cursor()

    # execute SQL query using execute() method.
    cursor.execute("SELECT VERSION()")

    # Fetch a single row using fetchone() method.
    data = cursor.fetchone()
    print("Database version : %s " % data)

