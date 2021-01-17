import sys, os
from _pytest.tmpdir import tmp_path
sys.path.append(os.path.dirname(os.path.abspath("../Aechive/rfc7501.txt")))


data_dict = {}


def insert_to_dict():
    with open(os.path.abspath("../Aechive/our_text.txt"))as file:
        for line in file.readlines():
            if line == "\n":
                continue

            # nurmelaized line
            key = line[:5]
            if not (key in data_dict.keys()):
                data_dict[key] = []
            data_dict[key].append(line)


def write_to_file():
    pass


if __name__ == "__main__":
    insert_to_dict()
    for key in data_dict.keys():
        print(key, ": ", data_dict[key])



