import random

def random_number():
    number = random.randrange(1, 50)
    
lottery = [] 
    
no1 = random_number()

lottery.insert(1, no1)

no2 = random_number()

lottery.append(no2)

no3 = random_number()

lottery.append(no3)

no4 = random_number()

lottery.append(no4)

no5 = random_number()

lottery.append(no5)

for x in lottery:
    print(x)
