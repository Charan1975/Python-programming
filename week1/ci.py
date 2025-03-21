p=int(input('entre the principle interest value:'))
t=int(input('entre the time taken value:'))
r=int(input('entre the rate of interest value:'))
A= p*(1+(r/100))**t
ci=(A-p)
print(ci)
