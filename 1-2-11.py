"""
Теперь давайте тренироваться удалять атрибуты в классе. Для этого вам необходимо из класса Book удалить три атрибута:

pages 
writer
rating
Удаление выполните с помощью оператора del и функции delattr

Ничего выводить на экран не требуется в этом задании

"""


class Book:
    name = '1984'
    writer = 'Джордж Оруэлл'
    pages = 213
    rating = 8.7
    genre = 'dystopian'
    
    
del Book.pages
del Book.writer
delattr(Book, 'rating')