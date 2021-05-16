# Check the given number is amstrong or not
N = int(input('Enter a number: '))
digit=0
a=0
temp=N
sum=0
while N!=0:
    digit = N%10
    a=digit**3
    sum+=a
    N=N//10
if sum==temp:
    print(str(temp)+' is an amstrong number')
else:
    print(str(temp)+' is not an amstrong number because '+str(sum)+' is not equal to '+str(temp) )