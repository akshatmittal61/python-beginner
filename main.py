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

try:
    n1 = int(input('Enter num 1: '))
    n2 = int(input('Enter num 2: '))
    print(f'Add: {n1 + n2}')
except ValueError as e:
    print(e)
finally:
    print('Done with it')
# except:
#     print('Something went wrong')