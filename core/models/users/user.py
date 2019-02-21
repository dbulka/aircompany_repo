class User:
    """
    create users class
    """

    def __init__(self, *args, **kwargs):
        """
        initialize new users
        :param args: input parametrs
        :param kwargs: inputs data
        """

    def check_person_info(self, *args, **kwargs):
        """
        check person info
        :param args: input parametrs
        :param kwargs: inputs data
        """

    def check_in(self, *args, **kwargs):
        """
        check in
        :param args: input parametrs
        :param kwargs: inputs data
        """

    def search_flight(self, *args, **kwargs):
        """
        search of light
        :param args: input parametrs
        :param kwargs: inputs data
        """

    def order_ticket(self, *args, **kwargs):
        """
        order ticket
        :param args: input parametrs
        :param kwargs: inputs data
        """


class RootUser(User):
    pass


class AdminUser(User):
    pass


class RegularUser(User):
    pass
