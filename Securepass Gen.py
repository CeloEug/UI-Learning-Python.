import random

##funcion to generate 32 random numbers and convert it to its respective ASCII characters. 
def securePass():
    rawpass = []
    for _ in range(32):
        rawpass.append(chr(random.randint(33, 126)))
    return "".join(rawpass)

print(securePass())