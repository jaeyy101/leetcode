from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        t_counter = Counter(t)
        window_counter = {}
        have, need = 0, len(t_counter)
        res = [-1, -1]
        res_len = float("inf")
        left = 0

        for right in range(len(s)):
            char = s[right]
            window_counter[char] = window_counter.get(char, 0) + 1

            if char in t_counter and window_counter[char] == t_counter[char]:
                have += 1

            while have == need:
                if (right - left + 1) < res_len:
                    res = [left, right]
                    res_len = right - left + 1

                window_counter[s[left]] -= 1
                if (
                    s[left] in t_counter
                    and window_counter[s[left]] < t_counter[s[left]]
                ):
                    have -= 1
                left += 1

        l, r = res
        return s[l : r + 1] if res_len != float("inf") else ""


print(Solution().minWindow("ADOBECODEBANC", "ABC"))
