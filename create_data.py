import sys, os
from _pytest.tmpdir import tmp_path
sys.path.append(os.path.dirname(os.path.abspath("../Aechive/rfc7501.txt")))
from tree import Tree


tree = Tree()


def create_tree():
    with open(os.path.abspath("../Aechive/our_text.txt"))as file:
        sentences = []
        for line in file.readlines():
            if line == "\n":
                continue
            sentences.append(line)

        tree.formTree(sentences)
        print(tree.positions)


def write_to_file():
    pass


if __name__ == "__main__":
    create_tree()




