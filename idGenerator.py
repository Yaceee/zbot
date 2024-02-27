import random
from faker import Faker

mail_adress = ['gmail.com', 'yahoo.fr', 'protonmail.com', 'hotmail.fr', 'orange.fr', 'free.fr', 'laposte.net', 'outlook.com']

def formatArrondissement(arrondissement: str):
    if(len(arrondissement) == 1):
        return '0' + arrondissement
    else:
        return arrondissement

def generateId():
    fake = Faker(locale="fr_FR")

    names = fake.name().split(' ')
    fname = names[0]
    lname = names[1]
    town = 'Paris'
    zipCode = '750' + formatArrondissement(str(random.randint(1,20)))

    number = '+336' + ''.join([str(random.randint(0,9)) for i in range(8)])
    email = fake.ascii_free_email()

    return (fname, lname , town, zipCode, number, email)

if __name__ == "__main__":
    print([generateId() for i in range(10)])