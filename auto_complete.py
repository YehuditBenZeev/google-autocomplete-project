from auto_complete_data import AutoCompleteData
from create_data import create_tree, tree
# from tree import


def get_best_k_completions(prefix: str):
    sentence_suggestion_list = tree.get_all_auto_suggestions(prefix)

    completed_sentence: str
    source_text: str
    offset: int
    score: int

    auto_complete_data = AutoCompleteData()
    auto_complete_data_list = []
    return auto_complete_data_list


if __name__ == "__main__":
    get_best_k_completions()
