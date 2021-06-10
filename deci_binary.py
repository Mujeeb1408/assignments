# program to convert the decimal number to binary number
def decimal_binary(a):
    if a >= 1:
        decimal_binary(a // 2)
    print(a % 2, end=' ')


x = int(input('Enter a decimal number : '))
decimal_binary(x)
