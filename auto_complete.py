from auto_complete_data import AutoCompleteData
from create_data import create_tree, tree
from util import replacer, update_score


def get_best_k_completions(prefix: str):
    auto_complete_data_list = tree.get_all_auto_suggestions(prefix)
    if len(auto_complete_data_list) > 0:
        update_score(auto_complete_data_list, len(prefix))

    # perfect match
    if len(auto_complete_data_list) >= 5:
        return auto_complete_data_list

    # replaced letter matches
    for i in range(len(prefix) - 1, -1, -1):
        # print(i)
        replaced_options = get_replaced_options(prefix, i)
        # print(replaced_options)
        for option in replaced_options:
            temp_auto_complete_data_list = tree.get_all_auto_suggestions(option)
            if len(temp_auto_complete_data_list) > 0:
                update_score(temp_auto_complete_data_list, len(prefix), i, True)
            auto_complete_data_list += remove_existing_sentences(auto_complete_data_list, temp_auto_complete_data_list)
            if len(auto_complete_data_list) >= 5:
                return auto_complete_data_list

    # delete letter
    for i in range(len(prefix) - 1, -1, -1):
        temp_auto_complete_data_list = tree.get_all_auto_suggestions(replacer(prefix, '', i))
        if len(temp_auto_complete_data_list) > 0:
            update_score(temp_auto_complete_data_list, len(prefix), i)
        auto_complete_data_list += remove_existing_sentences(auto_complete_data_list, temp_auto_complete_data_list)
        if len(auto_complete_data_list) >= 5:
            return auto_complete_data_list

    # add letter
    for i in range(len(prefix), -1, -1):
        add_letter_options = get_add_letter_options(prefix, i)
        for option in add_letter_options:
            temp_auto_complete_data_list = tree.get_all_auto_suggestions(option)
            if len(temp_auto_complete_data_list) > 0:
                update_score(temp_auto_complete_data_list, len(prefix), i)
            auto_complete_data_list += remove_existing_sentences(auto_complete_data_list, temp_auto_complete_data_list)
            if len(auto_complete_data_list) >= 5:
                return auto_complete_data_list

    return auto_complete_data_list


def get_replaced_options(prefix, index):
    replacement_letters = {
        'a': ['q', 'w', 's', 'z', 'e', 'i', 'u', 'o'],
        'b': ['v', 'g', 'h', 'n'],
        'c': ['x', 'd', 'f', 'v'],
        'd': ['s', 'e', 'r', 'f', 'c', 'x'],
        'e': ['w', 'r', 'd', 's', 'a', 'i', 'u', 'o'],
        'f': ['d', 'r', 't', 'g', 'v', 'c'],
        'g': ['f', 't', 'y', 'h', 'b', 'v', 'p'],
        'h': ['g', 'y', 'u', 'j', 'n', 'b'],
        'i': ['u', 'o', 'k', 'j', 'a', 'e'],
        'j': ['u', 'i', 'k', 'm', 'n', 'h'],
        'k': ['u', 'i', 'k', 'm', 'n', 'h', 'c'],
        'l': ['k', 'o', 'p'],
        'm': ['k', 'j', 'n'],
        'n': ['b', 'h', 'j', 'm'],
        'o': ['i', 'p', 'l', 'k', 'u', 'a', 'e'],
        'p': ['o', 'l', 'f'],
        'q': ['a', 'w', 'k'],
        'r': ['e', 't', 'f', 'd'],
        's': ['a', 'w', 'e', 'd', 'x', 'z', 'c'],
        't': ['r', 'y', 'g', 'f'],
        'u': ['y', 'i', 'j', 'h', 'a', 'i', 'o'],
        'v': ['c', 'f', 'g', 'b'],
        'w': ['q', 'a', 's', 'e'],
        'x': ['z', 's', 'd', 'c'],
        'y': ['t', 'u', 'h', 'g'],
        'z': ['a', 's', 'x']
    }
    # print("get_replaced_options: ", prefix, index)
    letter = prefix[index]
    replacement_options = []

    if not replacement_letters.get(letter):
        return replacement_options
    for l in replacement_letters[letter]:
        option = replacer(prefix, l, index)
        replacement_options.append(option)

    return replacement_options


def get_add_letter_options(prefix, index):
    vowels = ['a', 'e', 'i', 'u', 'o', 'ie', 'y']
    silent_letters = ['gh', 'b', 'w', 'l', 'n', 't', 'c']
    silent_letters_start = ['p', 'k']
    letters = ['d', 'f', 'g', 'h', 'j', 'k', 'm', 'p', 'q', 'r', 's', 'w', 'x', 'z']

    added_letters_options = []

    for letter in vowels:
        added_letters_options.append(prefix[:index] + letter + prefix[index:])

    for letter in silent_letters:
        added_letters_options.append(prefix[:index] + letter + prefix[index:])

    if index == 0:
        for letter in silent_letters_start:
            added_letters_options.append(prefix[:index] + letter + prefix[index:])

    for letter in letters:
        added_letters_options.append(prefix[:index] + letter + prefix[index:])

    return added_letters_options


def remove_existing_sentences(old_auto_complete_data_list, new_auto_complete_data_list):
    auto_complete_data_list = []
    in_old_list = False
    for new_auto_complete_item in new_auto_complete_data_list:
        for old_new_auto_complete_item in old_auto_complete_data_list:
            if new_auto_complete_item.source_text == old_new_auto_complete_item.source_text:
                in_old_list = True
                break

        if not in_old_list:
            auto_complete_data_list.append(new_auto_complete_item)
        in_old_list = False
    return auto_complete_data_list


if __name__ == "__main__":
    auto_complete_list = []
    auto_complete_list.append(AutoCompleteData("aaa aaa", "a 1", 0, 0))
    auto_complete_list.append(AutoCompleteData("aaa bbb", "a 2", 0, 0))
    auto_complete_list.append(AutoCompleteData("bbb bbb", "b 1", 0, 0))

    new_auto_complete_list = []
    new_auto_complete_list.append(AutoCompleteData("aaa aaa", "b 2", 0, 0))
    new_auto_complete_list.append(AutoCompleteData("aaa bbb", "a 2", 0, 0))
    new_auto_complete_list.append(AutoCompleteData("bbb bbb", "a 3", 0, 0))


    print(new_sentences(auto_complete_list, new_auto_complete_list))
