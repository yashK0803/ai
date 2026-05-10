def print_board(board):
    for row in board:
        print(" ".join("Q" if cell else "." for cell in row))
    print()


def solve_n_queens_backtracking(n):
    board = [[0] * n for _ in range(n)]
    solutions = []

    def is_safe(row, col):
        for i in range(col):
            if board[row][i] == 1:
                return False

        i, j = row, col

        while i >= 0 and j >= 0:
            if board[i][j] == 1:
                return False

            i -= 1
            j -= 1

        i, j = row, col

        while i < n and j >= 0:
            if board[i][j] == 1:
                return False

            i += 1
            j -= 1

        return True

    def backtrack(col):
        if col == n:
            solutions.append([row[:] for row in board])
            return

        for row in range(n):
            if is_safe(row, col):
                board[row][col] = 1

                backtrack(col + 1)

                board[row][col] = 0

    backtrack(0)

    return solutions


def solve_n_queens_branch_and_bound(n):
    board = [[0] * n for _ in range(n)]

    solutions = []

    rows = [False] * n
    upper_diagonal = [False] * (2 * n - 1)
    lower_diagonal = [False] * (2 * n - 1)

    def branch_and_bound(col):
        if col == n:
            solutions.append([row[:] for row in board])
            return

        for row in range(n):
            upper_index = row + col
            lower_index = n - 1 + col - row

            if (
                not rows[row]
                and not upper_diagonal[upper_index]
                and not lower_diagonal[lower_index]
            ):
                board[row][col] = 1

                rows[row] = True
                upper_diagonal[upper_index] = True
                lower_diagonal[lower_index] = True

                branch_and_bound(col + 1)

                board[row][col] = 0

                rows[row] = False
                upper_diagonal[upper_index] = False
                lower_diagonal[lower_index] = False

    branch_and_bound(0)

    return solutions


def main():
    n = 4

    print("Constraint Satisfaction Problem: N-Queens")
    print(f"Number of queens: {n}\n")

    backtracking_solutions = solve_n_queens_backtracking(n)

    print("Solutions using Backtracking:")

    for index, solution in enumerate(backtracking_solutions, start=1):
        print(f"Solution {index}:")
        print_board(solution)

    branch_bound_solutions = solve_n_queens_branch_and_bound(n)

    print("Solutions using Branch and Bound:")

    for index, solution in enumerate(branch_bound_solutions, start=1):
        print(f"Solution {index}:")
        print_board(solution)

    print(
        f"Total solutions using Backtracking: "
        f"{len(backtracking_solutions)}"
    )

    print(
        f"Total solutions using Branch and Bound: "
        f"{len(branch_bound_solutions)}"
    )


if __name__ == "__main__":
    main()