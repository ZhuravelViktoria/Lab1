import random 
rnd = [0, 0, 0] 
rnd[0] = random.randint(0, 100) 
rnd[1] = random.randint(0, 100)
while rnd[1] == rnd[0]:
    
    rnd[1] = random.randint(0, 100)
    rnd[2] = random.randint(0, 100)
while (rnd[2] == rnd[0]) and (rnd[2] == rnd[1]) : 
    rnd[2] = random.randint(0, 100)
for i in rnd: 
    print(i)
