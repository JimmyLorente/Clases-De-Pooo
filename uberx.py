

from io import BufferedRandom
from lib2to3.pgen2 import driver
from pyexpat import model
from turtle import st
from car import Car

class uber(Car):
    uber       : str

    def __init__(self,driver,passager,brand,model,id):
        self.id         = id
        self.driver     = driver
        self.passager   = passager
        self.brand      = brand
        self.model      = model

print (Car.brand,Car.id)