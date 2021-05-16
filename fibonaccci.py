# to print the fibonacci series
N = int(input('Enter a number: '))
a=0
b=1
fibo=0
i=1
print(0)
print(1)
while i < N-1:
    fibo = a+b
    i = i+1
    a = b
    b = fibo
    print(str(fibo))
