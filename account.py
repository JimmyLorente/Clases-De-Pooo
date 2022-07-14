import mailbox
from unicodedata import name
from xml.dom.minidom import Document


class Account() :
    id          = int
    name        = str
    document    = str
    mail        = str
    password    = str
    gender      = str
    numberCell  = int
    age         = int

    def __init__(self, name, document, mail, password, gender, numberCell, age):
        self.name       = name
        self.document   = document
        self.mail       = mail
        self.password   = password
        self.gender     = gender
        self.numberCell = numberCell
        self.age        = age
