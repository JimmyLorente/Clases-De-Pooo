from Car import Car

class UberConfort(Car):
    numberPassangger        = int
    carAccepted             = []
    seatMaterial            = []

    def __init__(self, license, driver, numberPassanggers, seatMaterial):
        super().__init__(license, driver)
        self.carAccepted        = Car
        self.seatMaterial       = seatMaterial
        self.numberPassangger   = numberPassanggers