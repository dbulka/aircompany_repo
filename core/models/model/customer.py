from user import User


class Customer(User):
    """
    create guest user
    """

    def __init__(self, id):
        """
        initialize new Customer user
        :param id: customer indeficator
        """
        self.id = id

    def book_ticket(self):
        """
        book ticket
        :return: booked ticket id
        """

    def buy_ticket(self):
        """
        buy ticket
        :return: ticket id
        """

