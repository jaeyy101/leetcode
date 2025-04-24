#include <iostream>
#include <string>

class Solution
{
public:
    bool valid_anagram(std::string s, std::string t)
    {
        return counter(s) == counter(t);
    }

    long int counter(std::string s)
    {
        long int total = 0;
        for (int i = 0, n = s.size(); i < n; i++)
        {
            total += (int)s[i];
        }

        return total;
    }
};

int main(void)
{
    Solution solution;
    std::string s, t;

    std::cout << "Enter first word: ";
    std::cin >> s;

    std::cout << "Enter second word: ";
    std::cin >> t;

    if (solution.valid_anagram(s, t))
    {
        std::cout << s << " is an anagram of " << t;
    }
    else
    {
        std::cout << s << " is not an anagram of " << t;
    }
    std::cout << "\n";
}