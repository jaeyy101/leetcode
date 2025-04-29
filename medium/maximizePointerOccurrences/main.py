class Solution:
    def maximizePointerOccurences(self, pointer: str, combinations: int) -> int:
        n = len(pointer)
        if n > combinations:
            return 0
        if n == combinations:
            return 1
        # Compute LPS
        lps = [0] * n
        i = 1
        needle_len = 0

        while i < n:
            if pointer[i] == pointer[needle_len]:
                needle_len += 1
                lps[i] = needle_len
                i += 1
            else:
                if needle_len == 0:
                    lps[i] = 0
                    i += 1
                else:
                    needle_len = lps[needle_len - 1]

        longest_suffix_prefix = lps[-1]
        no_overlaps = n - longest_suffix_prefix
        print(no_overlaps)

        return 1 + (combinations - n) // no_overlaps


print(Solution().maximizePointerOccurences("baaaaa", 28))
