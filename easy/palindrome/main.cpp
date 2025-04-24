#include <string>
#include <cctype>

class Solution
{
public:
    bool isPalindrome(std::string s)
    {
        int first = 0;
        int last = s.size() - 1;

        while (first < last)
        {
            char first_char = s[first];
            char last_char = s[last];
            if (!isalnum(first_char))
            {
                first++;
                continue;
            }
            if (!isalnum(last_char))
            {
                last--;
                continue;
            }
            if (tolower(first_char) != tolower(last_char))
            {
                return false;
            }
            first++;
            last--;
        }
        return true;
    }
};