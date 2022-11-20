# WAP TO CHECK A NUMBER IS PRIME OR NOT


# way -1
num=int(input('Enter a number::'))
#prime numbers are greater than 1
if num>1:
    for i in range(2,num):
        if(num%i)==0:
            print(num,'is not a prime number')
            print(i,'times',num//i,'is',num)
            break
    else:
        print('This is a prime number',num)
else:
    print('The number is not a primt number',num)


# way-2
num=int(input('Enter a number::'))
flag=False
if num>1:
    for i in range(2,num):
        if(num%i)==0:
            flag=True
            break
if flag:
    print('This is not a prime number',num)
else:
    print('This is a prime number',num)