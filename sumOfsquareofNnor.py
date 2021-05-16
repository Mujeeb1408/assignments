# to calculate the sum of square of natural number
print('Enter the N number: ')
N = int(input())
sum = 0
i = 1
while i <= N:
    sum = sum + i ** 2;
    i = i + 1
print("Sum of square of", str(N) , "Natural number " + str(sum) )

