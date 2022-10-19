import random

# [0, 1) közötti véletlen float számot generál:
print(random.random())

# [a, b] közötti egész számot generál (a < b)
print(random.randint(1, 6))

# start, stop, step -> [start, stop) között, step-enként állít elő véletlen számot
print(random.randrange(0, 100, 2))