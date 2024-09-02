def read_board(filename):
    """
    Reads the sudoku board from a file.
    
    Args:
        filename (str): The name of the file containing the sudoku board.
    
    Returns:
        list: A 2D list representing the sudoku board.
    """
    with open(filename, 'r') as file:
        board = [list(map(int, line.split())) for line in file]
    return board

def is_valid(board, row, col, num):
    """Checks if it's valid to place a number in a specific cell on the board."""
    # Check row, column, and 3x3 block
    block_row, block_col = 3 * (row // 3), 3 * (col // 3)
    if any(board[row][c] == num for c in range(9)) or any(board[r][col] == num for r in range(9)):
        return False
    if any(board[r][c] == num for r in range(block_row, block_row + 3) for c in range(block_col, block_col + 3)):
        return False
    if row == col and any(board[i][i] == num for i in range(9)):
        return False
    if row + col == 8 and any(board[i][8-i] == num for i in range(9)):
        return False
    return True

def select_unassigned_variable(board):
    """
    Selects the unassigned cell with the least options to try (minimum remaining values heuristic).
    
    Args:
        board (list): The sudoku board.
        
    Returns:
        tuple: Row and column indices and the list of possible numbers for the cell.
    """
    min_options = 10  # More than the maximum number of options (1-9)
    best_cell = None
    best_degree = -1 
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                options = [num for num in range(1, 10) if is_valid(board, r, c, num)]
                num_options = len(options)
                if num_options < min_options:
                    min_options = num_options
                    best_cell = (r, c, options)
                    best_degree = sum((1 for nr in range(9) if board[nr][c] != 0)) + sum((1 for nc in range(9) if board[r][nc] != 0))
                elif num_options == min_options:
                    degree = sum((1 for nr in range(9) if board[nr][c] != 0)) + sum((1 for nc in range(9) if board[r][nc] != 0))
                    if degree > best_degree:
                        best_cell = (r, c, options)
                        best_degree = degree
    return best_cell

def solve_sudoku(board):
     #Solves the sudoku puzzle using a backtracking algorithm.
    
    cell = select_unassigned_variable(board)
    if not cell:
        return True  # Puzzle solved
    row, col, options = cell

    for num in options:
        board[row][col] = num
        if solve_sudoku(board):
            return True
        board[row][col] = 0
    return False


def write_board(board, filename):
    """
    Writes the sudoku board to a file.
    
    Args:
        board (list): The sudoku board.
        filename (str): The name of the output file.
    """
    with open(filename, 'w') as file:
        for row in board:
            file.write(' '.join(map(str, row)) + '\n')

def main():
    """
    Main function to read the board, solve the sudoku, and write the solution to a file.
    """
    input_board = read_board('input.txt')
    if solve_sudoku(input_board):
        write_board(input_board, 'output.txt')
    else:
        print("No solution exists for the given sudoku.")

if __name__ == '__main__':
    main()
