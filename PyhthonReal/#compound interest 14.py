#compound interest 14
#A is the amount of money in the account after the specified number of years.
#P is the principal amount that was originally deposited into the account.
#r is the annual interest rate.
#n is the number of times per year that the interest is compounded.
#t is the specified number of years.



P=int(input('the principal amount that was originally deposited into the account:'))
r=int(input('the annual interest rate:'))
n=int(input('the number of times per year that the interest is compounded:'))
t=int(input('the specified number of years:'))
A=P*(1+(r/n))**(n*t)
print('the amount of money in the account after the specified number of years is',A)