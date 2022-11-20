#given two positive integers start and end. The task is to write a Python program to print all Prime numbers in an Interval.

#Definition: A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. The first few prime numbers are {2, 3, 5, 7, 11, ….}.


# way-1
lowerval=int(input('Enter the lowest range::'))

upperval=int(input('Enter the upper range::'))

print('the prime numbers in the range are::')
for n in range(lowerval,upperval+1):
    if n>1:
        for i in range(2,n):
            if (n%i)==0:
                break
        else:
            print(n)


# way-2
l=[]
for i in range(20,60):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        l.append(i)
print(l)