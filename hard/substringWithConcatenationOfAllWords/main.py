from collections import Counter


class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        """
        Remains incomplete
        """

        n = len(s)
        m = len(words)
        l = len(words[0])

        left = 0
        right = l
        output = []
        words_seen = Counter()
        word_count = Counter(words)
        count = 0
        while right < (n + 1):
            # Grab the current word
            word = s[left:right]

            # Checking if it's a valid word
            if word in word_count:

                # Checking if it's a word we've come across
                # if so, we modify the dictionary to change the indexes
                # using the index of the initial occurence of the word
                if word in words_map:
                    previous = words_seen[word]
                    for key in words_seen.copy():
                        if words_seen[key] <= previous:
                            del words_map[key]
                        else:
                            words_map[key] -= previous + 1

                    # Getting new index of word
                    words_map[word] = count - previous - 1
                    # Getting new count
                    count = words_map[word] + 1

                # Adding the word and it's index to the hashmap
                #  if it's not already there
                else:
                    words_map[word] = count
                    count += 1

                # Going on to check other words
                left += l
                right += l

            # If not a valid word
            else:
                if len(words_map.keys()) > 0:
                    left -= l
                    right -= l
                count = 0
                words_map = {}
                left += 1
                right += 1

            # If all the words have been found getting the beginning index
            if count == m:
                # - l * (m + 1) because of right += l above
                output.append(right - l * (m + 1))

        return output

    def findSubstring2(self, s: str, words: list[str]) -> list[int]:
        if not s or not words:
            return []

        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        word_count = Counter(words)
        result = []

        for i in range(word_len):
            left = i
            seen = Counter()
            for right in range(i, len(s) - word_len + 1, word_len):
                word = s[right : right + word_len]
                if word in word_count:
                    seen[word] += 1

                    while seen[word] > word_count[word]:
                        seen[s[left : left + word_len]] -= 1
                        left += word_len

                    if right + word_len - left == total_len:
                        result.append(left)
                else:
                    seen.clear()
                    left = right + word_len

        return result


# print(Solution().findSubstring("barfoofoobarthefoobarman", ["bar", "foo", "the"]))
print(
    Solution().findSubstring2(
        "wordgoodgoodgoodbestword", ["word", "good", "best", "good"]
    )
)
