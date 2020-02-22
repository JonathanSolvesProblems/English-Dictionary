import json
from difflib import get_close_matches # library to compare text

data = json.load(open("data.json"))

def definition(token):
    token = token.lower() # allows for capital and lower case letters of words to be accepted
    if token in data:
        return data[token]
    elif len(get_close_matches(token, data.keys())) > 0:
        return "Did you mean %s instead? " % get_close_matches(token, data.keys())[0]
    else: # if word is not in dictionary
        return "The word does not exist in the dictionary. Please verify your word and try again."

token = input("Enter word: ")

print(definition(token))