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
                box_list.append(str(c))
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
    print("")
    for row in grid:
        r=""
        for num in row:
            r+=str(num)+"  "
        print(r)
    print("")
#adding digits    
def add_digit(grid, row, col, num): #User function to add digit
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
#notes/notes grid basics
def get_notes(grid, row, col): #gets the notes of one digit
    notes=""
    for note in range (1,10):
        if check_all(grid, row, col, note)==True:
            notes+=str(note)
    return notes
def note_grid(grid): #returns notes grid, uses get_notes
    note_grid=[["" for _ in range(9)] for _ in range(9)]
    for row in range(9):
        for col in range(9):
            if grid[row][col]==0:
                note_grid[row][col]=get_notes(grid,row+1,col+1)
            else:
                note=grid[row][col]
                note_grid[row][col]=str(note)
    return note_grid
def print_ngrid(grid): #prints notes grid, uses note_grid
    print("")
    ngrid=note_grid(grid)
    for r in range(9):
        new_row=""
        for n in range(9):
            if ngrid[r][n]=="0":
                new_row+="("
                new_row+=str(grid[r][n])
                new_row+=")      "
            else:
                new_row+=str(ngrid[r][n])
                for i in range(9-len(ngrid[r][n])):
                    new_row+=" "
        print(new_row)
        print("")
#(here down) hidden subset (doubles, triples, quads) implication modifier
def note_to_pos(nlist): #provides a list of 9 strings (1 for each num) with the positions/indexes of the note nums
    position_list=["" for _ in range(9)]
    for num in range(1,10): #for each placeable number
        for i in range(9): #for each index in the list
            for note in nlist[i]: #for each note in the current index's string
                if note==str(num):
                    position_list[num-1]+=str(i)
    return position_list
def filter_hsubs(hsub_list): #removes non-unique hsubs, used in doubles, triples and quads functions
    filtered=[]
    for a in hsub_list:
        pos_match = True
        for b in filtered:
            if sorted(a[-1]) == sorted(b[-1]):
                pos_match = False
                break
        if pos_match:
            filtered.append(a)
    return filtered
#hsub identifiers (doubles, triples, and quads), returns list of positions, with list[-1] containing the nums exclusively in those positions
def doubles(list): #double hsub identifier
    doubles_list=[]
    for a in range(len(list)):
        for b in range(len(list)):
            if a!=b: #comparing every value with every other value in the note/position list
                pos_count=[]
                for pos1 in list[a]:
                    for pos2 in list[b]:
                        if pos1 not in pos_count: #adding all unique notes to pos_count
                            pos_count.append(str(pos1))
                        if pos2 not in pos_count:
                            pos_count.append(str(pos2))
                if len(pos_count)==2: #if there's only 2 values total
                    doubles_list.append([a,b,pos_count])
    filtered_doubles=filter_hsubs(doubles_list) #filtering out all non-unique doubles
    return filtered_doubles
def triples(list): #triple hsub identifier
    triples_list=[]
    for a in range(len(list)):
        for b in range(len(list)):
            if a!=b:
                for c in range(len(list)):
                    if a!=c and b!=c: #getting all non-repeated combos of ab&c
                        pos_count=[]
                        for pos1 in list[a]:
                            for pos2 in list[b]:
                                for pos3 in list[c]:
                                    if pos1 not in pos_count: #adding all unique notes to pos_count
                                        pos_count.append(str(pos1))
                                    if pos2 not in pos_count:
                                        pos_count.append(str(pos2))
                                    if pos3 not in pos_count:
                                        pos_count.append(str(pos3))
                        if len(pos_count)==3: #if there's only 3 values total
                            triples_list.append([a,b,c,pos_count])
    filtered_triples=filter_hsubs(triples_list) #filtering out all non-unique triples
    return filtered_triples
def quads(list): #quad hsub identifier
    quads_list=[]
    for a in range(len(list)):
        for b in range(len(list)):
            if a!=b:
                for c in range(len(list)):
                    if a!=c and b!=c:
                        for d in range(len(list)):
                            if a!=d and b!=d and c!=d: #getting all non-repeated combos of abc&d
                                pos_count=[]
                                for pos1 in list[a]:
                                    for pos2 in list[b]:
                                        for pos3 in list[c]:
                                            for pos4 in list[d]:
                                                if pos1 not in pos_count: #adding all unique notes to pos_count
                                                    pos_count.append(str(pos1))
                                                if pos2 not in pos_count:
                                                    pos_count.append(str(pos2))
                                                if pos3 not in pos_count:
                                                    pos_count.append(str(pos3))
                                                if pos4 not in pos_count:
                                                    pos_count.append(str(pos4))
                                if len(pos_count)==4: #if there's only 4 values total
                                    quads_list.append([a,b,c,d,pos_count])
    filtered_quads=filter_hsubs(quads_list) #filtering out all non-unique quadruples
    return filtered_quads
#(join_hsubs explanation) since hsubs can occur when n digits can only exist in n positions OR n positions can only contain n digits,
# takes nlist (note list) and plist (position list) that have both gone through an hsub identifier, converts the plist hsubs to nlist hsub format,
# combines them, and runs them through the hsub filter to get rid of non-unique hsubs.
def join_hsubs(note_hsubs, pos_hsubs): 
    hsubs=[]
    for hsub in note_hsubs:
        hsubs.append(hsub)
    new_pos_hsubs=[]
    for hsub in pos_hsubs: #converting a position hidden subset to note hsub format
        new_hsub=[]
        for x in hsub[-1]:
            new_hsub.append(int(x))
        new_hsub.append([])
        for x in range(len(hsub)-1):
            new_hsub[-1].append(str(hsub[x]+1))
        hsubs.append(new_hsub)
    filtered_hsubs=filter_hsubs(hsubs) #filtering out all non-unique hsubs
    return filtered_hsubs
