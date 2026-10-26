class WordIterator:
    def __init__(self, words):
        self.words = words
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.words):
            raise StopIteration

        word = self.words[self.index]
        self.index += 1
        return word


words = ["Python", "Java", "C++", "JavaScript"]

iterator = WordIterator(words)

for word in iterator:
    print(word)
