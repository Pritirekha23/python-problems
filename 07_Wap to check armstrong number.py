# WAP TO CHECK A NUMBER IS ARMSTRONG OR NOT.
#Example:

#Input : 153
#Output : Yes
#153 is an Armstrong #number.
#1*1*1 + 5*5*5 + 3*3*3 = 153

#Input : 120
#Output : No
#120 is not a Armstrong number.
#1*1*1 + 2*2*2 + 0*0*0 = 9

#Input : 1253
#Output : No
# 1253 is not a Armstrong Number
#1*1*1*1 + 2*2*2*2 + 5*5*5*5 + 3*3*3*3 = 723

num=int(input('Enter a number::'))
sum=0
temp=num
while temp>0:
    di=temp%10
    sum+=di**3
    temp//=10
if num==sum:
    print('this is an armstrong number',num)
else:
     print('this is not an armstrong number')