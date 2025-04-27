class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        board_size = 9

        # List of sets for Columns
        columns = [set() for _ in range(board_size)]

        # List of sets for 3x3 boxes
        boxes = [set() for _ in range(board_size)]
        box_size = 3

        for i in range(board_size):

            # Set for each row
            unique = set()

            for j in range(board_size):
                if board[i][j].isdigit():

                    # Calculating the box index from i and j
                    box_index = box_size * (i // box_size) + (j // box_size)

                    # Returning false if current digit is a replication
                    if (
                        board[i][j] in unique
                        or board[i][j] in columns[j]
                        or board[i][j] in boxes[box_index]
                    ):
                        return False

                    # Adding digit to sets
                    unique.add(board[i][j])
                    columns[j].add(board[i][j])
                    boxes[box_index].add(board[i][j])

        # Return True if no problems are found
        return True


print(
    Solution().isValidSudoku(
        [
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
        ]
    )
)
