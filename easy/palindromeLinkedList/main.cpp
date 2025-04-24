#include <iostream>
#include <cstdlib>

typedef struct Node
{
    int val;
    Node *next;
} Node;

class Solution
{
public:
    bool isPalindrome(Node *list)
    {
        Node *head = list;
        Node *slow = head;
        Node *fast = head->next;

        while (fast != nullptr && fast->next != nullptr)
        {
            slow = slow->next;
            fast = fast->next->next;
        }

        Node *left = head;
        Node *right = slow->next;

        Node *right_reversed = reverse_list(right);
        Node *left_temp = left;
        Node *right_reversed_temp = right_reversed;

        while (left != nullptr && right_reversed != nullptr)
        {
            std::cout << "Checking if left: " << left->val << " is equal right: " << right_reversed->val << "\n";
            if (left->val != right_reversed->val)
            {
                freeList(left_temp);
                freeList(right_reversed_temp);
                return false;
            }
            left = left->next;
            right_reversed = right_reversed->next;
        }
        freeList(left_temp);
        freeList(right_reversed_temp);
        return true;
    }

    Node *reverse_list(Node *head)
    {
        Node *prev = nullptr;
        Node *current = head;
        Node *next = nullptr;

        while (current != nullptr)
        {
            next = current->next;
            current->next = prev;
            prev = current;
            current = next;
        }
        return prev;
    }

    void freeList(Node *head)
    {
        if (head == nullptr)
        {
            return;
        }
        freeList(head->next);
        free(head);
    }
};

int main(void)
{
    Node *head = (Node *)malloc(sizeof(Node));
    head->val = 1;
    Node *first = (Node *)malloc(sizeof(Node));
    first->val = 1;
    Node *second = (Node *)malloc(sizeof(Node));
    second->val = 2;
    Node *last = (Node *)malloc(sizeof(Node));
    last->val = 1;
    head->next = first;
    first->next = second;
    second->next = last;

    Solution ll;
    std::cout << ll.isPalindrome(head) << "\n";
}
