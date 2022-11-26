#   This is a program that will scramble passwords in
#   both a logical and illogical way

vowels = ["a", "e", "i", "o", "u"]
symbols = ["!", "?", "$", "#", "%"]
scrambled = []

# Could set below to 21 to save the extra colde & calculations
consonants = "qwrtypsdfghjklzxcvbnm"
amount_of_consonants = 0
for c in consonants:
    amount_of_consonants += 1


def logical_scramble():
    for i in word:
        vowel_position = 0
        while vowel_position != 5:
            if i == vowels[vowel_position]:
                scrambled.append(symbols[vowel_position])
                vowel_position += 1
            else:
                scrambled.append(str(i))
                vowel_position += 1



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