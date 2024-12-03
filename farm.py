import time
from commands import strike


class Farm:
    def __init__(self, demon):
        self.demon = demon
        self.items = {
            'bread': True,
            'crumbA': False,
            'crumbB': False,
            'crumbC': False,
            'crumbD': False,
            'crumbE': False,
            'crumbF': False,
            'crumbG': False,
            'crumbH': False,
            'crumbI': False,
            'crumbJ': False,
            'crumbK': False,
            'crumbL': False,
            'crumbM': False,
            'crumbN': False,
            'crumbO': False,
        }
        self.moves = 0

    def update_moves(self):
        if self.moves > 15:
            print("You are out of moves\n")
            return "complete"
        else:
            if self.moves == 5:
                print("You feel a little lightheaded\n")
            if self.moves == 8:
                print("Your headache and nausea worsen")
            if self.moves == 13:
                print("You are really not feeling well, if you don't find the exit soon you might pass out\n")
            self.moves = self.moves + 1
            return ""
    def start(self):
        print(
            "You can see the indent in the ground where you were laying.\nThere are paths: \n\tleft, \n\tstraight, \n\tright")
        if self.items['bread']:
            print("On the ground is a loaf of bread, maybe you can drop breadcrumbs to leave a trail")
        self.demon.ac.set_commands(["w", "a", "d", "i", "grab bread"])

        while True:
            command = self.demon.user_val()
            print("")
            if command == "i":
                self.demon.print_inventory()
            elif command == "grab bread":
                print("You grab the bread")
                self.demon.add_to_inventory("bread")
                self.items['bread'] = False
            elif command == "a":
                return "B"
            elif command == "w":
                return "E"
            elif command == "d":
                return "C"
    def dead_end(self):
        print("You reached a dead end\n")
    def A(self):
        response = self.update_moves()
        if response == "complete":
            return "complete"
        print(
            "A There are paths \nstraight, \nright")
        if self.items['crumbA']:
            print("There is a crumb on the ground")
        self.demon.ac.set_commands(["w", "d", "i", "drop crumb", "use bread"])
        while True:
            command = self.demon.user_val()
            print("")
            if command == "i":
                self.demon.print_inventory()
            elif "bread" not in self.demon.inventory and (command == "drop crumb" or command == "use bread"):
                print("You don't have any bread")
            elif "bread" in self.demon.inventory and (command == "drop crumb" or command == "use bread"):
                print("You drop a crumb of bread\n")
                self.items['crumbA'] = True
            elif command == "w":
                return "O"
            elif command == "d":
                return "B"
    def B(self):
        response = self.update_moves()
        if response == "complete":
            return "complete"
        print(
            "B There are paths \nleft, \nstraight, \nright")
        if self.items['crumbB']:
            print("There is a crumb on the ground")
        self.demon.ac.set_commands(["w", "a", "d", "i", "drop crumb", "use bread"])
        while True:
            command = self.demon.user_val()
            print("")
            if command == "i":
                self.demon.print_inventory()
            elif "bread" not in self.demon.inventory and (command == "drop crumb" or command == "use bread"):
                print("You don't have any bread")
            elif "bread" in self.demon.inventory and (command == "drop crumb" or command == "use bread"):
                print("You drop a crumb of bread\n")
                self.items['crumbB'] = True
            elif command == "a":
                return "A"
            elif command == "w":
                return "D"
            elif command == "d":
                return "start"
    def C(self):
        response = self.update_moves()
        if response == "complete":
            return "complete"
        print(
            "C There are paths \nleft, \nstraight")
        if self.items['crumbC']:
            print("There is a crumb on the ground")
        self.demon.ac.set_commands(["a", "w", "i", "drop crumb", "use bread"])
        while True:
            command = self.demon.user_val()
            print("")
            if command == "i":
                self.demon.print_inventory()
            elif "bread" not in self.demon.inventory and (command == "drop crumb" or command == "use bread"):
                print("You don't have any bread")
            elif "bread" in self.demon.inventory and (command == "drop crumb" or command == "use bread"):
                print("You drop a crumb of bread\n")
                self.items['crumbC'] = True
            elif command == "a":
                return "start"
            elif command == "w":
                return "F"
    def D(self):
        response = self.update_moves()
        if response == "complete":
            return "complete"
        print(
            "D There are paths \nstraight, \nback")
        if self.items['crumbD']:
            print("There is a crumb on the ground")
        self.demon.ac.set_commands(["w", "s", "i", "drop crumb", "use bread"])
        while True:
            command = self.demon.user_val()
            print("")
            if command == "i":
                self.demon.print_inventory()
            elif "bread" not in self.demon.inventory and (command == "drop crumb" or command == "use bread"):
                print("You don't have any bread")
            elif "bread" in self.demon.inventory and (command == "drop crumb" or command == "use bread"):
                print("You drop a crumb of bread\n")
                self.items['crumbD'] = True
            elif command == "w":
                return "G"
            elif command == "s":
                return "B"
    def E(self):
        response = self.update_moves()
        if response == "complete":
            return "complete"
        print(
            "E There are paths \nstraight, \nback")
        if self.items['crumbE']:
            print("There is a crumb on the ground")
        self.demon.ac.set_commands(["w", "s", "i", "drop crumb", "use bread"])
        while True:
            command = self.demon.user_val()
            print("")
            if command == "i":
                self.demon.print_inventory()
            elif "bread" not in self.demon.inventory and (command == "drop crumb" or command == "use bread"):
                print("You don't have any bread")
            elif "bread" in self.demon.inventory and (command == "drop crumb" or command == "use bread"):
                print("You drop a crumb of bread\n")
                self.items['crumbE'] = True
            elif command == "w":
                print("You find yourself back at the beginning\n")
                return "start"
            elif command == "s":
                return "start"
    def F(self):
        response = self.update_moves()
        if response == "complete":
            return "complete"
        print(
            "F There are paths \nstraight, \nback")
        if self.items['crumbF']:
            print("There is a crumb on the ground")
        self.demon.ac.set_commands(["w", "s", "i", "drop crumb", "use bread"])
        while True:
            command = self.demon.user_val()
            print("")
            if command == "i":
                self.demon.print_inventory()
            elif "bread" not in self.demon.inventory and (command == "drop crumb" or command == "use bread"):
                print("You don't have any bread")
            elif "bread" in self.demon.inventory and (command == "drop crumb" or command == "use bread"):
                print("You drop a crumb of bread\n")
                self.items['crumbF'] = True
            elif command == "w":
                return "I"
            elif command == "s":
                return "C"
    def G(self):
        response = self.update_moves()
        if response == "complete":
            return "complete"
        print(
            "G There are paths \nleft, \nright")
        if self.items['crumbG']:
            print("There is a crumb on the ground")
        self.demon.ac.set_commands(["a", "d", "i", "drop crumb", "use bread"])
        while True:
            command = self.demon.user_val()
            print("")
            if command == "i":
                self.demon.print_inventory()
            elif "bread" not in self.demon.inventory and (command == "drop crumb" or command == "use bread"):
                print("You don't have any bread")
            elif "bread" in self.demon.inventory and (command == "drop crumb" or command == "use bread"):
                print("You drop a crumb of bread\n")
                self.items['crumbG'] = True
            elif command == "a":
                return "O"
            elif command == "d":
                return "H"
    def H(self):
        response = self.update_moves()
        if response == "complete":
            return "complete"
        print(
            "H There are paths \nleft, \nstraight, \nright, \nback")
        if self.items['crumbH']:
            print("There is a crumb on the ground")
        self.demon.ac.set_commands(["a", "d", "w", "s", "i", "drop crumb", "use bread"])
        while True:
            command = self.demon.user_val()
            print("")
            if command == "i":
                self.demon.print_inventory()
            elif "bread" not in self.demon.inventory and (command == "drop crumb" or command == "use bread"):
                print("You don't have any bread")
            elif "bread" in self.demon.inventory and (command == "drop crumb" or command == "use bread"):
                print("You drop a crumb of bread\n")
                self.items['crumbH'] = True
            elif command == "w":
                return "K"
            elif command == "a":
                return "G"
            elif command == "s":
                return "E"
            elif command == "d":
                return "I"
    def I(self):
        response = self.update_moves()
        if response == "complete":
            return "complete"
        print(
            "I There are paths \nleft, \nright, \nback")
        if self.items['crumbI']:
            print("There is a crumb on the ground")
        self.demon.ac.set_commands(["a", "d", "s", "i", "drop crumb", "use bread"])
        while True:
            command = self.demon.user_val()
            print("")
            if command == "i":
                self.demon.print_inventory()
            elif "bread" not in self.demon.inventory and (command == "drop crumb" or command == "use bread"):
                print("You don't have any bread")
            elif "bread" in self.demon.inventory and (command == "drop crumb" or command == "use bread"):
                print("You drop a crumb of bread\n")
                self.items['crumbI'] = True
            elif command == "a":
                return "H"
            elif command == "s":
                return "F"
            elif command == "d":
                return "J"
    def J(self):
        response = self.update_moves()
        if response == "complete":
            return "complete"
        print(
            "J There are paths \nleft, \nstraight")
        if self.items['crumbJ']:
            print("There is a crumb on the ground")
        self.demon.ac.set_commands(["a", "w", "i", "drop crumb", "use bread"])
        while True:
            command = self.demon.user_val()
            print("")
            if command == "i":
                self.demon.print_inventory()
            elif "bread" not in self.demon.inventory and (command == "drop crumb" or command == "use bread"):
                print("You don't have any bread")
            elif "bread" in self.demon.inventory and (command == "drop crumb" or command == "use bread"):
                print("You drop a crumb of bread\n")
                self.items['crumbJ'] = True
            elif command == "w":
                return "M"
            elif command == "a":
                return "I"
    def K(self):
        response = self.update_moves()
        if response == "complete":
            return "complete"
        print(
            "K There are paths \nright, \nback")
        if self.items['crumbK']:
            print("There is a crumb on the ground")
        self.demon.ac.set_commands(["d", "s", "i", "drop crumb", "use bread"])
        while True:
            command = self.demon.user_val()
            print("")
            if command == "i":
                self.demon.print_inventory()
            elif "bread" not in self.demon.inventory and (command == "drop crumb" or command == "use bread"):
                print("You don't have any bread")
            elif "bread" in self.demon.inventory and (command == "drop crumb" or command == "use bread"):
                print("You drop a crumb of bread\n")
                self.items['crumbK'] = True
            elif command == "s":
                return "H"
            elif command == "d":
                return "L"
    def L(self):
        response = self.update_moves()
        if response == "complete":
            return "complete"
        print(
            "L There are paths \nleft, \nstraight, \nright")
        if self.items['crumbL']:
            print("There is a crumb on the ground")
        self.demon.ac.set_commands(["a", "d", "w", "i", "drop crumb", "use bread"])
        while True:
            command = self.demon.user_val()
            print("")
            if command == "i":
                self.demon.print_inventory()
            elif "bread" not in self.demon.inventory and (command == "drop crumb" or command == "use bread"):
                print("You don't have any bread")
            elif "bread" in self.demon.inventory and (command == "drop crumb" or command == "use bread"):
                print("You drop a crumb of bread\n")
                self.items['crumbL'] = True
            elif command == "w":
                return "N"
            elif command == "a":
                return "K"
            elif command == "d":
                return "M"
    def M(self):
        response = self.update_moves()
        if response == "complete":
            return "complete"
        print(
            "M There are paths \nleft, \nback")
        if self.items['crumbM']:
            print("There is a crumb on the ground")
        self.demon.ac.set_commands(["a", "s", "i", "drop crumb", "use bread"])
        while True:
            command = self.demon.user_val()
            print("")
            if command == "i":
                self.demon.print_inventory()
            elif "bread" not in self.demon.inventory and (command == "drop crumb" or command == "use bread"):
                print("You don't have any bread")
            elif "bread" in self.demon.inventory and (command == "drop crumb" or command == "use bread"):
                print("You drop a crumb of bread\n")
                self.items['crumbM'] = True
            elif command == "a":
                return "L"
            elif command == "s":
                return "J"
    def N(self):
        response = self.update_moves()
        if response == "complete":
            return "complete"
        print(
            "N There are paths \nstraight, \nback")
        if self.items['crumbN']:
            print("There is a crumb on the ground")
        self.demon.ac.set_commands(["w", "s", "i", "drop crumb", "use bread"])
        while True:
            command = self.demon.user_val()
            print("")
            if command == "i":
                self.demon.print_inventory()
            elif "bread" not in self.demon.inventory and (command == "drop crumb" or command == "use bread"):
                print("You don't have any bread")
            elif "bread" in self.demon.inventory and (command == "drop crumb" or command == "use bread"):
                print("You drop a crumb of bread\n")
                self.items['crumbN'] = True
            elif command == "w":
                return "Tommy"
            elif command == "s":
                return "L"
    def O(self):
        response = self.update_moves()
        if response == "complete":
            return "complete"
        print(
            "O There are paths \nright, \nback")
        if self.items['crumbO']:
            print("There is a crumb on the ground")
        self.demon.ac.set_commands(["d", "s", "i", "drop crumb", "use bread"])
        while True:
            command = self.demon.user_val()
            print("")
            if command == "i":
                self.demon.print_inventory()
            elif "bread" not in self.demon.inventory and (command == "drop crumb" or command == "use bread"):
                print("You don't have any bread")
            elif "bread" in self.demon.inventory and (command == "drop crumb" or command == "use bread"):
                print("You drop a crumb of bread\n")
                self.items['crumbO'] = True
            elif command == "d":
                return "G"
            elif command == "s":
                return "A"
    def Tommy(self):
        print(
            "#Cutscene: You see a figure on the hill but as you approach the figure fades and you see two graves, but instead of Tommy's parents you see the names of your own\n")
        return "complete"

