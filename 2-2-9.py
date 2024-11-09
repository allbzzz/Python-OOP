"""
Создайте класс Laptop, у которого есть:

конструктор __init__, принимающий 3 аргумента: бренд, модель и цену ноутбука. На основании этих аргументов нужно для экземпляра создать атрибуты brand, model, price и также атрибут laptop_name  строковое значение, следующего вида: "<brand> <model>"
hp = Laptop('hp', '15-bw0xx', 57000)
print(hp.price) # выводит 57000
print(hp.laptop_name) # выводит "hp 15-bw0xx"
И затем создайте 2 экземпляра класса Laptopи сохраните их в переменные laptop1 и laptop2.
Sample Input:

Sample Output:

Good
"""


# Напишите определение класса Laptop       
class Laptop:
    def __init__(self, brand = None, model = None, price = None):
        self.brand = brand
        self.model = model
        self.price = price
        self.laptop_name = f'{self.brand} {self.model}'
        
laptop1 = Laptop()
laptop2 = Laptop()

# Ниже код для проверки класса Laptop и ЭК laptop1 и laptop2


assert isinstance(laptop1, Laptop)
assert isinstance(laptop2, Laptop)

hp = Laptop('hp', '15-bw0xx', 57000)
assert hp.laptop_name == 'hp 15-bw0xx'
assert hp.price == 57000
assert isinstance(hp, Laptop)


lenovo = Laptop('lenovo', 'z-570-dx', 61000)
assert lenovo.brand == 'lenovo'
assert lenovo.model == 'z-570-dx'
assert lenovo.price == 61000
assert lenovo.laptop_name == 'lenovo z-570-dx'
assert isinstance(lenovo, Laptop)      
print('Good')