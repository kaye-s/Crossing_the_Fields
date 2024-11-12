from bedroom import *
from commands import *

#Setup
#   creating the first instance of Demon, this will be passed to each function to take the player to the next location
#   Setting default avail commands to empty list.
demon = Demon()
demon.avail_commands(AvailCommands())

#Level 1 - Prologue, Escape Demon's bedroom
demon = run_bedroom(demon)

