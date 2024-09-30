"""
STEPS:
1. Create two user inputs, to play and player name.
2. Create a while loop -
   a. Set the iteration (lives)
   b. Create two conditions (routes), each with its own sub-conditions
   c. Some conditions go forward, some go backwards
   d. Check for invalid input and prompt for valid input
   e. Allow multiple answers (words, letters, spelling)
"""

play = str(input('Do you want to play? ')).capitalize()

while True:
    if play == 'Yes' or play == 'Y':
        name = input("Please enter your name: ").capitalize()
        if not name.isalpha():
            while True:
                name = input('Please enter a valid name (letters): ')
                if name.isalpha():
                    break
        print(f'Welcome to Views, {name}!')
        print("LET'S START!")
        break
    elif play == 'No' or play == 'N':
        print('GOODBYE!')
        quit()
    else:
        play = input('Please enter Yes, Y or No, N: ').capitalize()
        continue

lives = 4

while lives > 0:
    lives -= 1

    if lives == 0:
        print("You're out of lives. YOU LOSE!")
        print('GAME OVER!!')
        quit()

    options = ['door 1', 'door1', '1', 'door 2', 'door2', '2']
    answer = input('You are outside a castle facing two doors. Do you want to enter door 1 or door 2? ').lower()

    while True:
        if answer in options:
            break
        elif answer not in options:
            answer = input('Please enter: door 1, door 2, door1, door2, 1 or 2. ')
            continue

    if answer == 'door 1' or answer == 'door1' or answer == '1':
        print('You entered door 1. Inside you find stares that take you to the second floor.')

        answer = input("On the second floor there's a table with two pills - blue and red. Choose one: blue or "
                       "red? ").lower()

        while True:
            if answer not in ['blue', 'red']:
                print('Please choose from the options!')
                answer = input('Options: blue or red. ')
            elif answer in ['blue', 'red']:
                break

        if answer == 'blue':
            print('You are teleported back outside the castle!')
            continue
        elif answer == 'red':
            print("You are teleported to the third floor! There's a riddle on a mysterious wall.")

            answer = input('RIDDLE: I speak but I have no mouth, I listen but I have no ears. What am I? ').lower()

            if answer not in ['air', 'wind']:
                print('Invalid answer. Better luck next time!')
                continue

            if answer == 'air' or answer == 'wind':
                print('A door opens on the wall and you enter the fourth floor. A mysterious key appears on your hand.')

                answer = input('TRICK PUZZLE: There are two people in the room trying to get to the roof '
                               '- a little girl and an old lady. Who do you take with you? ').lower()

                if answer not in ['both', 'all', 'little girl', 'the little girl', 'girl', 'old lady']:
                    print('Invalid choice. Better luck next time!')
                    continue

                if answer == 'both' or answer == 'all':
                    print('You invite them to join you and share the view of the beautiful city. YOU WIN!!')
                elif answer == 'little girl' or answer == 'the little girl' or answer == 'girl':
                    print("You leave the old lady and deny her, her dying wish. Shame on you! YOU LOSE!!")
                elif answer == 'old lady':
                    print('You leave the little girl all by her self. Shame on you! YOU LOSE!!')
                else:
                    print('You go to the roof by yourself and a lightning hits you! YOU LOSE!!')
                print('THE END!!')
                quit()

    elif answer == 'door 2' or answer == 'door2' or answer == '2':
        print('You entered door 2. Inside you find an elevator that will take you to the third floor if you answer '
              'correctly')

        answer = input('MATHS TEST: sqrt of 100: ')

        while True:
            if not answer.isdigit():
                answer = input('Please enter a number (digit): ')
                continue
            else:
                if answer.isdigit():
                    break

        if answer != '10':
            print('Invalid answer. Better luck next time!')
            continue
        elif answer == '10':
            print("You are teleported to the third floor! There's a riddle on a mysterious wall.")

            answer = input('RIDDLE: I speak but I have no mouth, I listen but I have no ears. What am I? ').lower()

            if answer not in ['air', 'wind']:
                print('Invalid answer. Better luck next time!')
                continue

            if answer == 'air' or answer == 'wind':
                print('A door opens on the wall and you enter the fourth floor. A mysterious key appears on your hand.')

                answer = input('TRICK PUZZLE: There are two people in the room trying to get to the roof '
                               '- a little girl and an old lady. Who do you take with you? ').lower()

                if answer not in ['both', 'all', 'little girl', 'the little girl', 'girl', 'old lady']:
                    print('Invalid choice! Better luck next time.')
                    continue

                if answer == 'both':
                    print('You invite them to join you and share the view of the beautiful city. YOU WIN!!')
                elif answer == 'little girl' or answer == 'the little girl' or answer == 'girl':
                    print("You leave the old lady and deny her, her dying wish. Shame on you! YOU LOSE!!")
                elif answer == 'old lady':
                    print('You leave the little girl all by her self. Shame on you! YOU LOSE!!')
                else:
                    print('You go to the roof by yourself and a lightning hits you! YOU LOSE!!')
                print('THE END!!')
                quit()
