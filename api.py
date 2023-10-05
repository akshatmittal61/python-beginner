from json import *
from requests import *


def get_users():
    res = get(url='https://jsonplaceholder.typicode.com/users')
    res.raise_for_status()
    data = res.json()
    # return dumps(data)
    return data


users = get_users()

for user in users:
    # print(type(user))
    # print(user['name'])
    # print(loads(dumps(user)))
    print(user)