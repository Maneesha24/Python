import random
print('...rock...')
print('...paper...')
print('...scissors...')

user_score, computer_score = 0, 0
winning_score = 2

while(user_score < winning_score and computer_score < winning_score):
    print(f'Your score: {user_score} and Computer score: {computer_score}')

    # prompts user to enter choice (rock/paper/scissors)
    user_choice = input('Enter your choice: ')
    
    # generates random computer choice (rock/paper/scissors)
    random_choice = random.randint(1,3)
    if(random_choice == 1):
        computer_choice = 'rock'
    elif(random_choice == 2):
        computer_choice = 'paper'
    else:
        computer_choice = 'scissors'

    print(f'Computer chose {computer_choice}')

    # computer winning choice
    if (user_choice == 'rock' and computer_choice == 'paper') or (user_choice == 'scissors' and computer_choice == 'rock'):
        print('Computer wins!')
        computer_score += 1

    # Draw choice
    elif (user_choice == computer_choice):
        print('It\'s a draw')

    # user winning choice
    else:
        print('You win!')
        user_score += 1


print(f'Your score: {user_score} and Computer score: {computer_score}')

if(user_score > computer_score):
    print('YOU WON THE FINAL GAME!')

elif(user_score < computer_score):
    print('COMPUTER WON THE FINAL GAME!')
