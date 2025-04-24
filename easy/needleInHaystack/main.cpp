#include <iostream>
#include <string>
#include <vector>

// My Solution
// class Solution
// {
// public:
//     int strStr(std::string haystack, std::string needle)
//     {
//         int n = haystack.size();
//         int m = needle.size();
//         if (m < 1 || n < m)
//         {
//             return -1;
//         }
//         for (int i = 0; i < n; i++)
//         {
//             int j = i;
//             int k = 0;
//             bool found = true;
//             while (j < n && k < m)
//             {
//                 if (haystack[j] != needle[k])
//                 {
//                     found = false;
//                     break;
//                 }
//                 j++;
//                 k++;
//             }
//             if (found && k == m)
//             {
//                 return i;
//             }
//         }
//         return -1;
//     }
// };

// Knuth-Morris-Pratt (KMP) algorithm
class Solution
{
public:
    std::vector<int> computeLPS(std::string needle)
    {
        int m = needle.size();
        std::vector<int> lps(m, 0);

        int len = 0;
        int i = 1;

        while (i < m)
        {
            if (needle[i] == needle[len])
            {
                len++;
                lps[i] = len;
                i++;
            }
            else
            {
                if (len != 0)
                {
                    len = lps[len - 1];
                }
                else
                {
                    lps[i] = 0;
                    i++;
                }
            }
        }
        return lps;
    }

    int strStr(std::string haystack, std::string needle)
    {
        int n = haystack.size();
        int m = needle.size();
        if (m == 0)
            return 0;
        if (n < m)
            return -1;

        std::vector<int> lps = computeLPS(needle);
        for (int i = 0; i < lps.size(); i++)
        {
            std::cout << lps[i] << " ";
        }
        std::cout << "\n";
        int i = 0, j = 0;

        while (i < n)
        {
            if (haystack[i] == needle[j])
            {
                i++;
                j++;
            }
            if (j == m)
            {
                return i - j; // Found needle at index (i - j)
            }
            else if (i < n && haystack[i] != needle[j])
            {
                if (j != 0)
                {
                    j = lps[j - 1]; // Use LPS to skip redundant checks
                }
                else
                {
                    i++;
                }
            }
        }
        return -1;
    }
};

int main(void)
{
    Solution solution;
    std::cout << solution.strStr("ababcabcabababd", "ababd") << "\n";
}