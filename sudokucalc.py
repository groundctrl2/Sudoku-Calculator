#sudoku rules
def check_row(grid, row, digit):
    if not any(grid[row-1][a] == digit for a in range(9)):
        return True
def check_col(grid, col, digit):
    if not any (grid[a][col-1] == digit for a in range(9)):
        return True
def get_box(grid, row, col): #for check_box
    box_list=[]
    for a in range(9):
        for b in range(9):
            if ((a) // 3 == (row-1) // 3) and ((b) // 3 == (col-1) // 3):
                c=grid[a][b]
                box_list+=str(c)
    return box_list
def check_box(grid, row, col, digit):
    box=get_box(grid, row, col)
    for a in box:
        if str(a)==str(digit):
            return False
        return True

#user input
def new_grid():
    return [[0 for _ in range(9)] for _ in range(9)]
def print_grid(grid):
    print("FINAL GRID")
    for row in grid:
        print(row)
def add_digit(grid, row, col, digit):
    if check_row(grid, row, digit)==True:
        if check_col(grid, col, digit)==True:
            if check_box(grid, row, col, digit)==True:
                grid[row-1][col-1]=digit
            else:
                print("subgrid/box conflict")
        else:
            print("column conflict")
    else:
        print("row conflict")