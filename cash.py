from Payment import Payment

class Cash(Payment):

    def __init__(self, id, ammount, date, typePayment):
        super().__init__(id, ammount, date, typePayment)