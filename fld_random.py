import random

for x in range(10):
    r1 = random.randint(100, 999)
    print(f'{r1}', end=' ')

print('\n-------------------')
for x in range(10):
    r2 = random.randint(0, 250) / 10
    print(f'{r2}', end=' ')

print('\n-------------------')
for x in range(10):
    r3 = random.randint(0, 100) / 10 + 15
    print(f'{r3}', end=' ')

print('\n-------------------')
for x in range(10):
    r4 = random.randint(0, 49) * 2
    print(f'{r4}', end=' ')

print('\n-------------------')
for x in range(10):
    r5 = random.randint(20, 40) * 5
    print(f'{r5}', end=' ')