# WAP TO FIND OUT COMPOUND INTEREST
#Let us discuss the formula for compound interest. The formula to calculate compound interest annually is given by: 

#A = P(1 + R/100) t 

#Compound Interest = A – P 

#Where, 
#A is amount 
#P is the principal amount 
#R is the rate and 
#T is the time span

#Input: Principle (amount): 1200, Time: 2, Rate: 5.4
#Output: Compound Interest = 133.099243

#way-1
def Comintrst(p,r,t):
    A=p*(pow((1+r/100),t))
    Cintrst=A-p
    print('compound interest is ',Cintrst)
Comintrst(1200,5.4,2)


#way-2
p= 1200   
t= 2      
r= 5.4   
a=p*(1+(r/100))**t  
ci=a-p  
print(ci)