from Car import Car
from Driver import Driver
from Payment import Payment
from Rute import Rute
from User import User

class Trip(Car, User, Driver, Rute, Payment):
        idTrip      = int

        def __init__(self, license, driver, passanger, id):
                super().__init__(license, driver, passanger, id)