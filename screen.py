# Imports the terminal module from bearlibterminal
from bearlibterminal import terminal
# Imports input.py
import input
# Imports game.py
import game


# Setup of the terminal
def setup():
    # Clears the terminal screen
    terminal.clear()

    # Prints the title and author in the top two rows of terminal
    terminal.printf(6, 0, "pyMastermind")
    terminal.printf(7, 1, "By James T")

    # Prints the guess display boxes (Doubled brackets since
    # they are special characters)
    terminal.printf(2, 3, "[[ ]] [[ ]] [[ ]] [[ ]] [U+25CB][U+25CB][U+25CB][U+25CB]")
    terminal.printf(2, 4, "[[ ]] [[ ]] [[ ]] [[ ]] [U+25CB][U+25CB][U+25CB][U+25CB]")
    terminal.printf(2, 5, "[[ ]] [[ ]] [[ ]] [[ ]] [U+25CB][U+25CB][U+25CB][U+25CB]")
    terminal.printf(2, 6, "[[ ]] [[ ]] [[ ]] [[ ]] [U+25CB][U+25CB][U+25CB][U+25CB]")
    terminal.printf(2, 7, "[[ ]] [[ ]] [[ ]] [[ ]] [U+25CB][U+25CB][U+25CB][U+25CB]")
    terminal.printf(2, 8, "[[ ]] [[ ]] [[ ]] [[ ]] [U+25CB][U+25CB][U+25CB][U+25CB]")
    terminal.printf(2, 9, "[[ ]] [[ ]] [[ ]] [[ ]] [U+25CB][U+25CB][U+25CB][U+25CB]")
    terminal.printf(2, 10, "[[ ]] [[ ]] [[ ]] [[ ]] [U+25CB][U+25CB][U+25CB][U+25CB]")
    terminal.printf(2, 11, "[[ ]] [[ ]] [[ ]] [[ ]] [U+25CB][U+25CB][U+25CB][U+25CB]")
    terminal.printf(2, 12, "[[ ]] [[ ]] [[ ]] [[ ]] [U+25CB][U+25CB][U+25CB][U+25CB]")

    # Prints the selection boxes
    terminal.printf(2, 14, "[color=azure][[ ]][color=white] [[ ]] [[ ]] [[ ]]")

    # Puts the initial color guesses in the selection boxes
    for index in range(4):
        edit_choice_color(index, 0)

    # Shows the default timer value
    print_timer_display(game.TIMER_LENGTH)

    # Refreshes the terminal (i.e makes everything show up)
    terminal.refresh()


# Edits a guess display dot in a specific row at a specific index
# row goes 0-9
# index goes 0-3
# Color goes 0-6
# 0 = red, 1 = orange, 2 = yellow, 3 = green
# 4 = blue, 5 = violet, 6 = gray
def edit_guess(row, index, color):
    # Corrects the index to the absolute x position
    if index == 0:
        index = 3
    elif index == 1:
        index = 7
    elif index == 2:
        index = 11
    elif index == 3:
        index = 15

    # Handles different color choices and prints the colored dot
    # Adds 3 to row value to correct for space taken up by game title
    if color == 0:
        terminal.printf(index, row + 3, "[color=red][U+25CF]")
    elif color == 1:
        terminal.printf(index, row + 3, "[color=orange][U+25CF]")
    elif color == 2:
        terminal.printf(index, row + 3, "[color=yellow][U+25CF]")
    elif color == 3:
        terminal.printf(index, row + 3, "[color=green][U+25CF]")
    elif color == 4:
        terminal.printf(index, row + 3, "[color=azure][U+25CF]")
    elif color == 5:
        terminal.printf(index, row + 3, "[color=violet][U+25CF]")
    elif color == 6:
        terminal.printf(index, row + 3, "[color=gray][U+25CF]")


