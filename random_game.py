# Make a game where the user says a number between 1-5, and if its the same num as the computer they win.
# Else, they lose and keep playing till they win.
import random, time

begin_game = input('    Let\'s play a game! (yes/no) ')
print(' ')

while begin_game == 'yes':
    user_num = int(input('  Give me a number between 1 & 5. '))
    print(' ')
    random_num = random.randint(1,5)
    print (f'The Random Number: {random_num}')
    print(f'Your Number: {user_num}\n')
    if random_num == user_num:
        print('You guessed the number, you won!\n')
        begin_game = input('    Want to play again? (yes/no) ')
    else:
        print('You lost, womp womp\n')
        begin_game = input('    Play again? ')
    
        
        
        