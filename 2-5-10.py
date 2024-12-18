"""
В этом задании научимся просто вызывать защищенные и приватные методы у экземпляров класса.

Представьте, что у вас есть такой класс:

class PizzaMaker:
     def __make_pepperoni(self):
         ...

     def _make_barbecue(self):
         ...
Реализацию самих методов мы опустим. Ваша задача вызвать у экземпляра класса maker сначала метод _make_barbecue , затем метод __make_pepperoni .
Именно в такой последовательности. Создавать класс вам не нужно, он уже создан и доступен, просто вам не виден.
"""


maker = PizzaMaker()

maker._make_barbecue()
maker._PizzaMaker__make_pepperoni()

