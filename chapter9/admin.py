from privalage import Privelage
from user import Users

class Admin(Users):
    def __init__(self, first, last, username, password, dob, privelage):
        super().__init__(first, last, username, password, dob)
        self.privelage = Privelage(privelage)

