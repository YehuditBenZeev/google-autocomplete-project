from auto_complete import get_best_k_completions
from create_data import insert_to_dict, data_dict


def search_cln():
    print("Loading and prep..")
    # insert_to_dict()
    print("System is ready, enter text")
    text = input()
    completions = get_best_k_completions(text)
    print_completions(completions)


def print_completions(completions):
    print(completions)


if __name__ == "__main__":
    search_cln()
    for key in data_dict.keys():
        print(key, ": ", data_dict[key])