from .user import (RootUser, AdminUser, RegularUser)


user_types = {
    'root': RootUser(),
    'admin': AdminUser(),
    'regular': RegularUser()
}


class UserFactory(object):
    """
    Includes a various of types of creation user for controller usage
    """
    @classmethod
    def create_user_by_name(cls, name):
        """
        :param name: name from user info from db 
        :return: new instance of corresponding user
        """

    @classmethod
    def create_user_by_id(cls, m_id):
        """
        For api use only
        :param m_id: id of user
        :return: new instance of corresponding user
        """

    @classmethod
    def create_users(cls):
        """
        :return: all of users from db 
        """
