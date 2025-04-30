from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # Time complexity O(n*klogk)
        words_map = defaultdict(list)
        for word in strs:
            sorted_word = "".join(sorted(word))
            words_map[sorted_word].append(word)

        return list(words_map.values())

    def groupAnagrams1(self, strs: list[str]) -> list[list[str]]:
        words_map = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord("a")] += 1

            words_map[tuple(count)].append(word)

        print(words_map)
        return list(words_map.values())


print(Solution().groupAnagrams1(["bar", "foo", "ate", "eat"]))
