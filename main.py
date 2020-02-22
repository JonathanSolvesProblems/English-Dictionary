import json
from difflib import get_close_matches # library to compare text

data = json.load(open("data.json"))

def definition(token):
    token = token.lower() # allows for capital and lower case letters of words to be accepted
    if token in data:
        return data[token]
    elif token.title() in data: # for titles of words, where meant to have cap letter
        return data[token.title()]
    elif token.upper() in data():
        return data[token.upper()]
    elif len(get_close_matches(token, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if so, or N if not: " % get_close_matches(token, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(token, data.keys())[0]]
        elif yn == "N":
            return "The world does not exist. Please verify it"
        else:
            return "Invalid entry"
    else: # if word is not in dictionary
        return "The word does not exist in the dictionary. Please verify your word and try again."

token = input("Enter word: ")

output = definition(token)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)