def quiz():
    playing = input('Do you want to play? ')
    print(playing)

    if playing != 'yes':
        quit()
    print('Okay! Lets play')

    score = 0

    while True:
        answer = input('What does CPU stand for? ').title()
        print(answer)

        if answer == 'Central Processing Unit':
            print('Correct')
            score += 1
            break
        elif answer != 'Central Processing Unit':
            if not all(char.isalpha() or char.isspace() for char in answer):
                print('Please enter words next time!')
                continue
            print('Incorrect')
            print('SECOND CHANCE!!')
            answer = input('CLUE: Main brain of the computer. ')
            if answer == 'Central Processing Unit':
                print('Correct')
                score += 0.5
                break
            else:
                print('Incorrect!')
                break

    while True:
        answer = input('What is the sqrt of 81? ')
        print(answer)
    
        if answer == '9':
            print('Correct')
            score += 1
            break
        elif answer != '9':
            if not answer.isdigit():
                print('Please enter a number next time!')
                continue
            print('Incorrect')
            print('SECOND CHANCE!!')
            answer = input('CLUE: x multiplied by x. ')
            if answer == '9':
                print('Correct')
                score += 0.5
                break
            else:
                print('Incorrect')
                break

    while True:
        answer = input('Where is The Camp Nou Stadium located? ').title()
        print(answer)
    
        if answer == 'Barcelona':
            print('Correct')
            score += 1
            break
        elif answer != 'Barcelona':
            if not all(char.isalpha or char.isspace for char in answer):
                print('Please enter words next time!')
                continue
            print('Incorrect')
            print('SECOND CHANCE!!')
            answer = input('CLUE: Messi played here while in Spain. ')
            if answer == 'Barcelona':
                print('Correct')
                score += 0.5
                break
            else:
                print('Incorrect')
                break

    while True:
        answer = input('How many days are in a year? ')
        print(answer)
    
        if answer == '365':
            print('Correct')
            score += 1
            break
        elif answer != '365':
            if not answer.isdigit():
                print('Please enter a number next time!')
                continue
            print('Incorrect')
            print('SECOND CHANCE!!')
            answer = input('CLUE: Not including leap day. ')
            if answer == '365':
                print('Correct')
                score += 0.5
                break
            else:
                print('Incorrect')
                break

    while True:
        answer = input('Who is the creator of Marvel? ').title()
        print(answer)

        options = ['Stan-Lee', 'Stan Lee']
        if answer in options:
            print('Correct')
            score += 1
            break
        elif answer not in options:
            if not all(char.isalpha() or char.isspace() for char in answer):
                print('Please enter words next time!')
                continue
            print('Incorrect')
            print('SECOND CHANCE!!')
            answer = input('CLUE: The old man in Marvel movies (cameo). ')
            if answer in options:
                print('Correct')
                score += 0.5
                break
            else:
                print('Incorrect')
                break

    while True:
        answer = input('What is 5 - 3? ')
        print(answer)
    
        if answer == '2':
            print('Correct')
            score += 1
            break
        elif answer != '2':
            if not answer.isdigit():
                print('Please enter a number next time!')
                continue
            print('Incorrect')
            print('SECOND CHANCE!!')
            answer = input('CLUE: From 5, count 3 times to the left. ')
            if answer == '2':
                print('Correct')
                score += 0.5
                break
            else:
                print('Incorrect')
                break

    return score


def score_check(score):
    if score == 3 or score == 4:
        return 'Average Score. Try Again!'
    elif score < 3:
        return 'Below Average Score. Do Better!'
    elif score > 4:
        return 'Above Average Score. Smart Kid!'
    else:
        quit()


game = quiz()
result = score_check(game)

print(f'You got {game} out of 6')
print(result)
