from pyexpat import model
from re import S
from Car import Car

class UberFlash(Car):
    brand       = str
    model       = str
    loadSize    = []
    loadWeight  = int

    def __init__(self, license, driver, passanger, id, brand, model, loadSize, loadWeight):
        super().__init__(license, driver, passanger, id)

        self.brand      = brand
        self.model      = model
        self.loadSize   = loadSize
        self.loadWeight = loadWeight