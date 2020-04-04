def find_empty_location(mat, l):
    for lin in range(9):
        for col in range(9):
            if (mat[lin][col] == 0):
                l[0] = lin
                l[1] = col
                return True
    return False

def lin_usado(mat, lin, num):
    for i in range(9):
        if (mat[lin][i] == num):
            return True
    return False

def col_usado(mat, col, num):
    for i in range(9):
        if (mat[i][col] == num):
            return True
    return False

def campo_usado(mat, lin, col, num):
    for i in range(3):
        for j in range(3):
            if (mat[i + lin][j + col] == num):
                return True
    return False

def verificacao(mat, lin, col, num):
    return not lin_usado(mat, lin, num) and not col_usado(mat, col, num) and not campo_usado(mat, lin - lin % 3, col - col % 3, num)

def exibe(mat):
    for i in range(9):
        for j in range(9):
            textsurface = myfont.render(str(matriz[i][j]), False, (0, 0, 0))
            screen.blit(textsurface, ((56 * i) + 40,((56 * j) + 35)))