from random import choice
from string import ascii_uppercase, ascii_lowercase
import os
def generateToken() -> str:
    s = ascii_uppercase + ascii_lowercase + '0123456789'
    return ''.join(choice(s) for i in range(50))

def getFiles():
    for name_file in os.listdir('../files/'):
        print(name_file)

def getNames():
    f = open('configs/names.txt')
    l = []
    for x in f:
        x = x.split()
        c = StatioInfo(int(x[0]), x[1], float(x[2]), float(x[3]))
        l.append(c)
    return l


class StatioInfo:

    def __init__(self, number, name, lat, long):
        self.number = number
        self.name = name
        self.lat = lat
        self.long = lat

    def __repr__(self):
        return '{}  {}  {}  {}'.format(self.number, self.name, self.lat, self.long)

    def json(self):
        return {'number': self.number, 'name': self.name,
                'lat': self.lat, 'long': self.long,}

print(getNames())