from sudoku import Sudoku

if __name__ == '__main__':
    sudoku = Sudoku(
        board=[
            [8, 4, 0, 0, 5, 0, 0, 0, 0],
            [3, 0, 0, 6, 0, 8, 0, 4, 0],
            [0, 0, 0, 4, 0, 9, 0, 0, 0],
            [0, 2, 3, 0, 0, 0, 8, 9, 0],
            [1, 0, 0, 8, 0, 0, 0, 0, 4],
            [0, 9, 8, 0, 0, 0, 1, 6, 0],
            [0, 0, 0, 5, 0, 3, 0, 0, 0],
            [0, 3, 0, 1, 0, 6, 0, 0, 7],
            [0, 0, 0, 0, 2, 0, 0, 1, 3]],
        even_cells=[(2, 2), (0, 5), (2, 8), (3, 4), (4, 3), (4, 6), (5, 4), (6, 0), (6, 6),
                    (8, 2)]
    )
    if sudoku.solve_with_mrv():
        print("Solution found:")
        print(sudoku.matrix)
    else:
        print("There is no solution.")
    print(sudoku.count)
