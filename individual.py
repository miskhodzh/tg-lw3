#1. Даны два числа. Найти среднее арифметическое и среднее геометрическое их модулей.

n1 = int(input('Введите первое число >>> '))
n2 = int(input('Введите второе число >>> '))

abs1 = abs(n1)
abs2 = abs(n2)

arithmetic_mean = (abs1+abs2)/2
geometric_mean = (abs1*abs2)**0.5

print(arithmetic_mean)
print(geometric_mean)