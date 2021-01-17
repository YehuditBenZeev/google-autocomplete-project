
class TrieNode:
    def __init__(self):
        # Initialising one node for trie
        self.children = {}
        self.last = False
        self.father = None
        self.father_letter = ''


class Tree:
    def __init__(self):
        # Initialising the trie structure.
        self.root = TrieNode()
        self.sentence_list = []
        self.positions = {}

    def formTree(self, keys_):
        # Forms a trie structure with the given set of strings
        # if it does not exists already else it merges the key
        # into it by extending the structure as required
        for key_ in keys_:
            self.insert(key_)  # inserting one key to the trie.

    def insert(self, sentence):
        # Inserts a key into trie if it does not exist already.
        # And if the key is a prefix of the trie node, just
        # marks it as leaf node.


        node_current = self.root
        node_father = self.root
        father_letter = ''
        for i, letter in enumerate(sentence):
            if not node_current.children.get(letter):
                node_current.children[letter] = TrieNode()

            node_current.father = node_father
            node_current.father_letter = father_letter
            node_father = node_current
            node_current = node_current.children[letter]
            father_letter = letter

            if not (letter in self.positions.keys()):
                self.positions[letter] = set()
            self.positions[letter].add(node_current)

        node_current.last = True

    def search(self, key_):
        # Searches the given key in trie for a full match
        # and returns True on success else returns False.
        node = self.root
        found = True

        # for a in list(key):
        for i, a in enumerate(key_):
            print(i, ", ", a, end=", ")
            if not node.children.get(a):
                found = False
                break
            node = node.children[a]
            print(" ")
        print(" ")

        return node and node.last and found


    def suggestionsRecBackwords(self, node, word):
        if node.father == self.root:
            return node.father_letter + word

        return self.suggestionsRecBackwords(node.father, node.father_letter + word)

    def suggestionsRec(self, original_node, node, word):
        if node.last:
            prefix = self.suggestionsRecBackwords(original_node, '')
            sentence = prefix[:-2] + word
            self.sentence_list.append(sentence)

        for a, n in node.children.items():
            self.suggestionsRec(original_node, n, word + a)

    def printAllAutoSuggestions(self, sentence):
        return_value = 1
        for node in self.positions[sentence[0]]:
            temp_root = TrieNode()
            temp_root.children[sentence[0]] = node
            return_value = self.printAutoSuggestions(sentence, temp_root)
            if return_value == 1:
                break
        for s in self.sentence_list:
            print(s)
        return return_value

    def printAutoSuggestions(self, key_, node):
        # Returns all the words in the trie whose common
        # prefix is the given key thus listing out all
        # the suggestions for autocomplete.

        # node = self.root
        not_found = False
        temp_word = ''

        # for a in list(key_):
        for i, a in enumerate(key_):
            if not node.children.get(a):
                not_found = True
                break

            temp_word += a
            node = node.children[a]
        if not_found:
            return 0
        elif node.last and not node.children:
            return -1
        print("132")
        self.suggestionsRec(node, node, temp_word)

        return 1


if __name__ == "__main__":
    # Driver Code
    keys = ["hello dog", "dog", "t dog hell", "cat", "a",  # "t dog hell"
            "hel", "help", "helps", "helping"]  # keys to form the trie structure.
    key = "do"  # key for autocomplete suggestions.
    status = ["Not found", "Found"]

    # creating trie object
    t = Tree()

    # creating the trie structure with the
    # given set of strings.
    t.formTree(keys)
    print(t.positions)


    # autocompleting the given key using
    # our trie structure.
    comp = t.printAllAutoSuggestions(key)

    if comp == -1:
        print("No other strings found with this prefix\n")
    elif comp == 0:
        print("No string found with this prefix\n")

    # This code is contributed by amurdia
