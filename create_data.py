import sys, os
from _pytest.tmpdir import tmp_path
sys.path.append(os.path.dirname(os.path.abspath("../Aechive/rfc7501.txt")))
from tree import Tree
from config import file_
from auto_complete_data import AutoCompleteData
from util import get_shortened_sentence


tree = Tree()


def get_files():
    data_dir_list = []
    for root, directories, files in os.walk(file_):
        file_path = root + '/'
        for file in files:
            data_dir_list.append(file_path+'/'+file)
    print(len(data_dir_list))
    print("done get_files")
    return data_dir_list[:2]


def open_files():
    print("in function")
    data_file_list = get_files()
    all_lines = []

    for file_path in data_file_list:
        with open(os.path.abspath(file_path), encoding="utf8")as file:
            for i, line in enumerate(file.readlines(), start=1):
                line_lowercase = line.lower()
                contains_letters = line_lowercase.islower()
                if contains_letters:
                    short_line = get_shortened_sentence(line, 20)
                    auto_complete_data = AutoCompleteData(short_line,  f'{file_path} {i}', 0, 0)
                    all_lines.append(auto_complete_data)
    print(len(all_lines))
    return all_lines



# def create_tree():
#     with open(os.path.abspath(file_path))as file:
#         sentences = []
#         for line in file.readlines():
#             if line == "\n":
#                 continue
#             line = line.replace('\n', '')
#             sentences.append(line)

#         tree.formTree(sentences)
#         print(tree.positions)


def create_tree():
    all_lines = open_files()
    tree.formTree(all_lines)  ## change to auto_complete_data_item


def write_to_file():
    pass



