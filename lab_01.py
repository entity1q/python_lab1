# Завдання 1
# Перший етап: Введення чисел
a = int(input('Введіть ціле число: '))
b = int(input('Введіть ціле число: '))
c = float(input('Введіть дробове число: '))
d = float(input('Введіть дробове число: '))

# Завдання 2
# Другий етап: Арифметичні операції
sum = a + b
min = a - c
mno = c * d
dil = b / d
pow = c ** b
cd = a // d
ost = d % c

list1 = [sum, min, mno, dil, pow, cd, ost]

# Завдання 3
# Третій етап: Обчислення кількості елементів і виведення парних чисел
lengthOfList = len(list1)
print('Кількість елементів у списку:', lengthOfList)

print('Індекси чисел, що є парними:')
for index in range(len(list1)):
    if list1[index] % 2 == 0:
        print(index)

print('Парні значення в списку:')
for element in list1:
    if element % 2 == 0:
        print(element)

# Завдання 4
# Четвертий етап: Міняємо місцями елементи
list1[1], list1[4] = list1[4], list1[1]
print('Список після обміну другого та п’ятого елементів:', list1)

# Завдання 5
# П’ятий етап: Введення імені та прізвища для звіту
name = input("Введіть прізвище та ім'я: ")
print(name, "Виконав роботу №1.")
print(name, "Висновок: здобуті базові навички програмування на Python.")