def run_farm(demon):
    farm = Farm(demon)
    text = "Save Mom"
    newText = strike(text)
    print("-----------------------------------------------------------------------------------------------------------")
    print(
        "\nYou wake up in the middle of the tabacco field on Creaky farm, it feels familiar and yet you cannot see an easy way out. "
        "\nYou hope Tommy isn't waiting for you on the hill again.\n\nHint: try \n\tw \ta \ts \td : to move \n\ti : to view inventory\n")
    print(
        "Every command is one or two words, learn what you can do in each area. \n\tYour goal is simple: " + newText + " Find Tommy\n")
    print("-----------------------------------------------------------------------------------------------------------")
    move = farm.start()
    while move != "complete":
        move = {
            "start": farm.start,
            "A": farm.A,
            "B": farm.B,
            "C": farm.C,
            "D": farm.D,
            "E": farm.E,
            "F": farm.F,
            "G": farm.G,
            "H": farm.H,
            "I": farm.I,
            "J": farm.J,
            "K": farm.K,
            "L": farm.L,
            "M": farm.M,
            "N": farm.N,
            "O": farm.O,
            "Tommy": farm.Tommy

        }.get(move, lambda: move)()

    print("\nCongratulations, you reached a possible ending for level 2! Try again to see another ending and wait for level 3.")
    return demon