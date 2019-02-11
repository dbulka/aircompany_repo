from utils.db_service import MySQLConnector

class FlightsController(object):
    """
    'flights controller' for controlling 'flights' table from aircompany database
    """

    def __init__(self):
        """
        initialize mew 'flights controller'
        """
        MySQLConnector().connect()
        self.cursor = MySQLConnector.INSTANCE.get_cursor()

    def create(self, id_plane, _from, _to, date_departure, date_arrival):
        """
        create new row in 'flights' table with info:
        :param id_plane: plane's id from 'planes' table
        :param _from: point of departure
        :param _to: point of arrival
        :param date_departure: day of departure
        :param date_arrival: day of arrival
        :return: responce of mysql databases
        """
        MySQLConnector.INSTANCE.execute_query('use __aircompany;')
        MySQLConnector.INSTANCE.execute_query('INSERT INTO flights(id_plane, _from, _to, date_departure, date_arrival) '
                                              'VALUES ({0}, {1}, {2}, {3}, {4});'
                                              .format(id_plane, _from, _to, date_departure, date_arrival))


    def select(self):
        """
        select info from 'flights' table
        :return: selected info
        """
        MySQLConnector.INSTANCE.execute_query('SELECT * FROM flights;')
        return MySQLConnector.INSTANCE.get_results()

    def update(self, _to, id_plane):
        """
        update 'planes' table with info
        """
        MySQLConnector.INSTANCE.execute_query('UPDATE flights SET _to = {0} WHERE id_plane = {1};'.format(_to, id_plane))

    def delete(self, id):
        """
        delete info from 'flights' table, info:

        :return: mysql database responce
        """
        MySQLConnector.INSTANCE.execute_query('DELETE FROM flights WHERE id = {0}'.format(id))
