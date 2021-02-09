"""
https://github.com/bbryk/puzzle

module that contains functions to check the puzzle game

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
    Creates board(list with lists) by modeficating another board(list of strs)

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


def check_line(line_to_check: list):
    '''
    Checks the line for similar elements
    >>> check_line(['*', '*', '2', '5', '3', '*', '*', '*', '*'])
    True
    '''
    line = []
    for symbol in line_to_check:
        if symbol not in ('*', ' '):
            try:
                symbol = int(symbol)
                if 1 <= symbol <= 9:
                    line.append(symbol)
                else:
                    return False
            except ValueError:
                return False
    for i in range(len(line)):
        for j in range(i+1, len(line)):
            if line[i] == line[j]:
                return False
    return True


def side_switch(new_board: list):
    """
    rotate matrix by 90 degrees
    >>> side_switch([['*', '*', '*', '*', ' ', '*', '*', '*', '*'], \
    ['*', '*', '*', '1', ' ', '*', '*', '*', '*'], \
    ['*', '*', ' ', ' ', '3', '*', '*', '*', '*'], ['*', ' ', '4', ' ', '8', '*', '*', '*', '*'], \
    [' ', ' ', ' ', ' ', ' ', '9', ' ', '5', ' '], [' ', '6', ' ', ' ', '8', '3', ' ', ' ', '*'], \
    ['3', ' ', ' ', ' ', '1', ' ', ' ', '*', '*'], [' ', ' ', '8', ' ', ' ', '2', '*', '*', '*'], \
    [' ', ' ', '2', ' ', ' ', '*', '*', '*', '*']])
    ['**** ****', '****5 ***', '****   **', '****93 2*', '  38 81  ', '*1       ', \
'** 4   82', '***  6   ', '****  3  ']
    """
    # new_board = []

    # for row in board:
    #     new_board.append(list(row))
    # print(new_board)
    switched_board = [[0]*len(new_board)]*len(new_board)
    secondary_board1 = []

    for i in range(len(new_board)):
        for j in range(len(new_board[i])):
            switched_board[i][j] = new_board[j][len(new_board)-i-1]
        secondary_board1.append(list(switched_board[0]))
        secondary_board2 = []
    for lst in secondary_board1:
        strring = "".join(lst)
        secondary_board2.append(strring)
    return secondary_board2


def horizontal_check(new_board: list):
    """
    Checks every line in board for similar elements
    >>> print(horizontal_check([['*', '*', '*', '*', ' ', '*', '*', '*', '*'], \
    ['*', '*', '*', '1', ' ', '*', '*', '*', '*'], \
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
    Checks every column in board for similar elements
    >>> print(column_check([['*', '*', '*', '*', ' ', '*', '*', '*', '*'], \
    ['*', '*', '*', '1', ' ', '*', '*', '*', '*'], \
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


def colour_positions(new_board: list):
    """
    creates list of lists of similar color elements
    >>> print(colour_positions([['*', '*', '*', '*', ' ', '*', '*', '*', '*'], \
    ['*', '*', '*', '1', ' ', '*', '*', '*', '*'], \
    ['*', '*', ' ', ' ', '3', '*', '*', '*', '*'], ['*', ' ', '4', ' ', '8', '*', '*', '*', '*'], \
    [' ', ' ', ' ', ' ', ' ', '9', ' ', '5', ' '], [' ', '6', ' ', ' ', '8', '3', ' ', ' ', '*'], \
    ['3', ' ', ' ', ' ', '1', ' ', ' ', '*', '*'], [' ', ' ', '8', ' ', ' ', '2', '*', '*', '*'], \
    [' ', ' ', '2', ' ', ' ', '*', '*', '*', '*']])[0])
    [' ', ' ', '2', ' ', ' ', ' ', ' ', '3', ' ']

    """
    new_board1 = side_switch(new_board)
    colour_lines = []
    j = 0
    for i in range(5):

        # print(new_board[len(new_board)-1-i][:5])
        # print(type(new_board[len(new_board)-1-i][:5]))
        color_line = new_board[len(new_board)-1-i][j:5+j]
        color_line.extend(new_board1[len(new_board1)-1-i][-5-j:-1-j])
        j += 1
        colour_lines.append(color_line)

    return colour_lines


def color_check(new_board):
    '''
    checks color positions for similar elements

    >>> print(color_check([['*', '*', '*', '*', ' ', '*', '*', '*', '*'], \
    ['*', '*', '*', '1', ' ', '*', '*', '*', '*'], \
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
    The main function. Contains all the checks and validates board 

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


if __name__ == '__main__':
    import doctest
    doctest.testmod()
