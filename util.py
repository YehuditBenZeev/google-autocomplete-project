import string
import re


def get_clean_line(line):
    translator = str.maketrans('', '', string.punctuation)
    clean_line = line.translate(translator)
    line_list = clean_line.split()
    clean_line = ' '.join(line_list)
    clean_line = re.sub(r"[\n\t]*", "", clean_line)
    return clean_line


def print_suggestions(sentence_suggestion_list):
    if len(sentence_suggestion_list) < 1:
        print("no suggestion found.")
    for i, autocomplete_item in enumerate(list(set(sentence_suggestion_list)), start=1):
        print(f"{i}. {autocomplete_item.completed_sentence} (source file:{autocomplete_item.source_text})")


def get_shortened_sentence(sentence, sen_len):
    wort_list = sentence.split()
    if len(wort_list) < sen_len:
        return sentence
    short_sentence = " ".join(wort_list[:sen_len])
    return short_sentence


def calculate_score(sentence_suggestion):
    pass

