# print('Hello World')
# name = input('Please enter your name: ')
# print(f'Hi, {name} \nI am Gojo')
# x = 7 + 61
# print(x)

# first_name = 'akshat'
# last_name = 'mittal'
# print('Hello! My name is ' + first_name.capitalize() + ' ' + last_name.capitalize())
# print('Hello! My name is {} {}'.format(first_name, last_name))
# print('Hello! My name is {1} {0}'.format(last_name, first_name))
# print(f'Hello! My name is {first_name} {last_name}')

# age = 7
# Error cannot concatenate int and str
# print('Jake is ' + age + 'years old')
# n1 = input('Number 1: ')  # 3
# n2 = input('Number 2: ')  # 2
# print(n1 + n2)  # Prints string concatenation -> '4' + '2' = '32'
# n1 = int(input('Number 1: '))  # 3
# n2 = int(input('Number 2: '))  # 2
# print(n1 + n2)  # Prints addition -> 3 + 2 = 5
# print(n1 - n2)  # Subtraction -> 3 - 2 = 1
# print(n1 * n2)  # Multiplication -> 3 * 2 = 6
# print(n1 / n2)  # Division -> 3 / 2 = 1.5
# print(n1 ** n2)  # Exponent -> 3 ** 2 = 9

# try:
#     n1 = int(input('Enter num 1: '))
#     n2 = int(input('Enter num 2: '))
#     print(f'Add: {n1 + n2}')
# except ValueError as e:
#     print(e)
# finally:
#     print('Done with it')
# except:
#     print('Something went wrong')

# fruits = ['Apple', 'Mango', 'Banana']
# print(len(fruits))
# fruits.append('Papaya')
# fruits.insert(1, 'Pineapple')
# fruits.sort()  # Works in-place
# print(fruits, fruits[1], fruits[:3], fruits[1:3], fruits[-1], fruits[-1:-3], fruits[-3:-1])
#
# user = {
#     'name': 'Akshat',
#     'age': 21,
#     'stack': 'full',
#     'tags': ['developer', 'poet', 'hunter']
# }
# print(user, len(user), len(user['tags']))
# user['weather'] = 'fall'
# users = []
# users.append(user)
# users.append('null')
# users.append(7)
# print(users)


# people = ['Jane', 'Kate', 'Christopher', 'Fiona']
#
# for person in people:
#     print(person.capitalize())
#
# for i in range(1, 21, 2):
#     print(i)

def generate_username(name, emp_id):
    first_char = name.split()[0][0].lower()
    second_char = name.split()[1][0].lower()
    num_id = emp_id[-3:]
    return first_char + second_char + num_id


# username = generate_username('Akshat mittal', 'emp102947')
username = generate_username(emp_id='emp102947', name='Jane doe')
print(username)
