from core.controllers.users.users_controller import UsersController

user_control = UsersController()
# user_control.create("gmail", "123123", "Vasya", "2223344", "Dom 12", "Ivanov", "Minsk", "region", "22004", "BLR", 3)
user_control.update("xxx@ya.ru", "1233223",1)
user_control.delete(2)
user_control.read()