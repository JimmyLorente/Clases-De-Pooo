
from lib2to3.pgen2 import driver
from Account import Account

class Car :
    id          = int
    driver      = Account ("","")
    passanger   = int
    license     = str

    def __init__(self, license, driver, passanger, id):
        self.license    = license
        self.driver     = driver
        self.passanger  = passanger
        self.id         = id