from utils.context import Context, Parameter
from utils.db_service import MySQLConnector


class PlanesController(object):
    """
    'planes controller' for controlling 'planes' table from aircompany database
    """

    def __init__(self):
        """
        initialize new 'planes controller'
        """
        MySQLConnector().connect()
        self.cursor = MySQLConnector.INSTANCE.get_cursor()

    @staticmethod
    def create(plane):
        """
        create new row in 'planes' table
        """
        query = "INSERT INTO planes(manufacturer, model, econom_seats_num, biz_seats_num, vip_seats_num) " \
                "VALUES (\"\'{0}\'\",\"\'{1}\'\",\"{2}\",\"{3}\",\"{4}\");".format(
            plane.manufacturer, plane.model, plane.econom_seats_num, plane.business_seats_num,
            plane.vip_seats_num)
        print(query)
        MySQLConnector.INSTANCE.execute_query('use {0};'.format(Context.get(Parameter.DB_NAME)))
        MySQLConnector.INSTANCE.execute_query(query)

    def read(self):
        """
        select info from 'planes' table
        :return: selected info
        """
        MySQLConnector.INSTANCE.execute_query("SELECT * FROM planes;")
        return MySQLConnector.INSTANCE.get_results()

    def update(self, model, econom_seats_num, biz_seats_num, vip_seats_num, id):
        """
        update 'planes' table with info:
        :param model:
        :param econom_seats_num:
        :param biz_seats_num:
        :param vip_seats_num:
        :param id:
        :return:
        """
        MySQLConnector.INSTANCE.execute_query("UPDATE planes SET model = {0}, econom_seats_num = {1}, "
                                              "biz_seats_num = {2}, vip_seats_num = {3} WHERE id = {4};".format(
            model, econom_seats_num, biz_seats_num, vip_seats_num, id))

    def delete(self, id):
        """
        delete info from 'planes' table, info:
        :param id: plane identificator
        :return: mysql database responce
        """
        MySQLConnector.INSTANCE.execute_query("DELETE FROM planes WHERE id = {0}".format(id))
