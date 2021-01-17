from auto_complete_data import AutoCompleteData
from create_data import insert_to_dict, data_dict


def get_best_k_completions(prefix: str):
    insert_to_dict()
    auto_complete_data_list = []

    if prefix in data_dict.keys():
        auto_complete_data_list = data_dict[prefix]

    # completed_sentence: str
    # source_text: str
    # offset: int
    # score: int

    # auto_complete_data = AutoCompleteData()
    return auto_complete_data_list


if __name__ == "__main__":
    insert_to_dict()
    for key in data_dict.keys():
        print(key, ": ", data_dict[key])
