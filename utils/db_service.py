class DBConnector(object):
    """ An interface for a various DBMS connector methods """

    def get_connection(self, *args, **kwargs):
        """ Retrieves an db connection """

    def get_cursor(self):
        """ Returns an cursor object which able to execute queries """

    def execute_query(self, *args, **kwargs):
        """ Executes an query for connected db """

    def get_results(self):
        """ Fetches query result(s) """

    def shutdown(self):
        """ Clases cursor and connections """


class MySQLConnector(DBConnector):
    """
    MySQL's implementation of common DB connector methods 
    """

    INSTANCE = None

    def __new__(cls):
        if not cls.INSTANCE:
            cls.INSTANCE = object.__new__(cls)
        return cls.INSTANCE
