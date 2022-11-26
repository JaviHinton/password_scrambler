
scrambled = []



def logical_scramble():
    print()


def illogical_scramble():
    print()

user_selection = input("Please type -\n1. Logical Scrambling\n2. Illogical Scrambling\nSelection: ")

if user_selection == str(1):
    print("you have selected Logical Scrambling")
    word = input("Please enter a word to be scrambled: ")
    logical_scramble()
    print(scrambled)


elif user_selection == str(2) :
    print()

else:
    print("Incorrect entry, please enter either 1 or 2")