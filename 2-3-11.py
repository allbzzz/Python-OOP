"""
Создание приложения для учета задач
Необходимо создать приложение для учета задач, которое будет использовать классы Task, TaskList и TaskManager.

 

Класс Task будет хранить информацию о задаче (название, описание, статус выполнения), состоит из: 

метода __init__, принимающий  и сохраняет в атрибуты экземпляра name , description и status. По умолчанию status равен False.
 
метод display , который печатает информацию в следующем виде:
​​​​​{название задачи} (Сделана/Не сделана)
В зависимости от статуса задачи выводится Сделана или Не сделана 
 

Класс TaskList будет содержать список задач и методы для добавления/удаления задач, состоит из:

метода __init__, который должен создать пустой список задач в атрибуте tasks
 
метода add_task, который принимает задачу и добавляет ее в конец списка задач
 
метода remove_task, который принимает задачу и удаляет ее из списка задач
 

Класс TaskManager будет содержать методы для отображения списка задач и изменения статуса выполнения задач. В нем должно быть реализовано:

метод __init__, который должен принимать экземпляр TaskList  и сохранять его в атрибуте  task_list
 
метод  mark_done, который принимает задачу (экземпляр Task)  и устанавливает ей истинный статус выполнения
 
метод  mark_undone, который принимает задачу (экземпляр Task)  и устанавливает ей ложный статус выполнения
 
метод  show_tasks, который для каждой хранящейся задачи в списке вызывает метод display
Sample Input:

Sample Output:

Стирка (Не сделана)
-----Список дел-----
Стирка (Не сделана)
Продукты (Не сделана)
-----Список дел-----
Стирка (Сделана)
Продукты (Не сделана)
-----Список дел-----
Стирка (Сделана)
"""


# Напишите определение классов Task, TaskList и TaskManager
class Task:
    def __init__(self, name, description, status = False):
        self.name = name
        self.description = description
        self.status = status
    
    def display(self):
        if self.status:
            status_label = '(Сделана)'
        else:
            status_label = '(Не сделана)'
        print(f'{self.name} {status_label}')

            
class TaskList:
    def __init__(self):
        self.tasks = []
        
    def add_task(self, task):
        self.tasks.append(task)
            
    def remove_task(self, task):
        self.tasks.remove(task)

        
class TaskManager:
    def __init__(self, taskList):
        self.task_list = taskList
        
    def mark_done(self, task):
        self.task = task
        task.status = True
    
    def mark_undone(self, task):
        self.task = task
        self.status = False
    
    def show_tasks(self):
        for task in self.task_list.tasks:
            task.display()
            

# Ниже код для проверки классов Task, TaskList и TaskManager

# Создаем список задач
todo = TaskList()
assert todo.tasks == []

# Создаем несколько задач и добавляем их в список
task1 = Task("Стирка", "Постирать трусы, носки, слюнявчики")
assert task1.name == 'Стирка'
assert task1.description == 'Постирать трусы, носки, слюнявчики'
assert task1.status is False
task1.display()

todo.add_task(task1)
assert len(todo.tasks) == 1

task2 = Task("Продукты", "Купить лук чеснок огурцы хлеб и биток")
assert task2.name == 'Продукты'
assert task2.description == 'Купить лук чеснок огурцы хлеб и биток'
assert task2.status is False

todo.add_task(task2)
assert len(todo.tasks) == 2

# Создаем менеджер задач и показываем список задач
manager = TaskManager(todo)
assert isinstance(manager.task_list, TaskList)
print('-----Список дел-----')
manager.show_tasks()

# Отмечаем первую задачу выполненной и показываем список задач
manager.mark_done(task1)

# Проверяем изменился ли статус 2мя способами
assert task1.status is True
assert manager.task_list.tasks[0].status is True

print('-----Список дел-----')
manager.show_tasks()

# Удаляем вторую задачу и показываем список задач
todo.remove_task(task2)

assert len(todo.tasks) == 1
assert len(manager.task_list.tasks) == 1

print('-----Список дел-----')
manager.show_tasks()