"""
Теперь давайте каждое возможное исключение отлавливать отдельным блоком except.

Если возникает исключение типа ValueError , то необходимо вывести фразу «Введите целое число»

Если возникает исключение типа ZeroDivisionError, то необходимо вывести фразу «Делитель не должен быть равен нулю»

Sample Input 1:

15
5
Sample Output 1:

Результат деления a на b: 3.0
Sample Input 2:

8
0
Sample Output 2:

Делитель не должен быть равен нулю
Sample Input 3:

Follow the Cops Back Home
5
Sample Output 3:

Введите целое число
"""


try:
    a = int(input())
    b = int(input())
    print(f"Результат деления a на b: {a/b}")
except (ValueError):
    print('Введите целое число')
except ZeroDivisionError:
    print('Делитель не должен быть равен нулю')