import json

"""
builds a dict of lists of dicts
key == oracle_id
each oracle_dict[oracle_id] has a list of dicts, one for each printing
"""
def build_oracle_dict(dataset):
    oracle_dict = dict()
    for entry in dataset:  # entry --> single card object
        oracle_id = entry["oracle_id"]  # each oracle_id is unique to each logical card object
        if oracle_id in oracle_dict:
            oracle_dict[oracle_id].append(entry)
        else:  # make it into a list of card dicts
            oracle_dict[oracle_id] = [entry]
    return oracle_dict


def count_sets(oracle_dict):
    card_sets = dict()
    for card in oracle_dict:
        for printing in oracle_dict[card]:
            card_set = printing["set_name"]

            if card_set in card_sets:
                card_sets[card_set] += 1
            else:
                card_sets[card_set] = 1

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
