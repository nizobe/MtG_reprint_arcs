import json

#"data" is a list
#entry is a dict
#each "entry" is a single card.
#each "item" in entry.items() is each (k, v) pair in the card


def build_oracle_dict(dataset):
    oracle_dict = dict()
    for entry in dataset:
        oracle_id = entry["oracle_id"]
        if oracle_id in oracle_dict:
            oracle_dict[oracle_id] = [oracle_dict[oracle_id], entry]
        else:
            oracle_dict[oracle_id] = entry
    return oracle_dict


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
    card_file.close()
    return 0


main()
