// This algorithm failed
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
        long int traverser = 0;

        while (original_number > 0)
        {
            int final_digit = original_number % 10;
            int first_digit;
            long int another_original_number = x;
            while (another_original_number >= traverser)
            {
                first_digit = another_original_number % 10;
                another_original_number /= 10;
            }
            if (final_digit != first_digit)
            {
                return false;
            }
            original_number /= 10;
            if (traverser == 0)
            {
                traverser = 10;
            }
            else
            {
                traverser *= 10;
            }
        }
        return true;
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