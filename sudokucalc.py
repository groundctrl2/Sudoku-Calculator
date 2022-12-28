#sudoku rules
def check_row(grid, row, num):
    if not any(grid[row-1][a] == num for a in range(9)):
        return True
def check_col(grid, col, num):
    if not any (grid[a][col-1] == num for a in range(9)):
        return True
def get_box(grid, row, col): #for check_box
    box_list=[]
    for a in range(9):
        for b in range(9):
            if ((a) // 3 == (row-1) // 3) and ((b) // 3 == (col-1) // 3):
                c=grid[a][b]
                box_list+=str(c)
    return box_list
def check_box(grid, row, col, num):
    box=get_box(grid, row, col)
    for a in box:
        if str(a)==str(num):
            return False
        return True
def check_all(grid, row, col, num):
    if check_row(grid, row, num)==True:
        if check_col(grid, col, num)==True:
            if check_box(grid, row, col, num)==True:
                return True
    return False

#grid basics
def new_grid():
    return [[0 for _ in range(9)] for _ in range(9)]
def print_grid(grid):
    print("FINAL GRID")
    print("")
    for row in grid:
        r=""
        for num in row:
            r+=str(num)+"  "
        print(r)
    print("")

#adding digits    
def add_digit(grid, row, col, num):
    if check_row(grid, row, num)==True:
        if check_col(grid, col, num)==True:
            if check_box(grid, row, col, num)==True:
                grid[row-1][col-1]=num
            else:
                print("subgrid/box conflict")
        else:
            print("column conflict")
    else:
        print("row conflict")
def test_digit(grid, row, col, num): #allows you to place invalid digits
    grid[row-1][col-1]=num

#notes/notes grid basics
def get_notes(grid, row, col): #gets the notes of one digit
    notes=""
    for note in range (1,10):
        if check_all(grid, row, col, note)==True:
            notes+=str(note)
        else:
            notes+="0"
    return notes
def note_grid(grid): #returns notes grid, uses get_notes
    note_grid=[["" for _ in range(9)] for _ in range(9)]
    for row in range(9):
        for col in range(9):
            if grid[row][col]==0:
                note_grid[row][col]=get_notes(grid,row+1,col+1)
            else:
                note_grid[row][col]="    "+str(grid[row][col])+"    "
    return note_grid
def print_ngrid(grid): #prints notes grid, uses note_grid
    print("NOTE GRID")
    print("")
    ngrid=note_grid(grid)
    for row in ngrid:
        r=" "
        for note in row:
            r+=note+"  "
        print(r)
    print(" ")