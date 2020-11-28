import json
from operator import itemgetter

#"data" is a list
#entry is a dict
#each "entry" is a single card.
#each "item" in entry.items() is each (k, v) pair in the card


def build_oracle_dict(dataset):
    oracle_dict = dict()
    for entry in dataset:
        oracle_id = entry["oracle_id"]
        if oracle_id in oracle_dict: #need to write in dict { : } syntax...
            #oracle_dict[oracle_id]
            #oracle_dict[oracle_id] = {oracle_dict[oracle_id].copy(), entry.copy()}#[oracle_dict[oracle_id].copy(), entry.copy()]
            oracle_dict[oracle_id].append(entry)
        else:  # make it into a list of card dicts
            oracle_dict[oracle_id] = [entry]
    return oracle_dict


def count_sets(oracle_dict):
    card_sets = dict()
    for card in oracle_dict:
        for printing in oracle_dict[card]:  # for printing in oracle_dict[card]: #do i need to go one level deeper...?
            card_set = printing["set_name"]

            if card_set in card_sets:
                card_sets[card_set] += 1
            else:
                card_sets[card_set] = 1

            # for print in printing:
            #     #card_set = printing["set_name"]
            #     card_set = print["set_name"]
            #     if card_set in card_sets:
            #         card_sets[card_set] += 1
            #     else:
            #         card_sets[card_set] = 1

    card_count = 0
    for card in card_sets.values():
        card_count += card
    print(F"There are {len(card_sets.keys())} sets of cards.\nTotaling {card_count} cards.")
    return card_sets


def extract_oracle_ids(dataset):
    for entry in dataset:
        for k, v in entry.items():
            if k == "oracle_id":
                break
    return


def main():
    card_file = open('all-cards.json', encoding='utf8')
    card_data = json.load(card_file)

    oracle_dict = build_oracle_dict(card_data)

    print(F"build_oracle_dict() found # oracle_id values: {len(oracle_dict.keys())}")

    count_sets(oracle_dict)

    card_file.close()
    return 0


main()
