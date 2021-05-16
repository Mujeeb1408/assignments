# to calculate the sum of given n enven numbers
N = int(input('Enter the number N: '))
sum_of_even = 0
i = 2
n = 1
while i <= N:
    n = i % 2;
    if n == 0:
        sum_of_even = sum_of_even + i;
    i = i + 1
print('Sum of even number: ' + str(sum_of_even))
