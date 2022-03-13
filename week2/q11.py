#Random number Game!
import random
n = random.randint(1,20)
i=1
while i<=5:
    guess=int(input('Enter your guess number:'))
    if guess==n:
        print('You Win')
    else:
        print('Game over!')
    i+=1
print('The random number was:{}'.format(n))

