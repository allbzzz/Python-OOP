"""
Создайте класс Employee, который имеет следующие методы:

метод __init__, который устанавливает значения приватных атрибутов __name  и __salary: имя работника и его зарплату
 
приватный геттер метод для атрибута __name
 
приватный геттер метод для атрибута __salary
 
приватный сеттер метод для атрибута __salary: он должен позволять сохранять в атрибут __salary только положительные числа. В остальных случаях не сохраняем переданное значение в сеттер и печатаем на экран сообщение "ErrorValue:<value>".
 
свойство title, у которого есть только геттер из пункта 2.
 
свойство reward, у которого геттером будет метод из пункта 3, а сеттером — метод из пункта 4.
Sample Input:

Sample Output:

ErrorValue:-100
ErrorValue:hello
ErrorValue:777
ErrorValue:[1, 2]
"""


# Напишите определение класса Employee       
class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary
    
    def __get_name(self):
        return self.__name
    
    def __get_salary(self):
        return self.__salary
    
    def __set_salary(self, salary):
        if isinstance(salary, (int, float)) and salary >= 0:
            self.__salary = salary
        else:
            print(f"ErrorValue:{salary}")
    
    title = property(__get_name)
    reward = property(__get_salary, __set_salary)


# Ниже код для проверки методов класса Employee
employee = Employee("John Doe", 50000)
assert employee.title == "John Doe"
assert employee._Employee__name == "John Doe"
assert isinstance(employee, Employee)
assert isinstance(type(employee).title, property), 'Вы не создали property title'
assert isinstance(type(employee).reward, property), 'Вы не создали property reward'

assert employee.reward == 50000
employee.reward = -100  # ErrorValue:-100

employee.reward = 1.5
assert employee.reward == 1.5

employee.reward = 70000
assert employee.reward == 70000
employee.reward = 'hello'  # Печатает ErrorValue:hello
employee.reward = '777'  # Печатает ErrorValue:777
employee.reward = [1, 2]  # Печатает ErrorValue:[1, 2]
assert employee.reward == 70000
employee._Employee__set_salary(55000)
assert employee._Employee__get_salary() == 55000