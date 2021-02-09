"""
module

>>> print(validate_board(["**** ****",\
    "***1 ****",\
    "**  3****",\
    "* 4 8****",\
    "     9 5 ",\
    " 6  83  *",\
    "3   1  **",\
    "  8  2***",\
    "  2  ****"]))
False
"""

def create_board(board: list):
    """
    Creates board by modeficating board

    >>> create_board(["**** ****", \
        "***1 ****", \
        "**  3****", \
        "* 4 8****", \
        "     9 5 ", \
        " 6  83  *", \
        "3   1  **", \
        "  8  2***", \
        "  2  ****"])[0]
    ['*', '*', '*', '*', ' ', '*', '*', '*', '*']
    """
    new_board = []
    for row in board:
        new_board.append(list(row))
    return new_board


def check_line(check_line: list):
    '''
    >>> check_line(['*', '*', '2', '5', '3', '*', '*', '*', '*'])
    True
    '''
    line = []
    for symbol in check_line:
        if symbol != '*' and symbol != ' ':
            try:
                symbol = int(symbol)
                if symbol>=1 and symbol<=9:
                    line.append(symbol)
                else:
                    return False
            except:
                return False
    for i in range(len(line)):
        for j in range(i+1, len(line)):
            if line[i] == line[j]:
                return False
    return True


def side_switch(new_board: list):
    """
    rotate matrix by 90 degrees
    >>> side_switch([['*', '*', '*', '*', ' ', '*', '*', '*', '*'], ['*', '*', '*', '1', ' ', '*', '*', '*', '*'], \
    ['*', '*', ' ', ' ', '3', '*', '*', '*', '*'], ['*', ' ', '4', ' ', '8', '*', '*', '*', '*'], \
    [' ', ' ', ' ', ' ', ' ', '9', ' ', '5', ' '], [' ', '6', ' ', ' ', '8', '3', ' ', ' ', '*'], \
    ['3', ' ', ' ', ' ', '1', ' ', ' ', '*', '*'], [' ', ' ', '8', ' ', ' ', '2', '*', '*', '*'], \
    [' ', ' ', '2', ' ', ' ', '*', '*', '*', '*']])
    ['**** ****', '****5 ***', '****   **', '****93 2*', '  38 81  ', '*1       ', '** 4   82', '***  6   ', '****  3  ']
    """
    # new_board = []

    # for row in board:
    #     new_board.append(list(row))
    # print(new_board)
    b = [[0]*len(new_board)]*len(new_board)
    b1 = []

    for i in range(len(new_board)):
        for j in range(len(new_board[i])):
            b[i][j] = new_board[j][len(new_board)-i-1]
        b1.append(list(b[0]))
        b2 = []
    for lst in b1:
        strring = "".join(lst)
        b2.append(strring)
    return b2


def horizontal_check(new_board: list):
    """
    sfdg
    >>> print(horizontal_check([['*', '*', '*', '*', ' ', '*', '*', '*', '*'], ['*', '*', '*', '1', ' ', '*', '*', '*', '*'], \
    ['*', '*', ' ', ' ', '3', '*', '*', '*', '*'], ['*', ' ', '4', ' ', '8', '*', '*', '*', '*'], \
    [' ', ' ', ' ', ' ', ' ', '9', ' ', '5', ' '], [' ', '6', ' ', ' ', '8', '3', ' ', ' ', '*'], \
    ['3', ' ', ' ', ' ', '1', ' ', ' ', '*', '*'], [' ', ' ', '8', ' ', ' ', '2', '*', '*', '*'], \
    [' ', ' ', '2', ' ', ' ', '*', '*', '*', '*']]))
    True

    """
    for row in new_board:
        if not check_line(row):
            return False
    return True


def column_check(new_board: list):
    """
    fd
    >>> print(column_check([['*', '*', '*', '*', ' ', '*', '*', '*', '*'], ['*', '*', '*', '1', ' ', '*', '*', '*', '*'], \
    ['*', '*', ' ', ' ', '3', '*', '*', '*', '*'], ['*', ' ', '4', ' ', '8', '*', '*', '*', '*'], \
    [' ', ' ', ' ', ' ', ' ', '9', ' ', '5', ' '], [' ', '6', ' ', ' ', '8', '3', ' ', ' ', '*'], \
    ['3', ' ', ' ', ' ', '1', ' ', ' ', '*', '*'], [' ', ' ', '8', ' ', ' ', '2', '*', '*', '*'], \
    [' ', ' ', '2', ' ', ' ', '*', '*', '*', '*']]))
    False
    """

    new_board = side_switch(new_board)
    for row in new_board:
        if not check_line(row):
            return False
    return True

