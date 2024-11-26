import time


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
            return {
                "a": "B",
                "w": "E",
                "d": "C"
            }.get(command, "start")
    def A(self):
        print(
            "A There are paths \nstraight, \nright")
        if self.items['crumbA']:
            print("There is a crumb on the ground")
        self.demon.ac.set_commands(["w", "d", "i", "drop crumb"])
        while True:
            command = self.demon.user_val()
            print("")
            if command == "i":
                self.demon.print_inventory()
            elif command == "drop crumb":
                print("You drop the crumb\n")
                self.items['crumbA'] = True
            return {
                "w": "O",
                "d": "B"
            }.get(command, "A")
    def B(self):
        print(
            "B There are paths \nleft, \nstraight, \nright")
        if self.items['crumbB']:
            print("There is a crumb on the ground")
        self.demon.ac.set_commands(["w", "a", "d", "i", "drop crumb"])
        while True:
            command = self.demon.user_val()
            print("")
            if command == "i":
                self.demon.print_inventory()
            elif command == "drop crumb":
                print("You drop the crumb\n")
                self.items['crumbB'] = True
            return {
                "a": "A",
                "w": "D",
                "d": "start"
            }.get(command, "B")
    def C(self):
        print(
            "C There are paths \nleft, \nstraight")
        if self.items['crumbC']:
            print("There is a crumb on the ground")
        self.demon.ac.set_commands(["a", "w", "i", "drop crumb"])
        while True:
            command = self.demon.user_val()
            print("")
            if command == "i":
                self.demon.print_inventory()
            elif command == "drop crumb":
                print("You drop the crumb\n")
                self.items['crumbC'] = True
            return {
                "a": "start",
                "w": "F"
            }.get(command, "C")
    def D(self):
        print(
            "D There are paths \nstraight, \nback")
        if self.items['crumbD']:
            print("There is a crumb on the ground")
        self.demon.ac.set_commands(["w", "s", "i", "drop crumb"])
        while True:
            command = self.demon.user_val()
            print("")
            if command == "i":
                self.demon.print_inventory()
            elif command == "drop crumb":
                print("You drop the crumb\n")
                self.items['crumbD'] = True
            return {
                "w": "G",
                "s": "B"
            }.get(command, "D")
    def E(self):
        print(
            "E There are paths \nstraight, \nback")
        if self.items['crumbE']:
            print("There is a crumb on the ground")
        self.demon.ac.set_commands(["w", "s", "i", "drop crumb"])
        while True:
            command = self.demon.user_val()
            print("")
            if command == "i":
                self.demon.print_inventory()
            elif command == "drop crumb":
                print("You drop the crumb\n")
                self.items['crumbE'] = True
            return {
                "w": "H",
                "s": "start"
            }.get(command, "E")
    def F(self):
        print(
            "F There are paths \nstraight, \nback")
        if self.items['crumbF']:
            print("There is a crumb on the ground")
        self.demon.ac.set_commands(["w", "s", "i", "drop crumb"])
        while True:
            command = self.demon.user_val()
            print("")
            if command == "i":
                self.demon.print_inventory()
            elif command == "drop crumb":
                print("You drop the crumb\n")
                self.items['crumbF'] = True
            return {
                "w": "I",
                "s": "C"
            }.get(command, "F")
    def G(self):
        print(
            "G There are paths \nleft, \nright")
        if self.items['crumbG']:
            print("There is a crumb on the ground")
        self.demon.ac.set_commands(["a", "d", "i", "drop crumb"])
        while True:
            command = self.demon.user_val()
            print("")
            if command == "i":
                self.demon.print_inventory()
            elif command == "drop crumb":
                print("You drop the crumb\n")
                self.items['crumbG'] = True
            return {
                "a": "O",
                "d": "H"
            }.get(command, "G")
    def H(self):
        print(
            "H There are paths \nleft, \nstraight, \nright, \nback")
        if self.items['crumbH']:
            print("There is a crumb on the ground")
        self.demon.ac.set_commands(["a", "d", "w", "s", "i", "drop crumb"])
        while True:
            command = self.demon.user_val()
            print("")
            if command == "i":
                self.demon.print_inventory()
            elif command == "drop crumb":
                print("You drop the crumb\n")
                self.items['crumbH'] = True
            return {
                "w": "K",
                "a": "G",
                "s": "I",
                "d": "E"
            }.get(command, "H")
    def I(self):
        print(
            "I There are paths \nleft, \nright, \nback")
        if self.items['crumbI']:
            print("There is a crumb on the ground")
        self.demon.ac.set_commands(["a", "d", "s", "i", "drop crumb"])
        while True:
            command = self.demon.user_val()
            print("")
            if command == "i":
                self.demon.print_inventory()
            elif command == "drop crumb":
                print("You drop the crumb\n")
                self.items['crumbI'] = True
            return {
                "a": "H",
                "s": "F",
                "d": "J"
            }.get(command, "I")
    def J(self):
        print(
            "J There are paths \nleft, \nstraight")
        if self.items['crumbJ']:
            print("There is a crumb on the ground")
        self.demon.ac.set_commands(["a", "w", "i", "drop crumb"])
        while True:
            command = self.demon.user_val()
            print("")
            if command == "i":
                self.demon.print_inventory()
            elif command == "drop crumb":
                print("You drop the crumb\n")
                self.items['crumbJ'] = True
            return {
                "w": "M",
                "a": "I",
            }.get(command, "J")
    def K(self):
        print(
            "K There are paths \nright, \nback")
        if self.items['crumbK']:
            print("There is a crumb on the ground")
        self.demon.ac.set_commands(["d", "s", "i", "drop crumb"])
        while True:
            command = self.demon.user_val()
            print("")
            if command == "i":
                self.demon.print_inventory()
            elif command == "drop crumb":
                print("You drop the crumb\n")
                self.items['crumbK'] = True
            return {
                "s": "H",
                "d": "L"
            }.get(command, "K")
    def L(self):
        print(
            "L There are paths \nleft, \nstraight, \nright")
        if self.items['crumbL']:
            print("There is a crumb on the ground")
        self.demon.ac.set_commands(["a", "d", "w", "i", "drop crumb"])
        while True:
            command = self.demon.user_val()
            print("")
            if command == "i":
                self.demon.print_inventory()
            elif command == "drop crumb":
                print("You drop the crumb\n")
                self.items['crumbL'] = True
            return {
                "w": "N",
                "a": "K",
                "d": "M"
            }.get(command, "L")
    def M(self):
        print(
            "M There are paths \nleft, \nback")
        if self.items['crumbM']:
            print("There is a crumb on the ground")
        self.demon.ac.set_commands(["a", "s", "i", "drop crumb"])
        while True:
            command = self.demon.user_val()
            print("")
            if command == "i":
                self.demon.print_inventory()
            elif command == "drop crumb":
                print("You drop the crumb\n")
                self.items['crumbM'] = True
            return {
                "a": "L",
                "s": "J",
            }.get(command, "M")
    def N(self):
        print(
            "N There are paths \nstraight, \nback")
        if self.items['crumbN']:
            print("There is a crumb on the ground")
        self.demon.ac.set_commands(["w", "s", "i", "drop crumb"])
        while True:
            command = self.demon.user_val()
            print("")
            if command == "i":
                self.demon.print_inventory()
            elif command == "drop crumb":
                print("You drop the crumb\n")
                self.items['crumbN'] = True
            return {
                "w": "Tommy",
                "s": "L",
            }.get(command, "N")
    def O(self):
        print(
            "O There are paths \nright, \nback")
        if self.items['crumbO']:
            print("There is a crumb on the ground")
        self.demon.ac.set_commands(["d", "s", "i", "drop crumb"])
        while True:
            command = self.demon.user_val()
            print("")
            if command == "i":
                self.demon.print_inventory()
            elif command == "drop crumb":
                print("You drop the crumb\n")
                self.items['crumbO'] = True
            return {
                "d": "G",
                "s": "A",
            }.get(command, "O")
    def Tommy(self):
        print(
            "You found Tommy!")
        return "complete"

def run_farm(demon):
    farm = Farm(demon)
    print("-----------------------------------------------------------------------------------------------------------")
    print(
        "\nYou wake up in the middle of the tabacco field on Creaky farm, it feels familiar and yet you cannot see an easy way out. "
        "\nYou hope Tommy isn't waiting for you on the hill again.\n\nHint: try \n\tw \ta \ts \td : to move \n\ti : to view inventory\n")
    print(
        "Every command is one or two words, learn what you can do in each area. \n\tYour goal is simple: Find Tommy\n")
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