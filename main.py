from pprint import pprint
from car import Car


if __name__ == "__main__":
    print ( "hola mundo" )

    carro = Car()
    carro.id          = 5
    carro.brand       = "Toyota"
    carro.driver      = "Fer"
    carro.passager    = 5

print (vars(carro))