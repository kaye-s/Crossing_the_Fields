def comp_str(string1, string2):
    return string1.lower() == string2.lower()

def strike(text):
    return ''.join([u'\u0336{}'.format(c) for c in text])

class Demon:
    def __init__(self):
        self.ac = None
        self.inventory = []

    def avail_commands(self, ac):
        self.ac = ac

    def user_val(self):
        command = ""
        while not command in self.ac.simple_commands:
            command = input("Enter a command:")
        return command

    def print_inventory(self):
        print("Inventory:")
        if not self.inventory:
            print("\t None")
        else:
            for item in self.inventory:
                print("\t" + item)
        print("")

    def add_to_inventory(self, item):
        self.inventory.append(item)

    def remove_from_inventory(self, item):
        self.inventory.remove(item)

class AvailCommands:
    def __init__(self):
        self.simple_commands = []

    def set_commands(self, commands):
        self.simple_commands = commands




