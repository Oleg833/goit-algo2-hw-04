from trie import Trie

class Homework(Trie):
    def count_words_with_suffix(self, pattern) -> int:
        if not isinstance(pattern, str):
            raise TypeError("Pattern must be a string")
        
        words = self.keys()
        return sum(1 for word in words if word.endswith(pattern))

    def has_prefix(self, prefix) -> bool:
        if not isinstance(prefix, str):
            raise TypeError("Prefix must be a string")
        
        return any(word.startswith(prefix) for word in self.keys())

if __name__ == "__main__":
    trie = Homework()
    words = ["apple", "application", "banana", "cat"]
    for i, word in enumerate(words):
        trie.put(word, i)

    # Testing count_words_with_suffix
    assert trie.count_words_with_suffix("e") == 1  # apple
    assert trie.count_words_with_suffix("ion") == 1  # application
    assert trie.count_words_with_suffix("a") == 1  # banana
    assert trie.count_words_with_suffix("at") == 1  # cat

    # Testing has_prefix
    assert trie.has_prefix("app") is True  # apple, application
    assert trie.has_prefix("bat") is False  # no match
    assert trie.has_prefix("ban") is True  # banana
    assert trie.has_prefix("ca") is True  # cat

    print("All tests passed!")
