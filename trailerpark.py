import time


class TrailerPark:
    def __init__(self, demon):
        self.demon = demon
        self.items = {
            'gun': True,
            'rabbit': True,
            'dog': True,
            'bullet': True,
        }
        self.trap_open = False
        self.shot_rabbit = False
        self.isFed = False
        self.satan = False


    def start(self):
        print(
            "You are at the base of the hill, climbing up the hill in front of you will take you back to the "
            "trailers\nBehind you is the forest edge")
        self.demon.ac.set_commands(["w", "s", "i", "load gun"])

        while True:
            command = self.demon.user_val()
            print("")
            if command == "i":
                self.demon.print_inventory()
            elif command == "load gun" or command == "load rifle":
                self.load_gun()
            return {
                "w": "trailers",
                "s": "forest",
            }.get(command, "start")

    def trailers(self):
        print("To your left is the Peggot trailer, \nIn front is the dog cage, \nTo the right is your trailer")

        self.demon.ac.set_commands(["w", "a", "d", "s", "i", "load gun"])
        while True:
            command = self.demon.user_val()
            print("")

            if command == "i":
                self.demon.print_inventory()
            elif command == "load gun" or command == "load rifle":
                self.load_gun()

            # movement commands
            elif command == "s":
                return "start"
            elif command == "w":
                return "dog_cage"
            elif command == "a":
                return "peggot"
            elif command == "d":
                return "porch"

            print("")

    def dog_cage(self):
        if self.items['dog']:
            print("You approach the dog cage, it seems Stoner forgot to feed Satan again, he is snarling at you aggressively. \nYou probably shouldn't open the cage unless you can feed him first.")
        else:
            print("An empty dog cage")
        self.demon.ac.set_commands(["s", "i", "feed Satan", "open cage", "load gun", "feed satan", "feed dog", "use rabbit"])
        while True:
            command = self.demon.user_val()
            print("")

            if command == "i":
                self.demon.print_inventory()

            elif command == "load gun" or command == "load rifle":
                self.load_gun()

            # movement commands
            elif command == "s":
                return "trailers"

            elif (command == "feed dog" or command == "feed Satan" or command == "feed satan" or command == "use rabbit") and "dead rabbit" in self.demon.inventory:
                print("You give Satan the dead rabbit, he graciously eats the meat. It should be safe to open the cage now")
                self.isFed = True
            elif (command == "feed dog" or command == "feed Satan" or command == "feed satan") and "dead rabbit" not in self.demon.inventory:
                print("You have nothing to feed him")
            elif command == "open cage" and self.isFed:
                print("You let Satan out of the cage, it seems like he will follow you")
                self.items['dog'] = False
                self.satan = True
            elif command == "open cage" and not self.isFed:
                print("Against your better judgment you open the cage.")
                time.sleep(3)
                print("The anger in Satan's eyes is the last thing you see before he bites your neck")
                return "complete"
            print("")

    def peggot(self):
        print("You are in front of the Peggot trailer. You have many fond memories of this place")

        self.demon.ac.set_commands(["s", "i", "grab gun", "grab rifle", "load gun"])

        if self.items['gun']:
            print(
                "Laying next to the door is Mr. Peg's rifle. This is odd because he often kept it with him. \nWhere were the Peggot's anyways?")
        while True:
            command = self.demon.user_val()
            print("")

            if command == "i":
                self.demon.print_inventory()

            elif command == "load gun" or command == "load rifle":
                self.load_gun()

            # movement commands
            elif command == "s":
                return "trailers"
            elif command == "grab gun" or command == "grab rifle":
                print("You grab the gun")
                self.demon.add_to_inventory("gun")
                self.items['gun'] = False

            print("")

    def porch(self):
        print("The porch of your trailer, you hear yelling inside. \nBetter not enter until you're ready to deal with Stoner \n[WARNING: Once you enter the trailer you cannot go back]")

        self.demon.ac.set_commands(["w", "enter", "s", "i", "load gun"])
        while True:
            command = self.demon.user_val()
            print("")

            if command == "i":
                self.demon.print_inventory()
            elif command == "load gun" or command == "load rifle":
                self.load_gun()

            # movement commands
            elif command == "s":
                return "trailers"
            elif command == "w" or command == "enter":
                return "home"

            print("")

    def forest(self):
        print("The forest edge.\nTo the left is the creek, \nTo the right is the woods")

        self.demon.ac.set_commands(["a", "d", "s", "i", "load gun"])
        while True:
            command = self.demon.user_val()
            print("")

            if command == "i":
                self.demon.print_inventory()
            elif command == "load gun" or command == "load rifle":
                self.load_gun()

            # movement commands
            elif command == "s":
                return "start"
            elif command == "a":
                return "creek"
            elif command == "d":
                return "woods"

            print("")

    def creek(self):
        print("In front of you is a small creek. You spent many hours playing here with Maggot. The rushing water is very calming.")

        self.demon.ac.set_commands(["s", "i", "grab bullet", "load gun", "jump in", "swim"])

        if self.items['bullet']:
            print("On the creek bed you find a single bullet. It must've dropped from the last hunters in this area. Looks like the kind Mr. Peg would use")

        while True:
            command = self.demon.user_val()
            print("")

            if command == "i":
                self.demon.print_inventory()
            elif command == "load gun":
                self.load_gun()

            # movement commands
            elif command == "s":
                return "forest"
            elif command == "grab bullet":
                print("You grab the bullet")
                self.demon.add_to_inventory("bullet")
                self.items['bullet'] = False
            elif command == "jump in" or command == "swim":
                print("You wade into the creek. You don't remember it being this deep. If this was reality the water wouldn't reach above your knees.")
                time.sleep(2)
                print("Here, you are not so lucky")
                time.sleep(2)
                return "complete"

            print("")
    def load_gun(self):
        if "gun" in self.demon.inventory and "bullet" in self.demon.inventory:
            self.demon.add_to_inventory("loaded gun")
            self.demon.remove_from_inventory("gun")
            self.demon.remove_from_inventory("bullet")
            print("You now have a loaded gun")
            self.demon.print_inventory()
        elif "gun" not in self.demon.inventory:
            print("What gun?")
        elif "bullet" not in self.demon.inventory:
            print("You have nothing to put in it")

    def use_gun(self):
        if not self.items['rabbit']:
            print("There is nothing to use it on")
        elif "gun" in self.demon.inventory:
            print("You need to load the gun first")
        elif "loaded gun" in self.demon.inventory:
            print("Remembering what Mr. Peg showed you, you shoot the rabbit. You should be able to open the trap now")
            self.shot_rabbit = True
            self.demon.remove_from_inventory("loaded gun")
            self.demon.add_to_inventory("gun")

    def woods(self):
        print("You enter the woods. Following the well worn path you make your way into a clearing. You remember Mr. Peg taking you and Maggot out here to hunt")

        self.demon.ac.set_commands(["s", "i", "load gun", "use gun", "shoot gun", "open trap", "grab rabbit", "shoot rabbit", "kill rabbit"])
        if self.items['rabbit']:
            print(
                "Next to the bushes there is an animal trap with a rabbit caught inside, his leg is obviously broken and he is still struggling. It is a pitiful sight.")
        while True:
            command = self.demon.user_val()
            print("")

            if command == "i":
                self.demon.print_inventory()

            # movement commands
            elif command == "s":
                return "forest"

            elif command == "load gun":
                self.load_gun()
            elif command == "use gun" or command == "shoot gun" or command == "shoot rabbit" or command == "kill rabbit":
                self.use_gun()
            elif command == "open trap" and self.shot_rabbit:
                print("The rabbit is not struggling anymore, you open the trap with ease")
                self.trap_open = True
            elif command == "open trap" and not self.shot_rabbit:
                print("The rabbit limps away")
                self.items['rabbit'] = False

            elif command == "grab rabbit":
                if not self.trap_open:
                    print("The trap is closed, if you open it now the rabbit will probably escape")
                else:
                    print("You pick up the dead rabbit")
                    self.demon.add_to_inventory("dead rabbit")

            print("")

    def home(self):

        if self.satan:
            print("You enter the trailer, inside you see Stoner blocking the entrance to Mom's bedroom.")
            time.sleep(3)
            print("You hear Satan growling behind you.")
            time.sleep(3)
            print("You look into Stoner's face but it's blurry, you can't remember exactly what he looks like.")
            time.sleep(3)
            print("It has been a while since you've seen him.")
            time.sleep(3)
            print("You look down and see pills scattered on the ground.")
            time.sleep(3)
            print("You didn't recognize them before but now the oxy is unmistakable.")
            time.sleep(3)
            print("Suddenly, Satan rushes forward and attacks Stoner.")
            time.sleep(3)
            print("You waste no time running into the bedroom as Stoner struggles with the dog.")
            time.sleep(3)
            print("Mom is immobile on the bed.")
            time.sleep(3)
            print("Rushing to her side you try to think of some way to help her.")
            time.sleep(3)
            print("Just like before there is nothing you can do.")
            time.sleep(3)
            print("After all, you can't change what has already happened.")
            time.sleep(3)
        elif "loaded gun" in self.demon.inventory:
            print("You enter the trailer, inside you see Stoner blocking the entrance to Mom's bedroom.")
            time.sleep(3)
            print("You look into Stoner's face but it's blurry, you can't remember exactly what he looks like.")
            time.sleep(3)
            print("It has been a while since you've seen him.")
            time.sleep(3)
            print("But it's different now.")
            time.sleep(3)
            print("You didn't have a gun last time.")
            time.sleep(3)
            print("You raise the rifle to the place where Stoner's face should be.")
            time.sleep(3)
            print("Closing your eyes you pull the trigger.")
            time.sleep(3)
            print("When you open them, you see someone lying in a pool of blood.")
            time.sleep(3)
            print("But it isn't Stoner.")
            time.sleep(3)
        else:
            print("You enter the trailer, inside you see Stoner blocking the entrance to Mom's bedroom.")
            time.sleep(3)
            print("You look into Stoner's face but it's blurry, you can't remember exactly what he looks like.")
            time.sleep(3)
            print("It has been a while since you've seen him.")
            time.sleep(3)
            print("Just like before, you have nothing to fight him with.")
            time.sleep(3)
            print("With no other options, you rush towards him with your bare hands.")
            time.sleep(3)
            print("And just like before, he easily overpowers you.")
            time.sleep(3)
            print("He hits you.")
            time.sleep(3)
            print("Again.")
            time.sleep(3)
            print("And again.")
            time.sleep(3)
            print("Lying on the ground and about to lose consciousness you peer into the bedroom.")
            time.sleep(3)
            print("Mom is lying on the bed unmoving.")
            time.sleep(3)
            print("You don't even have the strength to call out to her.")
            time.sleep(3)
            print("After all, ")
            time.sleep(3)
            print("She is already dead")
            time.sleep(3)
        return "complete"

def run_trailer(demon):
    trailer = TrailerPark(demon)
    print("-----------------------------------------------------------------------------------------------------------")
    print(
        "\nYou awaken at the bottom of a small valley, you must have rolled down the hill. You can see your trailer up there in the distance"
        "\nYou worry about what Stoner might do alone in the house "
        "with Mom.\n\nHint: try \n\tw \ta \ts \td : to move \n\ti : to view inventory\n")
    print(
        "Every command is one or two words, learn what you can do in each area. \n\tYour goal is simple: Save Mom\n")
    print("-----------------------------------------------------------------------------------------------------------")
    move = trailer.start()
    while move != "complete":
        move = {
            "start": trailer.start,
            "trailers": trailer.trailers,
            "dog_cage": trailer.dog_cage,
            "peggot": trailer.peggot,
            "porch": trailer.porch,
            "home": trailer.home,
            "creek": trailer.creek,
            "woods": trailer.woods,
            "forest": trailer.forest

        }.get(move, lambda: move)()
    return demon