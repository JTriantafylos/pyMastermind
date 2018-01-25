# Imports the terminal module from bearlibterminal
from bearlibterminal import terminal
# Imports screen.py
import screen
# Imports input.py
import input
# Imports game.py
import game
# Imports time library
import time

# Opens a bearlibterminal terminal instance
terminal.open()

# Sets terminal title, size, font and font size
terminal.set("window: title='pyMastermind', size=24x18")
terminal.set("font: font/DejaVuSansMono.ttf, size=11")

# Shows the rules and welcome screen
for x in range(4):
    screen.show_welcome_screen(x)
    while terminal.read() != terminal.TK_ENTER:
        pass

# Calls for the terminal screen to be setup
screen.setup()

# Setups the game variables (i.e the secret code)
game.setup()

# Constantly listens for input and refreshes the screen 30 times a second
while not game.GAME_OVER:
    if terminal.has_input():
        input.handle(terminal.read())

    terminal.refresh()
    time.sleep(1 / 30)

# Checks if the player has won or not
if game.GAME_WON:
    # Waits 2 seconds and then shows win message
    time.sleep(2)
    screen.show_win_screen()
    terminal.refresh()

    # Waits for the user to press escape or the close button to end
    if terminal.read() == terminal.TK_ENTER or \
       terminal.read() == terminal.TK_CLOSE:
        quit()
else:
    # Waits 2 seconds and then shows lose message
    time.sleep(2)
    screen.show_lose_screen()
    terminal.refresh()

    # Waits for the user to press escape or the close button to end
    if terminal.read() == terminal.TK_ENTER or \
       terminal.read() == terminal.TK_CLOSE:
        quit()
