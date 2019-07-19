def sudoku2(grid):
    for i in range(9):
        temp = grid[i]
        temp = [i for i in temp if i in "123456789"]
        if len(temp) != len(set(temp)): 
            return False 
        temp2 = [grid[x][i] for x in range(9) if grid[x][i] in "123456789"]
        if len(temp2) != len(set(temp2)): 
            return False 
    t = -3
    for z in range(3):
        temp = set()
        t += 3
        for i in range(3):
            for x in range(3):
                if grid[t + i][t + x] not in "123456789":
                    print(t + i, t + x, grid[t + i][t + x], temp)
                    continue
                if grid[t + i][t + x] in temp:
                    # print(temp)
                    print(t + i, t + x, grid[t + i][t + x])
                    return False
                else: temp.add(grid[t + i][t + x])
    return True
            
grid = [[".",".",".",".",".",".","5",".","."], 
        [".",".",".",".",".",".",".",".","."], 
        [".",".",".",".",".",".",".",".","."], 
        ["9","3",".",".","2",".","4",".","."], 
        [".",".","7",".",".",".","3",".","."], 
        [".",".",".",".",".",".",".",".","."], 
        [".",".",".","3","4",".",".",".","."], 
        [".",".",".",".",".","3",".",".","."], 
        [".",".",".",".",".","5","2",".","."]]
print(sudoku2(grid))