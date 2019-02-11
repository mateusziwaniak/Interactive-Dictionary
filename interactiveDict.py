import json
from difflib import SequenceMatcher, get_close_matches


data = json.load(open("data.json"))


def take_input():
    x = ""
    while x not in data.keys():
        x = input("Please type a key word: ")

        if x in data.keys():
            return x
        elif x.title() in data.keys():
            return x.title()
        elif x.upper() in data.keys():
            return x.upper()
        else:
            x = similar_words(x)
    return x.lower()


def similar_words(x):
    word = get_close_matches(x, data.keys())[0]
    print("Maybe you wanted to print:", word, "?")
    choice = input("Press Y for YES or N for NO: ").lower()
    if choice == "y":
        return word
    else:
        return x


def get_inf(key):

    return data[key]


x = take_input()
for sentence in get_inf(x):
    print(sentence)

