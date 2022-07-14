from Account import Account

class Driver(Account):
    idDriver    = int
    license     = str

    def __init__(self, name, document, mail, password, gender, numberCell, age, idDriver, license):
        super().__init__(name, document, mail, password, gender, numberCell, age)

        self.idDriver   = idDriver
        self.license    = license