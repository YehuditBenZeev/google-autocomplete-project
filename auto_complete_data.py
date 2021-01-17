from dataclasses import dataclass


@dataclass
class AutoCompleteData:
    completed_sentence: str
    source_text: str
    offset: int
    score: int
    # methods that you need to define by yourself

    def __str__(self):
        return self.completed_sentence

    def __hash__(self):
        #print(hash(str(self)))
        return hash(str(self))

    # def __eq__(self,other):
    #     return self.name == other.name and self.age== other.age


@dataclass
class SentenceData:
   # completed_sentence: str
    source_file: str
    line: int
