from utils.db_service import MySQLConnector

class TicketTypesController(object):
    """
    'ticket types controller' for controlling 'ticket types' table from aircompany database
    """

    def __init__(self):
        """
        initialize mew 'ticket_types controller'
        """
        MySQLConnector().connect()
        self.cursor = MySQLConnector.INSTANCE.get_cursor()

    def create(self, title):
        """
        create new row in 'ticket_types' table with info:
        :param title: ticket types title
        :return: responce from mysql databases
        """

        MySQLConnector.INSTANCE.execute_query('use aircompany;')
        MySQLConnector.INSTANCE.execute_query('INSERT INTO ticket_types(title) value ({0});'.format(title))

    def read(self):
        """
        select info from 'ticket_types' table
        :return: selected info
        """
        MySQLConnector.INSTANCE.execute_query('SELECT * FROM ticket_types;')
        return MySQLConnector.INSTANCE.get_results()

    def update(self, title, id):
        """
        update 'ticket_types' table with info
        """
        MySQLConnector.INSTANCE.execute_query(
            'UPDATE ticket_types SET title = {0} WHERE id = {1};'.format(title, id))

    def delete(self, id):
        """
        delete info from 'ticket_types' table, info:

        :return: mysql database responce
        """
        MySQLConnector.INSTANCE.execute_query('DELETE FROM ticket_types WHERE id = {0}'.format(id))