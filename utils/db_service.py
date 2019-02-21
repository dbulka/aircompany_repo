import logging

import mysql.connector
from mysql.connector import Error

from utils import Context, Parameter


class DBConnector(object):
    """ An interface for a various DBMS connector methods """

    def connect(self, *args, **kwargs):
        """ Retrieves an db connection """

    def get_cursor(self):
        """ Returns an cursor object which able to execute queries """

    def execute_query(self, *args, **kwargs):
        """ Executes an query for connected db """

    def shutdown(self):
        """ Clases cursor and connections """


class MySQLConnector(DBConnector):
    """
    MySQL's implementation of common DB connector methods 
    """

    INSTANCE = None

    connection = None
    cursor = None

    def __new__(cls):
        """
        A singleton implementation for mysql connector
        :return: MySQLConnector instance
        """
        if not cls.INSTANCE:
            cls.INSTANCE = super().__new__(cls)
        return cls.INSTANCE

    def connect(self):
        """
        Retrieves connection params from config, creates mysql db connection
        """
        try:
            # auth_plugin is needed for mysql8+
            self.connection = mysql.connector.connect(host=Context.get(Parameter.DB_HOST),
                                                      database=Context.get(Parameter.DB_NAME),
                                                      user=Context.get(Parameter.DB_USERNAME),
                                                      password=Context.get(Parameter.DB_PASSWORD),
                                                      auth_plugin='mysql_native_password')
            self.connection.autocommit = True
            if self.connection.is_connected():
                db_Info = self.connection.get_server_info()
                logging.getLogger(__name__).debug("Connected to MySQL database... MySQL Server version on %s" % db_Info)
        except Error as e:
            logging.getLogger(__name__).error("Error while connecting to MySQL %s" % e)
            return

    def get_cursor(self):
        """
        Retrieves an cursor object for DB-API interaction
        :return: cursor object or none if we got exception
        """
        try:
            self.cursor = self.connection.cursor()
            logging.getLogger(__name__).debug("Cursor was created.")
        except Error as e:
            logging.getLogger(__name__).error("Something went wrong with cursor creating. %s" % e)
        finally:
            return self.cursor

    def execute_query(self, query):
        """
        :param query: str object like sql query
        :return: results of query as typle or none if we got exception
        """
        try:
            self.cursor.execute(query)
            logging.getLogger(__name__).debug("Query was execute.")
        except Error as e:
            logging.getLogger(__name__).error("Error while executing query. %s" % e)

    def get_results(self):
        return self.cursor.fetchall()

    def shutdown(self):
        """
        Closes the connection
        """
        try:
            if self.connection.is_connected():
                self.cursor.close()
                self.connection.close()
                logging.getLogger(__name__).debug("Connection was succesfully closed.")
            logging.getLogger(__name__).debug("Already closed")
        except Error as e:
            logging.getLogger(__name__).error("Error while closing channel %s" % e)
