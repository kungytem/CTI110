# CTI-110
# P3HW2 - BasicMath
# Migle Kungyte
# 07/01/2020

# Ask user to enter first and second number.
num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))

# Define the functions.

def add(x,y):
    '''This function adds 2 umbers'''
    return x + y

def multiply(x,y):
    '''This function multiplies 2 numbers'''
    return x * y

def subtract(x,y):
    '''This function substracts 2 numbers'''
    return x - y

# Take input from user.
print ('Select operation')
print ('1.Add')
print ('2.Multiply')
print ('3.Subtract')
print ('4.Exit')
choice=input('Enter choice 1/2/3/4:')

# If user chose 1 - add 2 numbers.
if choice == '1':
    print(num1, '+', num2,'=', add(num1,num2))

# If user chose 2 - multiply 2 numbers.
elif choice == '2':
    print(num1, '*', num2,'=', multiply(num1,num2))

# If user chose 3 - subtract 2 number.
elif choice == '3':
    print(num1, '-', num2,'=', subtract(num1,num2))

# If user chose 4 - print program will terminate.
elif choice == '4':
    print('The program will terminate')

# If user enter number not in the list, display incorrect choice was entered
else:
    print('Incorrect choice was entered')
