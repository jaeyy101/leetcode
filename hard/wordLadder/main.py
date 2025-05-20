from typing import List
from collections import deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0

        beginSet = set([beginWord])
        endSet = set([endWord])
        visited = set()
        wordLen = len(beginWord)
        steps = 1

        while beginSet and endSet:
            # Always expand the smaller set for efficiency
            if len(beginSet) > len(endSet):
                beginSet, endSet = endSet, beginSet

            nextSet = set()
            for word in beginSet:
                for i in range(wordLen):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        newWord = word[:i] + c + word[i + 1 :]
                        if newWord in endSet:
                            return steps + 1
                        if newWord in wordSet and newWord not in visited:
                            nextSet.add(newWord)
                            visited.add(newWord)
            beginSet = nextSet
            steps += 1

        return 0

    def ladderLength1(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        if endWord not in words:
            return 0

        queue = deque([(beginWord, 1)])
        while queue:
            word, n = queue.popleft()
            if word == endWord:
                return n
            for i in range(len(word)):
                for j in range(ord("a"), ord("z") + 1):
                    new_word = word[:i] + chr(j) + word[i + 1 :]
                    if new_word in words:
                        queue.append((new_word, n + 1))
                        words.remove(new_word)
        return 0
