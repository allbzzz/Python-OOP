"""
Теперь ваша задача изменить значения атрибутов name и pages:

в атрибут name необходимо присвоить значение «Скотный двор»
в атрибут pages необходимо положить значение 115
Изменение атрибутов необходимо выполнить при помощи функции setattr

Выводить ничего не нужно, просто поменяйте значения атрибутов класса

"""


class Book:
    name = '1984'
    writer = 'Джордж Оруэлл'
    pages = 213
    

setattr(Book, 'name', 'Скотный двор')
setattr(Book, 'pages', 115)