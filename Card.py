from Bank import Bank

class Card(Bank):
    cardNumber          = int
    cardSecurityCode    = int
    cardDate            = int

    def __init__(self, id, ammount, date, typePayment, bankName, identification, numberAccount, cardNumber, cardSecurityCode, cardDate):
        super().__init__(id, ammount, date, typePayment, bankName, identification, numberAccount)
        self.cardNumber         = cardNumber
        self.cardSecurityCode   = cardSecurityCode
        self.cardDate           = cardDate
