import sys, os
from _pytest.tmpdir import tmp_path
sys.path.append(os.path.dirname(os.path.abspath("../Aechive/rfc7501.txt")))
from tree import Tree
from config import file_path

tree = Tree()

def get_files():
    data_dir_list =[]#= [directory[0]+'/'+directory[1]+'/'for directory in os.walk(f'Aechive')]
    for root, directories, files in os.walk('Aechive'):
        file_path = root + '/'
        for file in files:
            data_dir_list.append(file_path+'/'+file)
    return data_dir_list


def open_files():
    data_file_list = get_files()
    all_lines = []
    for file_path in data_file_list:
        with open(os.path.abspath(file_path), encoding="utf8")as file:
            for line in file.readlines():
                if line == "\n":
                    continue
                all_lines.append(line)
    print(len(all_lines))
    

def create_tree():
    with open(os.path.abspath(file_path))as file:
        sentences = []
        for line in file.readlines():
            if line == "\n":
                continue
            line = line.replace('\n', '')
            sentences.append(line)

        tree.formTree(sentences)
        print(tree.positions)


def write_to_file():
    pass


if __name__ == "__main__":
    open_files()




