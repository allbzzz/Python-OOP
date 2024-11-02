"""
Создайте класс Lion. В нем должен быть метод roar, который печатает на экран "Rrrrrrr!!!"

Необходимо написать только определение класса

Пример работы с классом Lion

simba = Lion()
simba.roar() # печатает Rrrrrrr!!!
Sample Input:

Sample Output:

Rrrrrrr!!!
"""


# Напишите определение класса Lion       
class Lion:
    def roar(self):
        print('Rrrrrrr!!!')

# Ниже код для проверки класса Lion        
s = Lion()
assert isinstance(s, Lion)
assert s.__dict__ == {}
s.roar()