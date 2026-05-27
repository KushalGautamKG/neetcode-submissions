from typing import List
import collections
from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # If endWord isn't even available, impossible
        if endWord not in wordList:
            return 0

        # Build pattern -> words map (e.g., h*t -> [hot, hit])
        buckets = collections.defaultdict(list)
        wordList = list(set(wordList))  # optional dedupe
        wordList.append(beginWord)

        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                buckets[pattern].append(word)

        # BFS
        q = deque([beginWord])
        visited = set([beginWord])
        steps = 1

        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return steps
                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i+1:]
                    for next_word in buckets[pattern]:
                        if next_word not in visited:
                            visited.add(next_word)
                            q.append(next_word)
                    # Optional small optimization: clear to avoid reprocessing
                    buckets[pattern] = []
            steps += 1

        return 0




        return 0

        