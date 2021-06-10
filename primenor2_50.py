# to print the prime numbers the in the range 2 to 50
lower = 2
upper = 50
print('Prime numbers between 2 and 50 are ')
for num in range (lower , upper+1):
    if num > 1:
        for i in (2, num):
            if (num % i) == 0:
                break
            else:
                print(num)
