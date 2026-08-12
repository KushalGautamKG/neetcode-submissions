from typing import List

def contains_duplicate(words: List[str]) -> bool:
    i = 0
    while i < len(words):
        j = i + 1
        while j < len(words):
            if words[i] == words[j]:
                return True
            j += 1
        i += 1
    return False


# do not modify code below this line
print(contains_duplicate(["hello", "world", "hello"]))
print(contains_duplicate(["hello", "world", "i", "am", "great"]))
print(contains_duplicate(["hello", "hello", "hello"]))
print(contains_duplicate(["Hello", "hellooo", "hello"]))
