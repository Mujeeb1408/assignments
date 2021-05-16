# To calculate the product of digits of given number
N = int(input('Enter a number: '))
digit = 1
product = 1
while N != 0:
    digit = N % 10
    product = product * digit
    N = N // 10
if product == 0:
    print('Product is zero :('+str(product)+')  enter a number with no zero in it')
else:
    print('The product of digits of given number is : ' + str(product))
