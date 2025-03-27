import random
n=random.randint(1,100)
while True:
    x=int(input('guess th number:'))
    if(x<n):
      print('nmber is too low')
    elif(x>n):
      print('number is too high')
    else:
      print('congrats, number is found')
