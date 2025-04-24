#include <iostream>
#include <string>

class Solution
{
public:
    bool isPalindrome(int x)
    {
        if (x < 0)
        {
            return false;
        }

        if (x == 0)
        {
            return true;
        }

        long int original_number = x;
        long int reversed_number = 0;
        while (original_number > 0)
        {
            reversed_number = reversed_number * 10 + original_number % 10;
            original_number /= 10;
        }
        return x == reversed_number;
    }
};

int main(void)
{
    std::string input;
    std::cout << "NUMBER PALINDROME\nEnter a number: ";
    std::cin >> input;

    Solution sample;
    std::cout << sample.isPalindrome(std::stoi(input)) << "\n";
}