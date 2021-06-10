# Program to demonstrate Countintg ,Summing and average of numbers using loopings
N = int(input('Enter the number : '))
i = 0
sum = 0
avg = 0
if N==0:
    print('Enter a number other than zero')
else:
    while i <= N:
        sum += i
        i = i + 1
    avg = sum/(i-1)
    print('There are ',i-1,' Numbers')
    print('The sum of the total numbers is: ' , sum)
    print('The average of the given numbers is :',avg)
