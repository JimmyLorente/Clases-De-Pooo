import imp
from socket import INADDR_UNSPEC_GROUP
from Account import Account

class User(Account):
    idUser  = int

    def __init__(self, name, document, mail, password, gender, numberCell, age):
        super().__init__(name, document, mail, password, gender, numberCell, age)

        self.idUser     = id 