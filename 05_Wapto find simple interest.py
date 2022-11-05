# dt-1 nov 2022
# WAP TO FOR SIMPLE INTEREST
#Simple Interest = (P x T x R)/100 Where, P is the principle amount T is the time and R is the rate .
# EXAMPLE1:
#Input : P = 10000
 #       R = 5
  #      T = 5
#Output :2500.0
#We need to find simple interest on 
#Rs. 10,000 at the rate of 5% for 5 
#units of time.

#EXAMPLE2:
#Input : P = 3000
#        R = 7
 #       T = 1
#Output :210.0

# example 1
def simpleintrst(p,t,r):
    print('principal is',p)
    print('time period is',t)
    print('rate of interest is',r)
    sintrst=(p*t*r)/100
    print('Simple interest is',sintrst)
simpleintrst( 10000,5,5)

# example 2
def simpleintrst(p,t,r):
    print('principal is',p)
    print('time period is',t)
    print('rate of interest is',r)
    sintrst=(p*t*r)/100
    print('Simple interest is',sintrst)
simpleintrst( 3000,7,1)