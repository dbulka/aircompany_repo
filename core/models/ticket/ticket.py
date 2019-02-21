class Ticket:
    """
    create ticket class
    """

    def __init__(self, user, price, luggage):
        """
        initialize new ticket
        :param args: input parametrs
        :param kwargs: inputs data
        """
        self.luggage = luggage
        self.user = user
        self.price = price

    @property
    def final_price(self):
        return self.price + self.luggage.price

    def apply_direction(self, *args, **kwargs):
        """apply flight's direction
        :param args: input parametrs
        :param kwargs: inputs data
        """

    def choose_class(self, *args, **kwargs):
        """
        choose flight class
        :param args: input parametrs
        :param kwargs: inputs data
        :return: choosen flight class
        """

    def change_luggage(self, *args, **kwargs):
        """
        choose luggage class
        :param args: input parametrs
        :param kwargs: inputs data
        :return: choosen luggage class
        """


class EconomTicket(Ticket):
    pass


class BusinessTicket(Ticket):
    pass


class VIPTicket(Ticket):
    pass
