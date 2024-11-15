from bedroom import Bedroom, run_bedroom
from commands import comp_str, Demon, AvailCommands
from trailerpark import run_trailer

#Setup
#   creating the first instance of Demon, this will be passed to each function to take the player to the next location
#   Setting default avail commands to empty list.
demon = Demon()
demon.avail_commands(AvailCommands())



print("-----------------------------------------------------------------------------------------------------------")
print("Hello! Thank you for testing my game. To play the game as intended please just hit enter and enjoy.\nIf you are "
      "coming back to try a new level type the secret password 'rehab' to see the level select")
level = input()
if level == "rehab":
    print("Welcome back! Here are the currently available levels:\n\tLevel 0: Bedroom (0)\n\tLevel 1: Trailer (1)\nPlease "
          "select the level you wish to play (Type the number in parenthesis next to the chosen level)")
    choice = input()
    if choice == "0":
        demon = run_bedroom(demon)
    elif choice == "1":
        demon = run_trailer(demon)
else:
    # Level 0 - Prologue, Escape Demon's bedroom
    demon = run_bedroom(demon)

    # Level 1 - Save Mom in the Trailer Park
    demon = run_trailer(demon)

