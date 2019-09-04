from user_modul_1 import User
from user_priveredes_modul_1 import Privileges
class Admin(User):
    def __init__(self, first_name, last_name, age, profehinal):
        self.privileges = Privileges()
