# Task 10
# Є матриця
# [1, 2, 3, 4]
# [5, 6, 7, 8]
# [9, 10, 11, 12]
# [13, 14, 15, 16]
# Напишіть скрипт, який виведе цю матрицю на екран, обчислить та виведе суму елементів цієї матриці.

from random import random
N = 4
matrix = []
for i in range(N):
    row = []
    for j in range(N):
        row.append(int(random()*10))
    matrix.append(row)
for row in matrix:
    print(row)
sumMain = 0
sumSecondary = 0
for i in range(N):
    sumMain += matrix[i][i]
    sumSecondary += matrix[i][N-i-1]
print(sumMain)
print(sumSecondary)