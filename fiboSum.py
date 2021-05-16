# to calculate the sum of series
N = int(input('Enter a number: '))
a=0
b=1
fibo=0
i=1
sum=1
while i < N-1:
    fibo = a+b
    i = i+1
    a = b
    b = fibo
    sum = sum+fibo
print('The sum of fibonacci series is:'+str(sum))
