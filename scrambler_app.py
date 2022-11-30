

vowels_scrambled = {
    "a":"!",
    "e": "?",
    "i": "$",
    "o": "%",
    "u": "*"
    }
scrambled = []
word_list = []

def word_to_list():
    word_list = []
    for letter in word:
        word_list.append(letter)
    return word_list

def logical_scramble(word_list):
    current_letter = 0
    word_length = len(word_list)
    for vowel in vowels_scrambled:
        while current_letter >= word_length:
            if vowel == word_list[current_letter]:
                scrambled.append[vowel]
            else:
                scrambled.append(word_list[current_letter])
        current_letter += 1
    print(scrambled)
    return scrambled
    

    print()


def illogical_scramble():
    print()

user_selection = input("Please type -\n1. Logical Scrambling\n2. Illogical Scrambling\nSelection: ")


if user_selection == str(1):
    print("you have selected Logical Scrambling")
    word = input("Please enter a word to be scrambled: ")
    word_to_list()
    
    logical_scramble(word_list)
    print(scrambled)


elif user_selection == str(2) :
    print()

else:
    print("Incorrect entry, please enter either 1 or 2")