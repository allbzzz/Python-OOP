"""
Предположим, у нас есть класс WeatherStation для метеостанции, которая собирает данные с нескольких датчиков. Каждый экземпляр датчика можно создать отдельно, но вы все равно хотите поддерживать единое состояние для всей метеостанции. Для этого можно использовать шаблон Моносостояния, имея общее состояние для всех экземпляров класса датчика.

Датчики будут измерять температуру, влажность и давление. Ваша задача определить класс WeatherStation, у которого

имеются разделяемые атрибуты temperature, humidity и pressure. Вот их начальные состояния:
{"temperature": 0, "humidity": 0, "pressure": 0}
метод update_data, который изменяет состояние сразу трех показаний.
 
метод get_current_data, который возвращает кортеж показаний  temperature, humidity и pressure.
Sample Input:

Sample Output:

Good
"""


#  напишите определение класса WeatherStation    
class WeatherStation:
    __shared_attr = {"temperature": 0, "humidity": 0, "pressure": 0}
   
    def __init__(self):
        self.__dict__ = WeatherStation.__shared_attr
        
    def update_data(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
    
    def get_current_data(self):
        return (self.temperature, self.humidity, self.pressure)


# код для проверки
sensor1 = WeatherStation()
assert sensor1.temperature == 0
assert sensor1.humidity == 0
assert sensor1.pressure == 0
sensor2 = WeatherStation()
assert sensor2.get_current_data() == (0, 0, 0)
sensor1.update_data(25, 60, 103)
assert sensor1.get_current_data() == (25, 60, 103)
assert sensor2.get_current_data() == (25, 60, 103)
sensor3 = WeatherStation()
assert sensor3.get_current_data() == (25, 60, 103)
sensor3.update_data(50, 20, 10)
assert sensor1.get_current_data() == (50, 20, 10)
assert sensor2.get_current_data() == (50, 20, 10)
print('Good')