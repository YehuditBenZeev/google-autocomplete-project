from auto_complete_data import SentenceData, AutoCompleteData
from util import get_clean_line


class TrieNode:
    def __init__(self):
        # Initialising one node for trie
        self.children = {}
        self.last = False
        self.father = None
        self.father_letter = ''
        self.sentence_item = None


class Tree:
    def __init__(self):
        # Initialising the trie structure.
        self.root = TrieNode()
        self.sentence_list = []
        self.positions = {}

    def formTree(self, auto_complete_data_list):
        """ Forms a trie structure with the given set of strings
        if it does not exists already else it merges the key
        into it by extending the structure as required"""
        for auto_complete_data_item in auto_complete_data_list:
            self.insert(auto_complete_data_item)  # inserting one key to the trie.
            #sentence_item = SentenceData(completed_sentence=sentence, line=line, source_file='')

    def insert(self, auto_complete_data_item):
        """Inserts a key into trie if it does not exist already.
        And if the key is a prefix of the trie node, just
        marks it as leaf node."""
        # print("insert")
        node_current = self.root
        node_father = self.root
        father_letter = ''
        sentence = get_clean_line(auto_complete_data_item.completed_sentence)
        for i, letter in enumerate(sentence):
            if not node_current.children.get(letter):
                node_current.children[letter] = TrieNode()

            node_current = node_current.children[letter]
            node_current.father = node_father
            node_current.father_letter = father_letter

            node_father = node_current           
            father_letter = letter

            if not (letter in self.positions.keys()):
                self.positions[letter] = set()
            self.positions[letter].add(node_current)

        node_current.last = True
        node_current.sentence_item = auto_complete_data_item

    def search(self, sentence):
        # Searches the given key in trie for a full match
        # and returns True on success else returns False.
        node = self.root
        found = True

        # for a in list(key):
        for i, a in enumerate(sentence):
            print(i, ", ", a, end=", ")
            if not node.children.get(a):
                found = False
                break
            node = node.children[a]
            print(" ")
        print(" ")

        return node and node.last and found

    def suggestions_rec_backwards(self, node, sentence):
        if node.father is None:
            return node.father_letter + sentence

        return self.suggestions_rec_backwards(node.father, node.father_letter + sentence)

    def suggestions_rec(self, original_node, node, sentence):
        if node.last:
            prefix = self.suggestions_rec_backwards(original_node, '')
            full_sentence = prefix + sentence
            # source_text = f"{node.sentence_item.source_file} {node.sentence_item.line}"
            # auto_complete_item = AutoCompleteData(source_text=source_text, completed_sentence=full_sentence, offset=0, score=0)
            self.sentence_list.append(node.sentence_item)

        for letter, n in node.children.items():
            self.suggestions_rec(original_node, n, sentence + letter)

    def get_all_auto_suggestions(self, sentence):
        self.sentence_list = []
        if len(sentence) > 0:
            if self.positions.get(sentence[0]):
                for node in self.positions[sentence[0]]:
                    temp_root = TrieNode()
                    temp_root.children[sentence[0]] = node
                    self.get_node_auto_suggestions(sentence, temp_root)

        return self.sentence_list

    def get_node_auto_suggestions(self, sentence, node):
        # Returns all the words in the trie whose common
        # prefix is the given key thus listing out all
        # the suggestions for autocomplete.

        not_found = False
        temp_word = ''
        first_node = node.children.get(sentence[0])
        # for a in list(key_):
        for i, letter in enumerate(sentence):
            if not node.children.get(letter):
                not_found = True
                break

            temp_word += letter
            node = node.children[letter]
        if not_found:
            return 0
        elif node.last and not node.children:
            return -1
        self.suggestions_rec(first_node, node, temp_word)

        return 1


if __name__ == "__main__":
    # # Driver Code
    # keys = ["dog dog", "hello dog", "t dog hell", "dog", "dog hi", "doggi dog"]
    #         #"hel", "help", "helps", "helping"]  # keys to form the trie structure.
    # key = "do"  # key for autocomplete suggestions.
    # status = ["Not found", "Found"]
    #
    # # creating trie object
    # t = Tree()
    #
    # # creating the trie structure with the
    # # given set of strings.
    # t.formTree(keys)
    # #print(t.positions)
    #
    #
    # # autocompleting the given key using
    # # our trie structure.
    # comp = t.get_all_auto_suggestions(key)
    # for s in set(comp):
    #         print(s)
    # if comp == -1:
    #     print("No other strings found with this prefix\n")
    # elif comp == 0:
    #     print("No string found with this prefix\n")
    #
    # # This code is contributed by amurdia
    # line = "buyhi      jkg@#$/.' f"
    # clean_line = get_clean_line(line)
    # print(line)
    # print(clean_line)
    pass