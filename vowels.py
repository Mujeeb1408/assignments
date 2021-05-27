# counting vowels and consonants in string
string = str(input('Enter a string:'))
vowels = 0
consonants = 0
for letter in string:
    if letter == 'a' or letter =='e' or letter== 'i' or letter== 'o' or letter=='u':
        vowels = vowels+1
    else:
        consonants += 1
print('Number of vowels in given string :', vowels)
print('Number of consonants in given string :', consonants)