from random import choice
from string import ascii_uppercase, ascii_lowercase
def generateToken() -> str:
    s = ascii_uppercase + ascii_lowercase + '0123456789'
    return ''.join(choice(s) for i in range(50))


for i in range(10):
    print(generateToken())