#(hsub_cleanup explanation) takes the original notes list and the joined hsubs and returns a new nlist with the hsubs applied,
#ex. if there's a 567 triple, within the triple any numbers other than 56&7 are removed, and outside the triple 56&7 are removed from all other positions.
def hsub_cleanup(nlist, hsubs):
    new_nlist=["" for _ in range(9)]
    used_nums=""
    for i in range(9): #adding the hsubs to the new notes list
        for hsub in hsubs:
            for pos in range(len(hsub)-1):
                if i==hsub[pos]:
                    for note in nlist[i]:
                        if note in hsub[-1]:
                            if note not in new_nlist[i]:
                                new_nlist[i]+=note
                                used_nums+=note
    for i in range(9): #adding the rest of the notes to the empty new_nlist positions, excluding already used nums
        if len(new_nlist[i])==0:
            for note in nlist[i]:
                if note not in used_nums:
                    new_nlist[i]+=note
    return new_nlist
def singles(nlist): #recognizing and fixing naked singles, essentially a post-hsub_cleanup hsub identifier
    new_nlist=["" for _ in range(9)]
    used_nums=""
    for i in range(9): #identifying singles and adding them to new notes list
        if len(nlist[i])==1:
            new_nlist[i]+=nlist[i]
            used_nums+=nlist[i]
    for i in range(9): #going through the new notes list and adding the rest of the notes so long as a used single isn't in
        if len(new_nlist[i])==0:
            for note in nlist[i]:
                if note not in used_nums:
                    new_nlist[i]+=note
    return new_nlist
def apply_hsubs(nlist): #preps and runs the nlist through doubles, triples, quads, hsub_cleanup, and singles to return a fully "note implication applied" note list
    plist2=note_to_pos(nlist)
    ready2=join_hsubs(doubles(nlist),doubles(plist2))
    nlist2=hsub_cleanup(nlist,ready2)
    single2=singles(nlist2)
    plist3=note_to_pos(single2)
    ready3=join_hsubs(triples(single2),triples(plist3))
    nlist3=hsub_cleanup(single2,ready3)
    single3=singles(nlist3)
    plist4=note_to_pos(single3)
    ready4=join_hsubs(quads(single3),quads(plist4))
    nlist4=hsub_cleanup(single3,ready4)
    single4=singles(nlist4)
    return single4
def box_indices(row, col): #give row and col and it'll give the row and col positions of every other num in that box.
    r=row//3*3
    c=col//3*3
    indices=[[row2, col2] for row2 in range(r,r+3) for col2 in range(c,c+3)]
    return indices
#(hsubs explanation) #the note implication modifier. runs the rows, columns, and then boxes through apply_hsubs returning the new note grid. 
# If the finished note grid is the same as the original it'll instead return False
def hsubs(ngrid):
    ngrid2=[] #hsub'n the rows
    for r in range(9):
        row2=apply_hsubs(ngrid[r])
        ngrid2.append(row2)
    ngrid3=[["","","","","","","","",""] for _ in range(9)] #hsub'n the columns
    for c in range(9):
        col=[]
        for r in range(9):
            col.append(ngrid2[r][c])
        col2=apply_hsubs(col)
        for r in range(9):
            ngrid3[r][c]+=col2[r]
    ngrid4=[["","","","","","","","",""] for _ in range(9)] #hsub'n the boxes
    boxes=[[1,1],[1,4],[1,7],[4,1],[4,4],[4,7],[7,1],[7,4],[7,7]] #cheaty list of positions in each box
    for i in range(9):
        box=get_box(ngrid3,boxes[i][0],boxes[i][1])
        box2=apply_hsubs(box)
        box2i=box_indices(boxes[i][0],boxes[i][1])
        for b in range(9):
            r=box2i[b][0]
            c=box2i[b][1]
            ngrid4[r][c]+=box2[b]
    if ngrid4==ngrid:
        return False
    else:
        return ngrid4
def hsubs_recursive(ngrid): #runs hsubs repeatedly until all hidden subset logic is exhausted
    if not hsubs(ngrid):
        return ngrid
    else:
        return hsubs_recursive(hsubs(ngrid))


#example
grid1=new_grid()
add_digit(grid1,1,2,2)
add_digit(grid1,1,4,6)
add_digit(grid1,1,6,8)
add_digit(grid1,2,1,5)
add_digit(grid1,2,2,8)
add_digit(grid1,2,6,9)
add_digit(grid1,2,7,7)
add_digit(grid1,3,5,4)
add_digit(grid1,4,1,3)
add_digit(grid1,4,2,7)
add_digit(grid1,4,7,5)
add_digit(grid1,5,1,6)
add_digit(grid1,5,9,4)
add_digit(grid1,6,3,8)
add_digit(grid1,6,8,1)
add_digit(grid1,6,9,3)
add_digit(grid1,7,5,2)
add_digit(grid1,8,3,9)
add_digit(grid1,8,4,8)
add_digit(grid1,8,8,3)
add_digit(grid1,8,9,6)
add_digit(grid1,9,4,3)
add_digit(grid1,9,6,6)
add_digit(grid1,9,8,9)

print("")
print("DIGITS PLACED")
print_grid(grid1)
print("ORIGINAL NOTE GRID")
ngrid1=note_grid(grid1)
print_ngrid(ngrid1)
print("MODIFIED NOTE GRID (it takes a second)")
hsub1=hsubs_recursive(ngrid1)
print_ngrid(hsub1)
print("and voila it actually ends up solving the whole")
print("thing despite only being a quarter filled")
print("")
