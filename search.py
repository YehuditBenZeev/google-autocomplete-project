from auto_complete import get_best_k_completions
from create_data import create_tree, tree


def search_cln():
    print("Loading and prep..")
    create_tree()
    print("System is ready, enter text")
    text = input()
    while text != '#':    
        get_best_k_completions(text)
        print(text)
        text = input()
    # completions = get_best_k_completions(text)
    # print_completions(completions)


def print_completions(completions):
    print(completions)


if __name__ == "__main__":
    search_cln()
