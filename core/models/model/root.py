from user import User

class Root(User):
    """
    create root user
    """

    def __init__(self, id):
        """
        initialize new root user
        :param id: root's indeficator
        """
        self.id = id