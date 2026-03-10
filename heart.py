
#def proof_that_tony_stark_has_a_heart():
# 9 x 6 _ 8 x 5
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

columna = len(grid[0])
print("numero de columnas:", columna)
fila = len(grid)
print("numero de filas:", fila)

for c in range(columna):
    cadena = ""
    for f in range(fila):
        cadena += grid[f][c]
    print(cadena)

#print(grid[8][0] + grid[7][0] + grid[6][0] + grid[5][0] + grid[4][0] + grid[3][0] + grid[2][0] + grid[1][0] + grid[0][0])



#v = 0
#h = 0
#cadena = ""
#h = len(grid[0])
#for row in grid:
#    cadena += grid[v][0]
#    v += 1
#
#print(cadena)
#print(h)










#print(grid[8][0])
#print(grid[7][0])
#print(grid[6][0])
#print(grid[5][0])
#print(grid[4][0])
#print(grid[3][0])
#print(grid[2][0])
#print(grid[1][0])
#print(grid[0][0])
#print(grid[8][0] + grid[7][0] + grid[6][0] + grid[5][0] + grid[4][0] + grid[3][0] + grid[2][0] + grid[1][0] + grid[0][0])

# 8 0 a 7 0 .... 1 0 a 0 0
#print(grid[8][5])
#print(len(grid) * len(grid[0]))