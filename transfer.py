from Bank import Bank

class Transfer(Bank):

    def __init__(self, id, ammount, date, typePayment, bankName, identification, numberAccount):
        super().__init__(id, ammount, date, typePayment, bankName, identification, numberAccount)