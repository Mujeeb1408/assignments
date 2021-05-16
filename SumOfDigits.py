# To calculate the sum of digits of given number
N = int(input('Enter a number: '))
i = 1
sum = 0
n = 0
while i < N:
    n = N % 10
    sum = sum + n
    N = N / 10
    i = i + 1
print(int(sum))
