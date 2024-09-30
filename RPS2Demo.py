"""
STEP:
1. Import the random module
2. a. Create a def for game
      i. Create options
      ii. Create user input and randomise computer choice
      iii. Create  dic to hold choices
      iv. return choices
    b. Create a def to check win (set choices as parameters)
       i. Set winning and losing conditions then return
3. Set game iteration and scores
4. Loop game -
   a. Check win or lose
   b. Decrement iteration and increment scores
5. Print the final scores
"""

import random


def game():
    options = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(options)
    while True:
        player_choice = input('Enter: ')
        if player_choice in options:
            break
        else:
            print('Please enter rock, paper or scissors')
            continue

    choices = {'player': player_choice, 'computer': computer_choice}
    return choices


def check_win(player, computer):
    print(f'You chose {player}, Computer chose {computer}')

    if player == computer:
        return 'Its a tie!'
    elif player != computer:
        if player == 'rock' and computer == 'scissors':
            return 'You win!'
        elif player == 'paper' and computer == 'rock':
            return 'You win!'
        elif player == 'scissors' and computer == 'paper':
            return 'You win!'
        else:
            return 'You lose!'


game_time = 5
user = 0
pc = 0

while game_time > 0:
    game_time -= 1
    result = game()
    if result:
        my_choice, pc_choice = result['player'], result['computer']
        outcome = check_win(my_choice, pc_choice)
        print(outcome)
        if outcome == 'You win!':
            user += 1
        elif outcome == 'You lose!':
            pc += 1
    else:
        break

print(f'Your score is {user}, Computer score is {pc}')

if user == pc:
    print('The scores are even. GAME OVER!')
elif user > pc:
    print('You have won the game. CONGRATULATIONS!!')
else:
    print('The computer won the game. BETTER LUCK NEXT TIME!!')
