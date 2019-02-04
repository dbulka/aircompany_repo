import configparser
from os import getcwd
from enum import Enum

CONFIG_FILE_PATH = getcwd() + '/aircompany.ini'


class Context:
    """
    Cotains parser methods of config from a different number of sections of CONFIG_FILE_PATH
    """
    config = configparser.ConfigParser().read(CONFIG_FILE_PATH)

    @classmethod
    def get_db_parameter(cls, parameter):
        """
        Takes params from [db] section of ini file
        :param parameter: 
        :return: value from a parameter as str
        """

        return cls.config.get('db', parameter.value)


class Parameter(Enum):
    DB_USERNAME = 'dbuser'
    DB_PASSWORD = 'dbpassword'
    DB_HOST = 'dbhost'
    DB_PORT = 'dbport'
