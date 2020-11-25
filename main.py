import json
from collections import Counter

f = open('all-cards.json', encoding='utf8')

data = json.load(f)

keyCount = 0
cardCount = 0
stop = 0
entryCount = 0
setsRaw = list()

cardIDs = list()
oracleIDs = set()

cardInfo = {}

# def relevantValue(i):
#     switcher = {
#         "set":"sets",
#         "reprint":"reprints",
#
#     }
#
# def count_cards(cards, info):
#     for card in cards:
#         for(k, v) in card.items():

#"data" is a list
#entry is a dict
#each "entry" is a single card.
#each "item" in entry.items() is each (k, v) pair in the card
for entry in data:
    entryCount += 1
    for(k, v) in entry.items():
        keyCount += 1
        if k == "id":
            cardIDs.append(v)
        if k == "oracle_id":
            oracleIDs.add(v)
        if k == "set":
            setsRaw.append(v)

sets = dict(Counter(setsRaw))

for k,v in sets.items():
    print(F"{k} : {v}")

print(F"# of sets: {len(sets.keys())}")

print(F"cardIDs before duplicate removal: {len(cardIDs)}")

uIDs = set(cardIDs)

print(F"cardIDs after duplicate removal: {len(uIDs)}")

print(F"oracleIDs: {len(oracleIDs)}")


def build_oracle_dict(dataset):
    oracle_dict = dict()
    for entry in dataset:
        for k, v in entry.items():#wait sec... i can just access the "oracle_id" key directly inside "entry" /facepalm
            if k == "oracle_id":
                if v in oracle_dict:
                    oracle_dict[v] = [oracle_dict[v], entry]
                else:
                    oracle_dict[v] = entry
    return oracle_dict

def extract_oracle_ids(dataset):
    for entry in dataset:
        for k, v in entry.items():
            if k == "oracle_id":
                break
    return


def main():
    global data
    global f
    oracle_dict = build_oracle_dict(data)
    print(F"build_oracle_dict() found # oracle_id values: {len(oracle_dict.keys())}")
    f.close()
    return 0


main()

        # if stop < 10:
        #     print(k, "\n", v, "\n")
        #     stop += 1

# print(F"keyCount: {keyCount:,}")
# print(F"cardCount: {cardCount:,}")
# print(F"entryCount: {entryCount:,}")
