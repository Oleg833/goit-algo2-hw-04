from trie import Trie

class LongestCommonWord(Trie):
    def find_longest_common_word(self, strings):
        if not strings:  # Якщо вхідний список порожній
            return ""

        # Додаємо всі рядки у Trie
        for string in strings:
            self.put(string)

        # Знаходимо найдовший спільний префікс
        prefix = ""
        current = self.root

        while current:
            # Перевіряємо, чи є лише один дочірній вузол
            if len(current.children) == 1 and current.value is None:
                char = next(iter(current.children))  # Отримуємо єдиного дочірнього вузла
                prefix += char
                current = current.children[char]
            else:
                break

        return prefix

if __name__ == "__main__":
    # Тести
    trie = LongestCommonWord()
    strings = ["flower", "flow", "flight"]
    assert trie.find_longest_common_word(strings) == "fl"

    trie = LongestCommonWord()
    strings = ["interspecies", "interstellar", "interstate"]
    assert trie.find_longest_common_word(strings) == "inters"

    trie = LongestCommonWord()
    strings = ["dog", "racecar", "car"]
    assert trie.find_longest_common_word(strings) == ""

    print("Усі тести пройдено!")
