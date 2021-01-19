from auto_complete import get_best_k_completions
from create_data import create_tree, tree
import util


def search_cln():
    print("Loading and prep..")
    create_tree()
    print("System is ready, enter text")
    while True:
        text = ''
        current_text = input()
        while current_text != '#':
            text += current_text
            clean_text = util.get_clean_line(text)
            print(clean_text)
            sentence_suggestion_list = get_best_k_completions(clean_text)
            util.print_suggestions(sentence_suggestion_list)
            print(text)
            current_text = input()
    # completions = get_best_k_completions(text)
    # print_completions(completions)


if __name__ == "__main__":
    search_cln()
