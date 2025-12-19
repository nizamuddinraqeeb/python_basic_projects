print('** HCF **')
num1 = int(input('Enter 1st number: '))
num2 = int(input('Enter 2nd number: '))

hcf = 1

for i in range(2,num1+1):
    if num1%i ==0 and num2%i ==0:
        hcf = i

print(f'HCF of {num1} and {num2} is {hcf}\n')

print('-----------------------\n')

print('** LCM **')
num1 = int(input('Enter 1st number: '))
num2 = int(input('Enter 2nd number: '))

lcm = num1*num2

for i in range(num1*num2, num1, -1):
    if i%num1 ==0 and i%num2 ==0:
        lcm = i

print(f'LCM of {num1} and {num2} is {lcm}\n')
