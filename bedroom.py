from commands import *

class Bedroom:
    def __init__(self, demon):
        self.demon = demon
        self.items = {
            'sketchbook': True,
            'markers': True,
            'screwdriver': True,
            'key': True
        }
        self.window_is_open = False
        self.is_drawer_unlocked = False

    # start/hub, avail commands are:
    #   w, a, s, d
    # returns string
    def start(self):
        print("In front of you is your desk\n To the left is a window\n To the right is a door\n Your bed is behind you")
        self.demon.ac.set_commands(["w", "a", "s", "d", "i"])

        while True:
            command = self.demon.user_val()
            print("")
            if command == "i":
                self.demon.print_inventory()
            # if w, goTo desk
            return {
                "w": "desk",
                "a": "window",
                "s": "bed",
                "d": "door"
            }.get(command, "start")

    #desk helper methods:
    def locked_drawer_response(self):
        print("Drawer is locked\n")
        return "desk"

    def use_key(self):
        if "key" in self.demon.inventory:
            print("Drawer is unlocked")
            self.is_drawer_unlocked = True
        else:
            print("You don't have a key")

    # desk, avail commands are:
    #   s
    #   grab + sketchbook
    #   open + drawer
    #   unlock + drawer
    def desk(self):
        print("This is your desk")
        print("There is a drawer with a keyhole")

        if self.items['sketchbook']:
            print("On top of the desk is a sketchbook")

        self.demon.ac.set_commands(["s", "grab sketchbook", "open drawer", "use key", "i"])
        while True:
            command = self.demon.user_val()
            print("")

            if command == "i":
                self.demon.print_inventory()

            # if s, goTo start
            elif command == "s":
                return "start"

            # if grab + sketchbook
            # add sketchbook to inventory - sketchbook false
            elif command == "grab sketchbook":
                print("You pick up the sketchbook")
                self.demon.add_to_inventory("sketchbook")
                self.items['sketchbook'] = False

            elif command == "open drawer":
                return "drawer" if self.is_drawer_unlocked else self.locked_drawer_response()
            elif command == "use key":
                self.use_key()
            print("")

    #drawer, avail commands are:
    #   s
    #   grab + markers
    #   grab + screwdriver
    def drawer(self):
        print("You opened the drawer")
        if self.items['markers']:
            print("\tThere is a pack of markers")
        if self.items['screwdriver']:
            print("\tThere is a screwdriver")

        self.demon.ac.set_commands(["s", "grab markers", "grab screwdriver", "i"])
        while True:
            command = self.demon.user_val()
            print("")

            if command == "i":
                self.demon.print_inventory()

            #if s, goTo desk
            elif command == "s":
                return "desk"


            elif command == "grab markers":
                print("You pick up the markers")
                self.demon.add_to_inventory("markers")
                self.items['markers'] = False

            elif command == "grab screwdriver":
                print("You pick up the screwdriver")
                self.demon.add_to_inventory("screwdriver")
                self.items['screwdriver'] = False
            print("")

    #window helper method:
    def use_screwdriver(self):
        if "screwdriver" in self.demon.inventory:
            print("You pry open the window")
            self.window_is_open = True
        else:
            print("You don't have a screwdriver")
    #window: avail commands are:
    #   open + window
    #   look
    #   s
    #   use + screwdriver
    #   exit/w
    def window(self):
        print("You are at the window")

        self.demon.ac.set_commands(["s", "i", "use screwdriver", "open window", "look out", "w", "escape"])
        while True:
            command = self.demon.user_val()
            print("")

            if command == "i":
                self.demon.print_inventory()

            elif command == "s":
                return "start"
            elif command == "use screwdriver":
                self.use_screwdriver()
            elif command == "open window":
                print("The window seems to be stuck, if only you had something to pry it open")
            elif command in ["escape", "w"] and self.window_is_open:
                print("You escape through the window")
                return "complete"
            elif command == "look out":
                print("You look out the window. In front of the window you see a dog cage. Beyond that, the Peggot trailer.")
                print("Further in the distance you see a creek")
            print("")

    #window: avail commands are:
    #   lie down
    #   s
    #   look under
    def bed(self):
        print("This is your bed")
        if self.items['key']:
            print("It looks like something might be under it")

        self.demon.ac.set_commands(["s", "i", "look under"])
        while True:
            command = self.demon.user_val()
            print("")

            if command == "i":
                self.demon.print_inventory()

            # if s, goTo start
            elif command == "s":
                return "start"
            elif command == "look under":
                return "underBed"
            print("")

    def underBed(self):
        print("Under the bed")
        if self.items['key']:
            print("There is a small key lying in a pile of dust")

        self.demon.ac.set_commands(["s", "i", "grab key"])
        while True:
            command = self.demon.user_val()
            print("")

            if command == "i":
                self.demon.print_inventory()

            if command == "grab key":
                print("You picked up the key")
                self.items['key'] = False
                self.demon.add_to_inventory("key")
            if command == "s":
                return "bed"
            print("")


    #door: avail commands are:
    #   open door
    #   s
    def door(self):
        print("You are in front of the door.")

        self.demon.ac.set_commands(["s", "i", "open door", "use key", "use screwdriver"])
        while True:
            command = self.demon.user_val()
            print("")

            if command == "i":
                self.demon.print_inventory()
            elif command == "s":
                return "start"
            elif command == "open door":
                print("The door is locked")
            elif command == "use key" and "key" in self.demon.inventory:
                print("You try the key on the door but it doesn't fit")
            elif command == "use screwdriver" and "screwdriver" in self.demon.inventory:
                print("You try to fit the screwdriver in the lock and wiggle it around but it doesn't seem to do anything. \nIf you knew anything about lock picking you would know that wouldn't work")
            print("")

def run_bedroom(demon):
    bedroom = Bedroom(demon)
    print("You wake up in your childhood bedroom.\n Hint: try \n\tw \ta \ts \td : to move \n\ti : to view inventory")
    print("Every command is one or two words, learn what you can do in each area. \n\tYour goal is simple: Escape\n")

    move = bedroom.start()
    while move != "complete":
        move = {
            "start": bedroom.start,
            "desk": bedroom.desk,
            "window": bedroom.window,
            "bed": bedroom.bed,
            "door": bedroom.door,
            "drawer": bedroom.drawer,
            "underBed": bedroom.underBed
        }.get(move, lambda: move)()

    print("Congratulations, you completed level 1! Come back later for level 2.")
    return demon
