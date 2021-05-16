# to reverse the given number & checking for palindrome
N = int(input('Enter a Number N: '))
i = 1
reverse = 0
temp = N
while N > 0:
    n = N % 10
    reverse = reverse*10 + n
    N = int(N/10)
    i = i+1
if reverse == temp:
    print('Given number is palindrome :' + str(reverse))
else:
    print('Given number is not palindrome reverse is :' + str(reverse))