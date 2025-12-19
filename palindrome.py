#palindrome is a word that remains same if spelt backword
#like nan or gaag
word = input('Enter a word to check: ')

#1st method by using a list reverse
print('Using list reverse method: ')

word_list = list(word)
word_reverse = word_list[::-1]

if word_list == word_reverse:
    print(f'\"{word}\" is a palindrome.')
else:
    print(f'\"{word}\" is not a palindrome.')

#2nd method by string slicing and comparing
print('\nUsing String slicing method: ')
length = len(word)

#we will check if length of word is even or odd
if length % 2 == 0:
    #if length is even we'll compare 1st half with reverse of 2nd half
    if word[:length//2] == word[-1:length//2-1:-1]:
        print(f'\"{word}\" is a palindrome.')
    else:
        print(f'\"{word}\" is not a palindrome.')

else:
    
    if word[:length//2] == word[-1:length//2:-1]:
        print(f'\"{word}\" is a palindrome.')
    else:
        print(f'\"{word}\" is not a palindrome.')
        