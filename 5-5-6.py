"""
Перед вами имеется часть готового кода. Ваша задача дописать функцию get_user: она должна принимать логин пользователя и возвращать имя пользователя из словаря users. Если логин отсутствует, необходимо возбуждать исключение UserNotFoundError с текстом User not found

Также не забудьте реализовать класс-исключение UserNotFoundError

Sample Input 1:

alice
Sample Output 1:

Alice Smith
Sample Input 2:

vinnie
Sample Output 2:

User not found
Sample Input 3:

jack
Sample Output 3:

Jack Wild
"""


class UserNotFoundError(Exception):
    pass

users = {
    "alice": {"name": "Alice Smith", "email": "alice@example.com"},
    "bob": {"name": "Bob Johnson", "email": "bob@example.com"},
    "jack": {"name": "Jack Wild", "email": "jack_wild@example.com"}
}

def get_user(username):
    if username in users:
        return users[username]["name"]
    else:
        raise UserNotFoundError("User not found")

try:
    username = get_user(input())
except UserNotFoundError as e:
    print(e)
else:
    print(username)