# Edits the hints for the current guess
# 0 = no match
# 1 = right color, wrong spot
# 2 = right color, right spot
def edit_hints(hints, current_guess):
    # Corrects values for proper positioning
    index = [18, 19, 20, 21]
    current_guess += 2

    # Iterates through the current hint list and draws the
    # corresponding hints to the screen
    for x in range(len(hints)):
        if hints[x] == 2:
            terminal.printf(index[x], current_guess, "[color=red][U+25CF]")
        elif hints[x] == 1:
            terminal.printf(index[x], current_guess, "[color=white][U+25CF]")
        else:
            terminal.printf(index[x], current_guess, "[U+25CB]")


# Edits the selection row colors
# index goes 0-3
# Color goes 0-6
# 0 = red, 1 = orange, 2 = yellow, 3 = green
# 4 = blue, 5 = violet, 6 = gray
def edit_choice_color(index, color):
    # Corrects the index to the absolute x position
    if index == 0:
        index = 3
    elif index == 1:
        index = 7
    elif index == 2:
        index = 11
    elif index == 3:
        index = 15

    if color == 0:
        terminal.printf(index, 14, "[color=red][U+25CF]")
    elif color == 1:
        terminal.printf(index, 14, "[color=orange][U+25CF]")
    elif color == 2:
        terminal.printf(index, 14, "[color=yellow][U+25CF]")
    elif color == 3:
        terminal.printf(index, 14, "[color=green][U+25CF]")
    elif color == 4:
        terminal.printf(index, 14, "[color=azure][U+25CF]")
    elif color == 5:
        terminal.printf(index, 14, "[color=violet][U+25CF]")
    elif color == 6:
        terminal.printf(index, 14, "[color=gray][U+25CF]")


# Edits which selection box the user is currently hovering over
def edit_choice_box(index):
    if index == 0:
        # Prints the selection boxes
        terminal.printf(2, 14, "[color=azure][[ ]][color=white] [[ ]] [[ ]] [[ ]]")
    elif index == 1:
        # Prints the selection boxes
        terminal.printf(2, 14, "[[ ]] [color=azure][[ ]][color=white] [[ ]] [[ ]]")
    elif index == 2:
        # Prints the selection boxes
        terminal.printf(2, 14, "[[ ]] [[ ]] [color=azure][[ ]][color=white] [[ ]]")
    elif index == 3:
        # Prints the selection boxes
        terminal.printf(2, 14, "[[ ]] [[ ]] [[ ]] [color=azure][[ ]][color=white]")

    # Redraws the players color guesses
    edit_choice_color(0, input.SELECT_COLOR_0)
    edit_choice_color(1, input.SELECT_COLOR_1)
    edit_choice_color(2, input.SELECT_COLOR_2)
    edit_choice_color(3, input.SELECT_COLOR_3)


# Resets the color choices to defaults (red)
def reset_choice_colors():
    for index in range(4):
        edit_choice_color(index, 0)

    input.SELECT_COLOR_0 = 0
    input.SELECT_COLOR_1 = 0
    input.SELECT_COLOR_2 = 0
    input.SELECT_COLOR_3 = 0


# Prints the guess timer to the screen
def print_timer_display(time):
    time = str(round(time, 1))
    terminal.printf(18, 14, time)


