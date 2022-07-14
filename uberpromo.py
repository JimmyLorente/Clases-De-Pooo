from pyexpat import model
from Car import Car

class UberPromo(Car):
    brand       = str
    model       = str

    def __init__(self, license, driver, passanger, id, brand, model):
        super().__init__(license, driver, passanger, id)
        self.brand      = brand
        self.model      = model