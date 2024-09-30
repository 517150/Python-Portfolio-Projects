import random

"""
STEPS:
1. Create a user input for the number that will be used
2  a. Convert the string (input) into an integer
   b. Prompt for the required values (integers) if user input is incorrect #didn't use a try block
3. Create a random number generator (using user input as a stop range)
4. Create score
5. Use a while loop -
  a. Increment score
  b. Create a user input for guesses (within the stop range)
  c. Repeat step 2, plus for the user to stay within range
  d. Compare user input to random number and print relevant message. Break if correct!
"""

while True:
    enter_range = input('Enter a number: ')
    if enter_range.isdigit():
        enter_range = int(enter_range)
        if enter_range <= 0:
            print('Please enter a number larger than 0!')
            continue
        break
    else:
        print('Please enter a number next time!')
        continue

random_number = random.randint(0, enter_range)
guesses = 0
score = 10

while score > 0:
    guesses += 1
    score -= 1

    user_guess = input('Make a guess: ')
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please enter a number next time!')
        continue

    if user_guess == random_number:
        score += 1
        if score == 10:
            print('First try. PERFECT!!')
        else:
            print('You got it in', guesses, 'guesses')
        break
    elif user_guess > random_number:
        if user_guess > enter_range:
            print(f'Please enter a number within {enter_range}')
            continue
        print('The number is lower!')
    else:
        print('The number is higher!')

    if score == 3:
        hint1 = random_number - random.randint(0, 5)
        if hint1 < 0:
            hint1 = 0
        hint2 = random_number + random.randint(0, 5)
        if hint2 > enter_range:
            hint2 = enter_range
        while hint1 == hint2:
            continue
        print(f'Hint: {hint1} - {hint2}')

    if score == 0:
        print(f'The number is: {random_number}')
        print('You are out of guesses')
        print("You didn't get it. SORRY!!")


print('Your score is', score, 'out of 10')
