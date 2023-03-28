# Task 12
# За допомогою циклів вивести на екран усі прості числа від 1 до 100.

for n in range (2, 200):
    count = 0
    for k in range(2, n):
        if n % k == 0:
            count += 1
    if count == 0:
        print(n)
