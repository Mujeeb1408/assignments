# program to accept sentence and print the long word present in the sentence
A = str(input('Enter a sentence: '))
B = max(A.split(), key=len)
print('The longest word present in given sentence is:(',B,')   and its length is',len(B))
