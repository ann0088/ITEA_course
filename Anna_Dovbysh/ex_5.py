'''def my_function():
    print('From my function')

my_function()
my_function()
'''

'''def my_function(name):
    print(f'From my function {name}')

my_function('Olya')
my_function('Grisha')
'''


'''def my_function(name, country='Ukraine'):
    print(f'My name is: {name}')
    print(f'I am from : {country}')

my_function('Olya')
my_function('Grisha', country='Spain')
my_function(name='Maxim', country='Italy')
my_function('Nikita', country='Romania')
'''

'''def eat_food(food):
    for dish in food:
        print(f'eating {dish}..')
fruit = ['banana', 'apples', 'pineapples']
vegetables = ['potato', 'tomato']

eat_food(food=fruit)
eat_food(food=vegetables)
'''

'''def power(a, b):
    result = a**b
    return result

a = 2
b = 3
power_of_a_b = power(a, b)
print(power_of_a_b)
'''
'''
def power(a, b):
    return a**b

a = 2
b = 3
power_of_a_b = power(a, b)
print(power_of_a_b)
'''

import sys
print(sys.path)