# Shows the welcome message
def show_welcome_screen(part):
    # Clears the screen
    terminal.clear()

    if part == 0:
        # Prints instructions (part 1)
        terminal.printf(6, 1, "[color=black][bkcolor=white] Welcome to ")
        terminal.printf(6, 2, "[color=black][bkcolor=white] Mastermind ")
        terminal.printf(4, 4, "[color=black][bkcolor=white] The goal is to ")
        terminal.printf(3, 5, "[color=black][bkcolor=white] guess the random ")
        terminal.printf(5, 6, "[color=black][bkcolor=white] color  combo ")
        terminal.printf(4, 7, "[color=black][bkcolor=white] by using hints ")
        terminal.printf(5, 8, "[color=black][bkcolor=white] given to you ")
        terminal.printf(3, 9, "[color=black][bkcolor=white] via colored dots ")
        terminal.printf(6, 10, "[color=black][bkcolor=white] like these ")
        terminal.printf(6, 11, "[color=black][bkcolor=white] ---------- ")
        terminal.printf(8, 12, "[bkcolor=black][color=red][U+25CF] "
                               "[color=white][U+25CB]  "
                               "[U+25CB] "
                               "[color=white][U+25CF]")

        terminal.printf(5, 15, "[color=black][bkcolor=white] Press  enter ")
        terminal.printf(4, 16, "[color=black][bkcolor=white] to continue... ")

        # Refreshes the screen
        terminal.refresh()
    elif part == 1:
        # Prints instructions (part 2)
        terminal.printf(7, 2, "[color=black][bkcolor=white] Red dots ")
        terminal.printf(5, 3, "[color=black][bkcolor=white] mean correct ")
        terminal.printf(4, 4, "[color=black][bkcolor=white] color, correct ")
        terminal.printf(3, 5, "[color=black][bkcolor=white] spot. White dots ")
        terminal.printf(5, 6, "[color=black][bkcolor=white] mean correct ")
        terminal.printf(5, 7, "[color=black][bkcolor=white] color, wrong ")
        terminal.printf(3, 8, "[color=black][bkcolor=white] spot. Empty dots ")
        terminal.printf(6, 9, "[color=black][bkcolor=white] mean wrong ")
        terminal.printf(5, 10, "[color=black][bkcolor=white] color, wrong ")
        terminal.printf(9, 11, "[color=black][bkcolor=white] spot ")

        terminal.printf(5, 15, "[color=black][bkcolor=white] Press  enter ")
        terminal.printf(4, 16, "[color=black][bkcolor=white] to continue... ")

        # Refreshes the screen
        terminal.refresh()
    elif part == 2:
        # Prints instructions (part 3)
        terminal.printf(5, 3, "[color=black][bkcolor=white] You will get ")
        terminal.printf(6, 4, "[color=black][bkcolor=white] 10 guesses ")
        terminal.printf(3, 5, "[color=black][bkcolor=white] and you will get ")
        terminal.printf(6, 6, "[color=black][bkcolor=white] 15 seconds ")
        terminal.printf(4, 7, "[color=black][bkcolor=white] to input  each ")
        terminal.printf(5, 8, "[color=black][bkcolor=white] guess before ")
        terminal.printf(4, 9, "[color=black][bkcolor=white] it is inputted ")
        terminal.printf(7, 10, "[color=black][bkcolor=white] for  you ")

        terminal.printf(5, 15, "[color=black][bkcolor=white] Press  enter ")
        terminal.printf(4, 16, "[color=black][bkcolor=white] to continue... ")

        # Refreshes the screen
        terminal.refresh()
    else:
        # Prints instructions (part 4)
        terminal.printf(4, 3, "[color=black][bkcolor=white] Use the Up and ")
        terminal.printf(4, 4, "[color=black][bkcolor=white] Down arrowkeys ")
        terminal.printf(4, 5, "[color=black][bkcolor=white] to change your ")
        terminal.printf(3, 6, "[color=black][bkcolor=white] selected  color, ")
        terminal.printf(3, 7, "[color=black][bkcolor=white] use the Left and ")
        terminal.printf(3, 8, "[color=black][bkcolor=white] Right  arrowkeys ")
        terminal.printf(4, 9, "[color=black][bkcolor=white] to switch your ")
        terminal.printf(5, 10, "[color=black][bkcolor=white] selected box ")

        terminal.printf(5, 15, "[color=black][bkcolor=white] Press  enter ")
        terminal.printf(3, 16, "[color=black][bkcolor=white] to begin game... ")

        # Refreshes the screen
        terminal.refresh()


# Shows the player a win message
def show_win_screen():
    # Clears the screen
    terminal.clear()

    # Prints win message
    terminal.printf(7, 6, "[color=black][bkcolor=white] You Win! ")
    terminal.printf(5, 7, "[color=black][bkcolor=white] Press  enter ")
    terminal.printf(3, 8, "[color=black][bkcolor=white] to exit game.... ")


# Shows the player a lose message
def show_lose_screen():
    # Clears the screen
    terminal.clear()

    # Prints lose message
    terminal.printf(6, 6, "[color=black][bkcolor=white] You  Lose! ")
    terminal.printf(5, 7, "[color=black][bkcolor=white] Press  enter ")
    terminal.printf(3, 8, "[color=black][bkcolor=white] to exit game.... ")
