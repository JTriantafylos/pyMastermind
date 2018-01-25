# Imports screen.py
import screen
# Imports random library
import random

# Stores the secret code using numbers to represent colors
# 0 = red, 1 = orange, 2 = yellow, 3 = green
# 4 = blue, 5 = violet, 6 = gray
SECRET_CODE = [0, 0, 0, 0]

# Stores the hints for the current guess
CURRENT_HINTS = []

# Stores the count of guesses the player has used
CURRENT_GUESS = 0

# Constant for how long the countdown timer should be
TIMER_LENGTH = 15.0

# Stores whether the game is over yet and whether the player won or not
GAME_OVER = False
GAME_WON = False


# Setups the game for the player
def setup():
    global SECRET_CODE

    # Generates a random color code for each index of the secret code
    for x in range(4):
        SECRET_CODE[x] = random.randint(0, 6)

    # Prints the secret code using the integer color codes (commented out)
    # print("Code: ", SECRET_CODE)


# Handles the players current inputted guess
def handle_guess(color0, color1, color2, color3):
    global CURRENT_GUESS
    global CURRENT_HINTS
    global GAME_OVER
    global GAME_WON

    # Stores the secret code temporarily to be manipulated
    # during hint checking
    temp_secret_code = []
    for x in range(len(SECRET_CODE)):
        temp_secret_code.append(SECRET_CODE[x])

    # Checks if the player has any guesses left
    if CURRENT_GUESS < 10:
        # Displays the players guess in the proper guess row
        screen.edit_guess(CURRENT_GUESS, 0, color0)
        screen.edit_guess(CURRENT_GUESS, 1, color1)
        screen.edit_guess(CURRENT_GUESS, 2, color2)
        screen.edit_guess(CURRENT_GUESS, 3, color3)

        # Resets the colors shown in the selection boxes to default (red)
        screen.reset_choice_colors()

        # Increments their guess count by 1
        CURRENT_GUESS += 1

        # Checks for correct color, correct spot for each guessed color
        # within the secret code and adds the corresponding hint
        # to the current hints list
        if color0 == temp_secret_code[0]:
            CURRENT_HINTS.append(2)
            color0 = -1
            temp_secret_code[0] = -1
        if color1 == temp_secret_code[1]:
            CURRENT_HINTS.append(2)
            color1 = -1
            temp_secret_code[1] = -1
        if color2 == temp_secret_code[2]:
            CURRENT_HINTS.append(2)
            color2 = -1
            temp_secret_code[2] = -1
        if color3 == temp_secret_code[3]:
            CURRENT_HINTS.append(2)
            color3 = -1
            temp_secret_code[3] = -1

        # Checks for correct color, wrong spot for each guessed color
        # within the secret code and adds the corresponding hint
        # to the current hints list
        if color0 != -1:
            if color0 in temp_secret_code:
                CURRENT_HINTS.append(1)
                temp_secret_code[temp_secret_code.index(color0)] = -1
            else:
                CURRENT_HINTS.append(0)
        if color1 != -1:
            if color1 in temp_secret_code:
                CURRENT_HINTS.append(1)
                temp_secret_code[temp_secret_code.index(color1)] = -1
            else:
                CURRENT_HINTS.append(0)
        if color2 != -1:
            if color2 in temp_secret_code:
                CURRENT_HINTS.append(1)
                temp_secret_code[temp_secret_code.index(color2)] = -1
            else:
                CURRENT_HINTS.append(0)
        if color3 != -1:
            if color3 in temp_secret_code:
                CURRENT_HINTS.append(1)
                temp_secret_code[temp_secret_code.index(color3)] = -1
            else:
                CURRENT_HINTS.append(0)

        # Sorts the current hints to show red dots first, white dots
        # second and blank dots third
        CURRENT_HINTS.sort(reverse=True)

        # Displays the hints on-screen
        screen.edit_hints(CURRENT_HINTS, CURRENT_GUESS)

        # Checks if the player has guessed the correct code
        if CURRENT_HINTS == [2, 2, 2, 2]:
            GAME_OVER = True
            GAME_WON = True
        # Checks if the play is out of guesses
        elif CURRENT_GUESS == 10:
            GAME_OVER = True

        # Clears current hints for the next guess
        CURRENT_HINTS = []
