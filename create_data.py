import sys, os
from _pytest.tmpdir import tmp_path
sys.path.append(os.path.dirname(os.path.abspath("../Aechive/rfc7501.txt")))
from tree import Tree
from config import file_
from auto_complete_data import AutoCompleteData


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
                    # clean_line =
                    auto_complete_data = AutoCompleteData(line,  f'{file_path} {i}', 0, 0)
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
    tree.formTree(all_lines)


def write_to_file():
    pass


if __name__ == "__main__":
    # open_files()
    # get_files()
    # non_ascii_string = "a♥"
    # is_ascii = ".   \n"
    # check_non_ascii_string = non_ascii_string.isascii()
    # check_non_ascii_string_1 = is_ascii.isascii()
    # print(check_non_ascii_string)
    # print(check_non_ascii_string_1)
    # print(".kn".isalpha())
    # print("***********")
    # a_string = "123f"
    #
    # a_string_lowercase = a_string.lower()
    # contains_letters = a_string_lowercase.islower()
    # print(contains_letters)
    create_tree()



