# Imports the terminal module from bearlibterminal
from bearlibterminal import terminal
# Imports keyboard library
import keyboard
# Imports screen.py
import screen
# Imports game.py
import game
# Imports threading library
from threading import Thread, Timer
# imports time library
import time

# Global variables to handle color selection
SELECT_BOX = 0
SELECT_COLOR_0 = 0
SELECT_COLOR_1 = 0
SELECT_COLOR_2 = 0
SELECT_COLOR_3 = 0

# Stores whether the timer is currently counting down
COUNTING_DOWN = False


# Submits the currently inputted guess
def timer_submit():
    global COUNTING_DOWN
    COUNTING_DOWN = False

    # Simulates a press of the enter key
    keyboard.press_and_release('enter')


# Creates a timer object that submits the users guess after
# a period of time
timer = Timer(game.TIMER_LENGTH, timer_submit)


# Function to be ran in a thread to display the countdown timer
def timer_display_start():
    for x in range(150):
        if COUNTING_DOWN:
            screen.print_timer_display(game.TIMER_LENGTH - (x / 10))
            time.sleep(0.1)
        else:
            break


# Handles all terminal inputs
def handle(key):
    global SELECT_BOX
    global SELECT_COLOR_0
    global SELECT_COLOR_1
    global SELECT_COLOR_2
    global SELECT_COLOR_3
    global COUNTING_DOWN

    # Checks if the timer is currently counting down
    if not COUNTING_DOWN:
        # Checks for input to start timer
        if key == terminal.TK_LEFT or \
           key == terminal.TK_RIGHT or \
           key == terminal.TK_UP or \
           key == terminal.TK_DOWN:
            COUNTING_DOWN = True
            timer_thread()
    # Handles escape press and close button press
    if key == terminal.TK_CLOSE or key == terminal.TK_ESCAPE:
        quit()

    # Handles arrow key presses
    elif key == terminal.TK_LEFT:
        # Changes selected box to be one to the left
        if SELECT_BOX > 0:
            SELECT_BOX -= 1
            screen.edit_choice_box(SELECT_BOX)
    elif key == terminal.TK_RIGHT:
        # Changes selected box to be one to the right
        if SELECT_BOX < 3:
            SELECT_BOX += 1
            screen.edit_choice_box(SELECT_BOX)
    elif key == terminal.TK_UP:
        # Changes the selected boxes color choice up by one
        if SELECT_BOX == 0:
            if SELECT_COLOR_0 > 0:
                SELECT_COLOR_0 -= 1
                screen.edit_choice_color(0, SELECT_COLOR_0)
        elif SELECT_BOX == 1:
            if SELECT_COLOR_1 > 0:
                SELECT_COLOR_1 -= 1
                screen.edit_choice_color(1, SELECT_COLOR_1)
        elif SELECT_BOX == 2:
            if SELECT_COLOR_2 > 0:
                SELECT_COLOR_2 -= 1
                screen.edit_choice_color(2, SELECT_COLOR_2)
        elif SELECT_BOX == 3:
            if SELECT_COLOR_3 > 0:
                SELECT_COLOR_3 -= 1
                screen.edit_choice_color(3, SELECT_COLOR_3)
    elif key == terminal.TK_DOWN:
        # Changes the selected boxes color choice down by one
        if SELECT_BOX == 0:
            if SELECT_COLOR_0 < 6:
                SELECT_COLOR_0 += 1
                screen.edit_choice_color(0, SELECT_COLOR_0)
        elif SELECT_BOX == 1:
            if SELECT_COLOR_1 < 6:
                SELECT_COLOR_1 += 1
                screen.edit_choice_color(1, SELECT_COLOR_1)
        elif SELECT_BOX == 2:
            if SELECT_COLOR_2 < 6:
                SELECT_COLOR_2 += 1
                screen.edit_choice_color(2, SELECT_COLOR_2)
        elif SELECT_BOX == 3:
            if SELECT_COLOR_3 < 6:
                SELECT_COLOR_3 += 1
                screen.edit_choice_color(3, SELECT_COLOR_3)

    # Submits the players guess and checks it against the secret code
    elif key == terminal.TK_ENTER:
        COUNTING_DOWN = False
        # Cancels the timer if it is currently counting down
        timer.cancel()
        # Handles the users submitted guess
        game.handle_guess(SELECT_COLOR_0, SELECT_COLOR_1,
                          SELECT_COLOR_2, SELECT_COLOR_3)

        # Resets the timer countdown display
        screen.print_timer_display(game.TIMER_LENGTH)


# Thread function to run the input countdown
def timer_thread():
    # Creates and starts a timer that submits the users guess
    # after a set amount of time
    global timer
    timer = Timer(game.TIMER_LENGTH, timer_submit)
    timer.start()

    # Creates and starts a thread that will run the timer countdown display
    timer_display_thread = Thread(target=timer_display_start, args=())
    timer_display_thread.daemon = True
    timer_display_thread.start()