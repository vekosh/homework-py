# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# in -> out
# - 6782 -> 23
# - 0.67 -> 13
# - 198.45 -> 27

num = float(input('Введите число: '))
n = len(str(num))
num = int(num * 10 ** n)
x = 0
while num != 0:
    x += num % 10
    num //= 10
print(round(x))
