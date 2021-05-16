# to check the given number is prime or not
N = int(input('Enter a number :'))
i = 2
if N == 1 and N == 0:
    print('Not a prime number')
while i < N:
    n = N % i
    i = i+1
if n == 0:
    print(str(N)+' is not a prime number')
else:
    print(str(N)+' is a prime number')

