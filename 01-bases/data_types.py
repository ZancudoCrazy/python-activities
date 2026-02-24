# Data types
age:int = 28
name:str = 'Adrian'
str_age:str = '28'
# print('Edad: ' + edad) wrong
print('Edad: '+ str(age)) # good
print(f'Edad: {age + 1}') # better
# print(f'Edad: {strAge + 1}')  wrong
print(f'Edad: {int(str_age) + 1}') # good

x = 1
print(x)

x = 'Hello'
print(x)