def colour_positions(new_board:list):
    """
    g
    >>> print(colour_positions([['*', '*', '*', '*', ' ', '*', '*', '*', '*'], ['*', '*', '*', '1', ' ', '*', '*', '*', '*'], \
    ['*', '*', ' ', ' ', '3', '*', '*', '*', '*'], ['*', ' ', '4', ' ', '8', '*', '*', '*', '*'], \
    [' ', ' ', ' ', ' ', ' ', '9', ' ', '5', ' '], [' ', '6', ' ', ' ', '8', '3', ' ', ' ', '*'], \
    ['3', ' ', ' ', ' ', '1', ' ', ' ', '*', '*'], [' ', ' ', '8', ' ', ' ', '2', '*', '*', '*'], \
    [' ', ' ', '2', ' ', ' ', '*', '*', '*', '*']])[0])
    [' ', ' ', '2', ' ', ' ', ' ', ' ', '3', ' ']

    """
    new_board1 = side_switch(new_board)
    colour_lines = []
    j=0
    for i in range(5):

        # print(new_board[len(new_board)-1-i][:5])
        # print(type(new_board[len(new_board)-1-i][:5]))
        color_line = new_board[len(new_board)-1-i][j:5+j] 
        color_line.extend( new_board1[len(new_board1)-1-i][-5-j:-1-j])
        j+=1
        colour_lines.append(color_line)

    return colour_lines

def color_check(new_board):
    '''
    checks color positions
    
    >>> print(color_check([['*', '*', '*', '*', ' ', '*', '*', '*', '*'], ['*', '*', '*', '1', ' ', '*', '*', '*', '*'], \
    ['*', '*', ' ', ' ', '3', '*', '*', '*', '*'], ['*', ' ', '4', ' ', '8', '*', '*', '*', '*'], \
    [' ', ' ', ' ', ' ', ' ', '9', ' ', '5', ' '], [' ', '6', ' ', ' ', '8', '3', ' ', ' ', '*'], \
    ['3', ' ', ' ', ' ', '1', ' ', ' ', '*', '*'], [' ', ' ', '8', ' ', ' ', '2', '*', '*', '*'], \
    [' ', ' ', '2', ' ', ' ', '*', '*', '*', '*']]))
    True
    '''
    color_lines = colour_positions(new_board)
    for row in color_lines:
        if not check_line(row):
            return False
    return True

def validate_board(board) -> bool:
    """
    fghh

    >>> print(validate_board(["**** ****",\
    "***1 ****",\
    "**  3****",\
    "* 4 8****",\
    "     9 5 ",\
    " 6  83  *",\
    "3   1  **",\
    "  8  2***",\
    "  2  ****"]))
    False
    """
    board = create_board(board)
    if horizontal_check(board) and column_check(board) and color_check(board):
        return True
    return False

# print(color_check([['*', '*', '*', '*', ' ', '*', '*', '*', '*'], ['*', '*', '*', '1', ' ', '*', '*', '*', '*'], \
#     ['*', '*', ' ', ' ', '3', '*', '*', '*', '*'], ['*', ' ', '4', ' ', '8', '*', '*', '*', '*'], \
#     [' ', ' ', ' ', ' ', ' ', '9', ' ', '5', ' '], [' ', '6', ' ', ' ', '8', '3', ' ', ' ', '*'], \
#     ['3', ' ', ' ', ' ', '1', ' ', ' ', '*', '*'], [' ', ' ', '8', ' ', ' ', '2', '*', '*', '*'], \
#     [' ', ' ', '2', ' ', ' ', '*', '*', '*', '*']]))



#print(check_line(['*', '*', '2', '5', '3', '*', '*', '*', '*']))


# print(validate_board([
#     "**** ****",
#     "***1 ****",
#     "**  3****",
#     "* 4 8****",
#     "     9 5 ",
#     " 6  83  *",
#     "3   1  **",
#     "  8  2***",
#     "  2  ****"
# ]))

# print(colour_positions(create_board([
#     "**** ****",
#     "***1 ****",
#     "**  3****",
#     "* 4 8****",
#     "     9 5 ",
#     " 6  83  *",
#     "3   1  **",
#     "  8  2***",
#     "  2  ****"
# ])))
# print(side_switch([['*', '*', '*', '*', ' ', '*', '*', '*', '*'], ['*', '*', '*', '1', ' ', '*', '*', '*', '*'], \
#     ['*', '*', ' ', ' ', '3', '*', '*', '*', '*'], ['*', ' ', '4', ' ', '8', '*', '*', '*', '*'], \
#     [' ', ' ', ' ', ' ', ' ', '9', ' ', '5', ' '], [' ', '6', ' ', ' ', '8', '3', ' ', ' ', '*'], \
#     ['3', ' ', ' ', ' ', '1', ' ', ' ', '*', '*'], [' ', ' ', '8', ' ', ' ', '2', '*', '*', '*'], \
#     [' ', ' ', '2', ' ', ' ', '*', '*', '*', '*']]))\
if __name__ =='__main__':
    import doctest
    doctest.testmod()