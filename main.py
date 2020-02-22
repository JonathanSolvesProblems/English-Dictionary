import json

data = json.load(open("data.json"))

def definition(token):
    return data[token]

token = input("Enter word: ")

print(definition(token))