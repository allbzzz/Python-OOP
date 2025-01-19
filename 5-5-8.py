"""
Для следующего задания нам нужно реализовать базовым класс исключения PasswordInvalidError, который наследуется от стандартного класса исключений Exception. Этот класс можно использовать для обработки любых общих ошибок, связанных с неверными паролями.

От него нужно унаследовать следующие классы:

PasswordLengthError представляет ошибку, связанную с недостаточной длиной пароля;
 
PasswordContainUpperError представляет ошибку, связанную с отсутствием заглавных букв в пароле;
 
PasswordContainDigitError представляет ошибку, связанную с отсутствием цифр в пароле.
 

Создайте класс User с атрибутами username и password(пароль по умолчанию None). Класс должен иметь метод set_password, который принимает пароль и устанавливает его как значение атрибута password. Метод set_password должен также проверять, соответствует ли пароль заданным требованиям безопасности:

Длина пароля должна быть не менее 8 символов (в противном случае генерируется исключение PasswordLengthError с текстом Пароль должен быть не менее 8 символов);
 
Пароль должен содержать хотя бы одну заглавную букву (в противном случае генерируется исключение PasswordContainUpperError с текстом Пароль должен содержать хотя бы одну заглавную букву);
 
Пароль должен содержать хотя бы одну цифру (в противном случае генерируется исключение PasswordContainDigitError с текстом Пароль должен содержать хотя бы одну цифру);
Sample Input:

Sample Output:

Пароль должен быть не менее 8 символов
Пароль должен содержать хотя бы одну заглавную букву
Пароль должен содержать хотя бы одну цифру
"""


# Напишите определение класса User и классов исключений
class PasswordInvalidError(Exception):
    pass
class PasswordLengthError(PasswordInvalidError):
    pass
class PasswordContainUpperError(PasswordInvalidError):
    pass
class PasswordContainDigitError(PasswordInvalidError):
    pass

class User:
    def __init__(self, username, password=None):
        self.username = username
        self.password = password
        
    def set_password(self, password): 
        if len(password) < 8:
            raise PasswordLengthError('Пароль должен быть не менее 8 символов')
        elif not any(char.isupper() for char in password):
            raise PasswordContainUpperError('Пароль должен содержать хотя бы одну заглавную букву')
        elif not any (char.isdigit() for char in password):
            raise PasswordContainDigitError('Пароль должен содержать хотя бы одну цифру')
        else:
            self.password = password
 

# Ниже код для проверки
assert issubclass(PasswordInvalidError, Exception)
assert issubclass(PasswordLengthError, PasswordInvalidError)
assert issubclass(PasswordContainUpperError, PasswordInvalidError)
assert issubclass(PasswordContainDigitError, PasswordInvalidError)   

user = User("johndoe")

try:
    user.set_password("weakpwd")
except PasswordLengthError as e:
    print(e)

try:
    user.set_password("strongpassword8")
except PasswordContainUpperError as e:
    print(e)

try:
    user.set_password("Safepassword")
except PasswordContainDigitError as e:
    print(e)

user.set_password("SecurePass123")
assert user.password == 'SecurePass123'