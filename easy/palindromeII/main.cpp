#include <iostream>
#include <string>
#include <cctype>

class Solution
{
public:
    bool validPalindrome(std::string s)
    {
        int i = 0;
        int j = s.size() - 1;

        while (i < j)
        {
            char first_char = s[i];
            char last_char = s[j];
            if (!isalnum(first_char))
            {
                i++;
                continue;
            }
            if (!isalnum(last_char))
            {
                j--;
                continue;
            }

            if (tolower(first_char) != tolower(last_char))
            {
                return isPalindrome(s, i + 1, j) || isPalindrome(s, i, j - 1);
            }
            i++;
            j--;
        }
        return true;
    }

    bool isPalindrome(std::string s, int i, int j)
    {
        while (i < j)
        {
            if (s[i] == s[j])
            {
                i++;
                j--;
            }
            else
            {
                return false;
            }
        }
        return true;
    }
};

int main(void)
{
    Solution checker;
    std::cout << checker.validPalindrome("aba") << "\n";
}