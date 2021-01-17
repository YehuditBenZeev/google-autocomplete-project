from auto_complete import get_best_k_completions
from create_data import create_tree, tree


def search_cln():
    print("Loading and prep..")
    create_tree()
    print("System is ready, enter text")
    text = input()
    while text != '#':    
        sentence_suggestion_list = get_best_k_completions(text)
        print_suggestions(sentence_suggestion_list)
        print(text)
        text = input()
    # completions = get_best_k_completions(text)
    # print_completions(completions)


def print_suggestions(sentence_suggestion_list):
    for i, autocomplete_item in enumerate(list(set(sentence_suggestion_list)), start=1):
        print(f"{i}. {autocomplete_item.completed_sentence} ({autocomplete_item.source_text})")
        


if __name__ == "__main__":
    search_cln()
