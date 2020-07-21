import json
from difflib import get_close_matches

data = json.load(open('data.json'))


def translate(word):
    w = word.lower()
    if w in data:
        return "\n".join(data[w])
    else:
        match = get_close_matches(w, data.keys())
        if match:
            # print("do you mean \""+match[0]+"\" Y/N")
            key = input("do you mean \""+match[0]+"\" Y/N  ")
            if key.lower() == 'y':
                return "\n".join(data[match[0]])
            else:
                return "Word doesn't exist! please check again."
        else:
            return "Word doesn't exist! please check again."


word = input('Enter word: ')
print(translate(word))
