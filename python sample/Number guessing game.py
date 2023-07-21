#Number guessing game
import random

number = random.randint(0, 100)
print('Number: ',number)
trials = 5
message = 'You Lost!'   

while trials > 0:
    print(f'{trials} attempt left.')
    trials -= 1
    user_input = int(input('Enter Number: '))

    if user_input == number:
        message = 'You Won!'
        break
    else:
        print('Try again!')
        continue

print(message)