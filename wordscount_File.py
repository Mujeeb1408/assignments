# program to calculate the number of occurance of words in file
filename = str(input('Enter the file name:'))
file = open(filename)
read = file.read()
w = read.split()
word = str(input('Enter the word: '))
count = 0
for wo in w:
    if wo == word:
        count = count + 1
print('The word ', word, ' is present ', count, ' times in the file.')
file.close()
