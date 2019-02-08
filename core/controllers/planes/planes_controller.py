from utils.db_service import MySQLConnector

class PlanesController(object):

    def __init__(self):
        MySQLConnector().connect()
        self.cursor = MySQLConnector.INSTANCE.get_cursor()

    def create(self, manufacturer, model, econom_seats_num, biz_seats_num, vip_seats_num):
        MySQLConnector.INSTANCE.execute_query('use __aircompany;')

        MySQLConnector.INSTANCE.execute_query('INSERT INTO planes(manufacturer, model, econom_seats_num, biz_seats_num, '
                                     'vip_seats_num) VALUES ({0},{1},{2},{3},{4});'
                                     .format(manufacturer, model, econom_seats_num, biz_seats_num, vip_seats_num))

    def select(self):
        MySQLConnector.INSTANCE.execute_query("SELECT * FROM planes;")
        return MySQLConnector.INSTANCE.get_results()

    # def update(self):
    #     MySQLConnector.INSTANCE.execute_query("UPDATE planes SET

    def delete(self):
        pass