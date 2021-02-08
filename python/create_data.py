import sys
import os
from tree import Tree
from config import file_
from auto_complete_data import SentenceData
from util import get_shortened_sentence, is_longer_then_3

sys.path.append(os.path.dirname(os.path.abspath("../Aechive/rfc7501.txt")))

tree = Tree()


def get_files():
    data_dir_list = []
    for root, directories, files in os.walk(file_):
        file_path = root + '/'
        for file in files:
            data_dir_list.append(file_path+'/'+file)
    print(len(data_dir_list))
    print("done get_files")
    # return data_dir_list
    return ["../Aechive/our_text.txt"]


def open_files():
    data_file_list = get_files()
    all_lines = []

    for file_path in data_file_list:
        with open(os.path.abspath(file_path), encoding="utf8")as file:
            for i, line in enumerate(file.readlines(), start=1):
                line_lowercase = line.lower()
                contains_letters = line_lowercase.islower()
                has_at_least_3_words = is_longer_then_3(line)
                if contains_letters and has_at_least_3_words:
                    short_line = get_shortened_sentence(line, 10)
                    sentence_data = SentenceData(short_line,  f'{file_path} {i}')
                    all_lines.append(sentence_data)
    print(len(all_lines))
    return all_lines


def create_tree():
    all_lines = open_files()
    tree.formTree(all_lines)


def write_to_file():
    pass
