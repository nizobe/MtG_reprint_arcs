import json

f = open('default_cards.json', encoding='utf8')

data = json.load(f)

keyCount = 0
cardCount = 0
stop = 0

for entry in data:
    for(k, v) in entry.items():
        keyCount += 1
        if k == "object" and v == "card":
            cardCount += 1

        if stop < 10:
            print(k, "\n", v, "\n")
            stop += 1

print(F"keyCount: 1", keyCount)
print(F"cardCount: 1", cardCount)
f.close()
