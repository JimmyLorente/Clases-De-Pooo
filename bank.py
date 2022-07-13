
from payment import Payment


class   bank(Payment):
    bank                : str

def __init__(self,id,banco,monto,numero_cuenta):
    self.id                 = id
    self.monto              = monto
    self.banco              = banco
    self.numero_cuenta      = numero_cuenta

print (bank.numero_cuenta,bank.id)