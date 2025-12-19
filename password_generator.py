import random
length = int(input('Enter password length: '))

ask_nums = input('Do you want numbers to be used?(y/n)').strip().lower()
ask_upper = input('Do you want Capital letters to be used?(y/n)').strip().lower()
ask_lower = input('Do you want Small letters to be used?(y/n)').strip().lower()
ask_symbols = input('Do you symbols to be used?(y/n)').strip().lower()

char_list = []

if ask_nums == 'y':
    char_list += ['0','1','2','3','4','5','6','7','8','9']
if ask_upper == 'y':
    char_list += [
    'A','B','C','D','E','F','G','H','I','J','K','L','M',
    'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
if ask_lower == 'y':
    char_list += [
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z']
if ask_symbols == 'y':
    char_list += [
    '!', '@', '#', '$', '%', '^', '&', '*',
    '(', ')', '-', '_', '=', '+']

password = ''
for i in range(length):
    temp = random.choice(char_list)
    password += temp
    char_list.remove(temp)

print(f'Your password is   {password}')