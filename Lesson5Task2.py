# Task 2
# Напишіть скрипт для визначення суми цілих непарних чисел від 1 до 99
# за допомогою оператора for. Використовуйте цілочисельні змінні sum і count.

# 1 варіант розв'язання без циклу for
# print(sum(range(1, 100, 2)))

# 2 варіант розв'язання без циклу for
# number = list(range(1, 100, 2))
# print(sum(number))


# summa = 0
# for i in range(1, 100, 2):
#    summa += i
# print(summa)

a = range(1, 100, 2)
b = []
for elem in a:
        b.append(elem)
print(sum(b))
