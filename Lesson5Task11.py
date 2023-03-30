# Task 11
# Написати код для дзеркального перевороту списку [7,2,9,4] -> [4,9,2,7].
# Список може бути довільною довжиною.

import random
a=[]
for i in range(1, 20):
    x = random.randint(0, 10)
    a.append(x)
print(a)
print(a[::-1])
