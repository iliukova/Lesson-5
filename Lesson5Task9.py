# Task 9
# Створіть список із 12 елементів. Кожен елемент цього списку є зарплатою робітника
# за місяць. Виведіть цей список на екран та обчисліть середньомісячну зарплату цього робітника.

A=12
import random
a=[]
for i in range(A):
    x=random.randint(0,10000)
    a.append(x)
print(a)
middle=sum(a)//A
print("Average salary is",middle)