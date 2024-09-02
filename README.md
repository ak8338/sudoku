# sudoku
Sudoku Project

Project Description: Implement the Backtracking Algorithm to solve X-Sudoku
puzzles. The rules of the game are:

• The game board consists of 9 × 9 cells divided into 3 × 3 non-overlapping blocks. Some of the cells already have numbers (1 to 9) assigned to them
initially.
• The goal is to find assignments (1 to 9) for the empty cells so that every row, column, and
3 × 3 block contains all the digits from 1 to 9 once. In addition, each of the two main
diagonals (45° and 135°) contains all the digits from 1 to 9 once.

Use the minimum remaining value and degree heuristics to implement the SELECT-
UNASSIGNED-VARIABLE function in the Backtracking Algorithm. For the ORDER-DOMAIN-
VALUES function, simply order the domain values in increasing order from 1 to 9 instead of using
heuristics. You do not have to implement the INFERENCE function inside the Backtracking
Algorithm. (Reminder: when implementing the minimum remaining values and degree heuristics,
two or more variables are neighbors if they share a common constraint.)

Input and output files: Your program will read in the initial game board values from an input text
file and produce an output text file that contains the solution. The input file contains 9 rows (or
lines) of integers. Each row contains 9 integers ranging from 0 to 9,
separated by blank spaces. Digits 1-9 represent the cell values and 0’s represent blank cells.
Similarly, the output file contains 9 rows of integers. Each row contains
9 integers ranging from 1 to 9 (without 0s,) separated by blank spaces.

n n n n n n n n n
n n n n n n n n n
n n n n n n n n n
n n n n n n n n n
n n n n n n n n n
n n n n n n n n n
n n n n n n n n n
n n n n n n n n n
n n n n n n n n n
Figure 1. Input file format. n is an integer between 0 and 9, with 0s representing blank cells.

n n n n n n n n n
n n n n n n n n n
n n n n n n n n n
n n n n n n n n n
n n n n n n n n n
n n n n n n n n n
n n n n n n n n n
n n n n n n n n n
n n n n n n n n n
Figure 2. Output file format. n is an integer between 1 and 9.

One sample input and sample output is included.
