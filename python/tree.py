from auto_complete_data import SentenceData
from util import get_clean_sentence, get_shortened_sentence, from_sentence_to_auto_complete
import json


class TrieNode:
    def __init__(self):
        # Initialising one node for trie
        self.children = {}
        self.last = False
        self.sentence_data_list = []


class Tree:
    def __init__(self):
        # Initialising the trie structure.
        self.root = TrieNode()
        self.sentence_list = []
        self.positions = {}

    def formTree(self, sentence_data_list):
        """ Forms a trie structure with the given set of strings
        if it does not exists already else it merges the key
        into it by extending the structure as required"""
        for sentence_data_item in sentence_data_list:
            self.insert(sentence_data_item)  # inserting one key to the trie.
            # sentence_item = SentenceData(completed_sentence=sentence, line=line, source_file='')

    def insert(self, sentence_data_item):
        """Inserts a key into trie if it does not exist already.
        And if the key is a prefix of the trie node, just
        marks it as leaf node."""

        node_current = self.root
        sentence = get_clean_sentence(sentence_data_item.completed_sentence)
        short_sentence = get_shortened_sentence(sentence, 5)
        word_list = short_sentence.split()
        for i, word in enumerate(word_list):
            if i != len(word_list) - 1:
                word = word + ' '
            for letter in word:
                if not node_current.children.get(letter):
                    node_current.children[letter] = TrieNode()

                node_current = node_current.children[letter]

                if word[0] == letter:
                    if not (word[0] in self.positions.keys()):
                        self.positions[word[0]] = set()
                    self.positions[word[0]].add(node_current)


        node_current.last = True
        node_current.sentence_data_list.append(SentenceData(sentence_data_item.completed_sentence, sentence_data_item.source_text))

    def get_all_auto_suggestions(self, sentence):
        self.sentence_list = []
        if len(sentence) > 0:
            if self.positions.get(sentence[0]):
                for node in self.positions[sentence[0]]:
                    temp_root = TrieNode()
                    temp_root.children[sentence[0]] = node
                    self.get_node_auto_suggestions(sentence, temp_root)

        return from_sentence_to_auto_complete(self.sentence_list)

    def get_node_auto_suggestions(self, sentence, node):
        not_found = False

        for i, letter in enumerate(sentence):
            if not node.children.get(letter):
                not_found = True
                break

            node = node.children[letter]
        if not_found:
            return 0
        elif node.last and not node.children:
            return -1

        self.get_complete_suggestion(node)
        return 1

    def get_complete_suggestion(self, node):
        if node.last:
            for item in node.sentence_data_list:
                self.sentence_list.append(item)
            return

        for letter, n in node.children.items():
            self.get_complete_suggestion(n)
