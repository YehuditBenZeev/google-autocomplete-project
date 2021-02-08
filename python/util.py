import string
import re
from auto_complete_data import AutoCompleteData


def is_longer_then_3(line):
    clean_line = get_clean_sentence(line)
    clean_line_list = clean_line.split()
    return len(clean_line_list) > 3


def get_clean_sentence(prefix):
    translator = str.maketrans('', '', string.punctuation)
    clean_prefix = prefix.translate(translator)
    prefix_list = clean_prefix.split()
    clean_prefix = ' '.join(prefix_list)
    clean_prefix = re.sub(r"[\n\t]*", "", clean_prefix)
    return clean_prefix


def print_suggestions(auto_complete_data_suggestion_list):
    if len(auto_complete_data_suggestion_list) < 1:
        print("no suggestion found.")
    for i, item in enumerate(auto_complete_data_suggestion_list[:5], start=1):
        print(f"{i}. {item.completed_sentence} (source file:{item.source_text}) \n (score:{item.score})")

    reset_score(auto_complete_data_suggestion_list)


def reset_score(auto_complete_data_list):
    for item in auto_complete_data_list:
        item.score = 0


def get_shortened_sentence(sentence, sen_len):
    wort_list = sentence.split()
    if len(wort_list) < sen_len:
        return sentence
    short_sentence = " ".join(wort_list[:sen_len])
    return short_sentence


def update_score(auto_complete_data_list, prefix_len, index=-1, is_replaced=False):
    for item in auto_complete_data_list:
        if not item.score == 0:
            continue
        item.score = prefix_len * 2
        if not index == -1:
            if is_replaced:
                item.score -= 5 - index if 5 - index > 1 else 1
            else:
                item.score -= (5 - index)*2 if 5 - index > 1 else 2


def replacer(old_string, new_string, index):
    # raise an error if index is outside of the string
    if index >= len(old_string) or index < 0:
        raise ValueError("index outside given string")

    # insert the new string between "slices" of the original
    return old_string[:index] + new_string + old_string[index + 1:]


def from_sentence_to_auto_complete(sentence_list):
    auto_complete_list = []
    for sentence_item in sentence_list:
        auto_complete_list.append(AutoCompleteData(sentence_item.completed_sentence, sentence_item.source_text, 0, 0))

    return auto_complete_list

#def get_sub_sentence


if __name__ == "__main__":
    s = "abc def"
    s1 = replacer(s, 'qa', 5)
    print(s1)
    print(len(s1))
