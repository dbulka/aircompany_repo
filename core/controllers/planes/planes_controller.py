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

    def create(self, manufacturer, model, econom_seats_num, biz_seats_num, vip_seats_num):
        """
        create new row in 'plane' table with info:
        :param manufacturer: manufacturer's name
        :param model: model's type
        :param econom_seats_num: number of econom seats
        :param biz_seats_num: number of biz. seats
        :param vip_seats_num: number of vip seats
        :return: responce of mysql databases
        """
        MySQLConnector.INSTANCE.execute_query('use aircompany;')
        MySQLConnector.INSTANCE.execute_query('INSERT INTO planes(manufacturer, model, econom_seats_num, biz_seats_num, '
                                              'vip_seats_num) VALUES ({0},{1},{2},{3},{4});'
                                              .format(manufacturer, model, econom_seats_num, biz_seats_num, vip_seats_num))

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

    #     1. окно выбора параметров для изменения: через for/in root выбирает какие параметры хочет изменить
    #     2. окно выбора параметра-условия измения: через через for/in root задаёт параметр-условие
    #     3. задаём значения для параметров п1. п2.

    def delete(self, id):
        """
        delete info from 'planes' table, info:
        :param id: plane identificator
        :return: mysql database responce
        """
        MySQLConnector.INSTANCE.execute_query("DELETE FROM planes WHERE id = {0}".format(id))