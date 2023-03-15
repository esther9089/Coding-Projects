"""Gomoku starter code
You should complete every incomplete function,
and add more functions and variables as needed.

Note that incomplete functions have 'pass' as the first statement:
pass is a Python keyword; it is a statement that does nothing.
This is a placeholder that you should remove once you modify the function.

Author(s): Michael Guerzhoy with tests contributed by Siavash Kazemian.  Last modified: Oct. 30, 2021
"""

def is_empty(board):
    '''Return True iff there are no stones on board board'''

    count = 0
    for i in range(len(board)):
        for j in range (len(board[0])):
            if board[i][j] == " ":
                count += 1

    if count == 64:
        return True
    else:
        return False



def is_bounded(board, y_end, x_end, length, d_y, d_x):
    '''Return "OPEN" if sequence is open, "SEMIOPEN" if sequence is semi-open, and "CLOSED" if sequence is closed'''


    #direction (0,1) left-to-right
    if d_y == 0 and d_x == 1:

        if x_end == 7:
            if x_end - length >= 0 and board[y_end][x_end - length] == " ":
                return "SEMIOPEN"
            else:
                return "CLOSED"
        elif x_end - (length-1) == 0:
            if x_end + 1 <= 7 and board[y_end][x_end + 1] == " ":
                return "SEMIOPEN"
            elif x_end + 1 <= 7 and board[y_end][x_end + 1] == " ":
                if x_end - length >= 0 and board[y_end][x_end - length] == " ":
                    return "OPEN"
                else:
                    return "SEMIOPEN"
        elif x_end - (length) >= 0 and x_end-(length)<=7:

            if board[y_end][x_end + 1] == " " and board[y_end][x_end-length] == " ":
                return "OPEN"
            elif board[y_end][x_end + 1] != " " and board[y_end][x_end-length] != " ":
                return "CLOSED"
            else:
                return "SEMIOPEN"


    # direction (1,0) top-to-bottom
    if d_y == 1 and d_x == 0:

        if y_end == 7:
            if y_end - length >= 0 and board[y_end - length][x_end] == " ":
                return "SEMIOPEN"
            else:
                return "CLOSED"
        elif y_end - (length-1) == 0:
            if y_end + 1 <= 7 and board[y_end + 1][x_end] == " ":
                return "SEMIOPEN"
            else:
                return "CLOSED"

        elif y_end - (length) >= 0 and y_end-(length)<=7:

            if board[y_end + 1][x_end] == " " and board[y_end - length][x_end] == " ":
                return "OPEN"
            elif board[y_end + 1][x_end] != " " and board[y_end - length][x_end] != " ":
                return "CLOSED"
            else:
                return "SEMIOPEN"



    # direction (1,1) upper-left-to-lower-right
    if d_y == 1 and d_x == 1:

        if y_end == 7 :
            if y_end - length >= 0 and x_end - length >= 0 and board[y_end - length][x_end - length] == " ":
                return "SEMIOPEN"
            else:
                return "CLOSED"
        elif x_end == 7:
            if y_end - length >= 0 and x_end - length >= 0 and board[y_end - length][x_end - length] == " ":
                return "SEMIOPEN"
            else:
                return "CLOSED"
        elif y_end - (length-1) == 0:
            if y_end + 1 <= 7 and x_end + 1 <= 7 and board[y_end + 1][x_end + 1] == " ":
                return "SEMIOPEN"
            else:
                return "CLOSED"
        elif x_end - (length-1) == 0:
            if y_end + 1 <= 7 and x_end + 1 <= 7 and board[y_end + 1][x_end + 1] == " ":
                return "SEMIOPEN"
            else:
                return "CLOSED"
        elif y_end + 1 <=7 and y_end - length >= 0 and x_end + 1 <=7 and x_end-length >= 0:
            if board[y_end - length][x_end-length] == " " and board[y_end+1][x_end + 1] == " ":
                return "OPEN"
            elif board[y_end - length][x_end-length] != " " and board[y_end+1][x_end + 1] != " ":
                return "CLOSED"
            else:
                return "SEMIOPEN"



    # direction (1,-1) upper-right-to-lower-left
    if d_y == 1 and d_x == -1:

        if y_end == 7 :
            if y_end - length >= 0 and x_end + length >= 0 and x_end + length <= 7 and board[y_end - length][x_end + length] == " ":
                return "SEMIOPEN"
            else:
                return "CLOSED"
        elif x_end + (length-1) == 7:
            if y_end + 1 >= 0 and y_end + 1 <=7 and x_end + 1 >= 0 and board[y_end + 1][x_end - 1] == " ":
                return "SEMIOPEN"
            else:
                return "CLOSED"
        elif y_end - (length-1) == 0:
            if x_end == 0:
                return "CLOSED"
            elif y_end + 1 <= 7 and x_end - 1 <= 7 and x_end - 1 >= 0 and board[y_end + 1][x_end - 1] == " ":
                return "SEMIOPEN"
            else:
                return "CLOSED"
        elif x_end == 0:
            if y_end - length <= 7 and x_end - length <= 7 and board[y_end - length][x_end + length] == " ":
                return "SEMIOPEN"
            else:
                return "CLOSED"
        elif y_end + 1 <=7 and x_end - 1 <=7:
            # if board[y_end - length][x_end - length] == " ":
            #     return "OPEN"
            # else:
            #     return "SEMIOPEN"


            if board[y_end - length][x_end+length] == " " and board[y_end+1][x_end - 1] == " ":
                return "OPEN"
            elif board[y_end - length][x_end+length] != " " and board[y_end+1][x_end - 1] != " ":
                return "CLOSED"
            else:
                return "SEMIOPEN"

        # else:
        #     return "CLOSED"

def detect_row(board, col, y_start, x_start, length, d_y, d_x):
    '''Return tuple
    (# of open sequences of colour col of length length, # of semi-open sequences of colour col of length length)
    '''
    open_seq_count = 0
    semi_open_seq_count = 0
    s = ""
    string_search = ""
    a = 0
    b = 0
    x = 0

    if col == "w":
        anti_col = "b"
    if col == "b":
        anti_col = "w"

    if d_y == 1 and d_x == 1:
        diagonal = max(x_start, y_start)
    elif d_x == -1 and (8-y_start) != 8:
        diagonal = y_start
    elif d_x == -1 and (8-y_start) == 8:
        diagonal = 7 - x_start
    else:
        diagonal = 0

    string_search = (col*length)

    for i in range(0, (8-diagonal)): #creating the string
        s += board [y_start] [x_start]
        y_start += d_y
        x_start += d_x

    if len(s) < 8:
        x = 8 - len(s)
        for i in range(0, x):
            s+= "N"

    #for open
    search = (" " + string_search + " ")
    #for open
    if length < 5:
        if s.count(" " + string_search + " " + string_search + " ") > 0:
            open_seq_count = 2
        else:
            x = s.count(search)
            open_seq_count += x

    else:
        x = s.count(search)
        open_seq_count += x

    a = s.count(" " + string_search + anti_col)
    semi_open_seq_count += a

    b = s.count(anti_col + string_search + " ")
    semi_open_seq_count += b

    c = s.count(" " + string_search + "N")
    semi_open_seq_count += c

    if s.count(string_search) != 0:
        a = s.index(string_search)
        if a == 0:
            if length == 8:
                semi_open_seq_count += 1
            if s[length] == " ":
                semi_open_seq_count += 1

        if s.count(string_search) > semi_open_seq_count:
            if s[8-length] == col:
                count = 0
                for i in range (0, length):
                    if s[8-length+i] == col:
                        count += 1
                if count == length and s[8-length-1] == " ":
                    semi_open_seq_count += 1

        elif a + length == 8:
            if s[a-1] == " ":
                semi_open_seq_count += 1

    return open_seq_count, semi_open_seq_count

def detect_rows(board, col, length):
    y_start = 0
    x_start = 0
    open_seq_count, semi_open_seq_count = 0, 0

    for i in range(0,1):
        for i in range (0, 8): #for left to right
            y_start += i
            new_open, new_semi = detect_row(board, col, y_start, x_start, length, 0, 1)
            open_seq_count += new_open
            semi_open_seq_count += new_semi
            y_start = 0
            x_start = 0

        for i in range (0, 8): #for top to bottom
            x_start += i
            new_open, new_semi = detect_row(board, col, y_start, x_start, length, 1, 0)
            open_seq_count += new_open
            semi_open_seq_count += new_semi
            y_start = 0
            x_start = 0

        for i in range (0, 8): #for upper left to lower right
            y_start += i
            new_open, new_semi = detect_row(board, col, y_start, x_start, length, 1, 1)
            open_seq_count += new_open
            semi_open_seq_count += new_semi
            y_start = 0
            x_start = 0

        for i in range (1, 8): #for upper left to lower right
            x_start += i
            new_open, new_semi = detect_row(board, col, y_start, x_start, length, 1, 1)
            open_seq_count += new_open
            semi_open_seq_count += new_semi
            y_start = 0
            x_start = 0

        y_start = 0
        x_start = 7

        for i in range (0, 8): #for upper right to lower left

            x_start = 7 - i
            new_open, new_semi = detect_row(board, col, y_start, x_start, length, 1, -1)
            open_seq_count += new_open
            semi_open_seq_count += new_semi
            y_start = 0


        y_start = 0
        x_start = 7

        for i in range (1, 8): #for upper right to lower left
            y_start += i
            new_open, new_semi = detect_row(board, col, y_start, x_start, length, 1, -1)
            open_seq_count += new_open
            semi_open_seq_count += new_semi
            y_start = 0
            x_start = 7
    return open_seq_count, semi_open_seq_count

def search_max(board):

    move_y = 0
    move_x = 0
    list_move = []
    list_score = []

    for i in range (8):
        for j in range (8):

            if board[i][j] == " ":
                board[i][j] = "b"
                list_move += [[i, j]]
                list_score += [score(board)]
                board[i][j] = " "

            else:
                continue

    max_num = -100001


    # find max score
    for k in range (0, len(list_score)):
        if list_score[k] >= max_num:
            max_num = list_score[k]
        else:
            continue

    # find index of max score in list list_score
    ind = list_score.index(max_num)

    # find the corresponding list of x and y positions at ind
    move_y = list_move[ind][0]
    move_x = list_move[ind][1]


    return move_y, move_x


def score(board):
    MAX_SCORE = 100000

    open_b = {}
    semi_open_b = {}
    open_w = {}
    semi_open_w = {}

    for i in range(2, 6):
        open_b[i], semi_open_b[i] = detect_rows(board, "b", i)
        open_w[i], semi_open_w[i] = detect_rows(board, "w", i)


    if open_b[5] >= 1 or semi_open_b[5] >= 1:
        return MAX_SCORE

    elif open_w[5] >= 1 or semi_open_w[5] >= 1:
        return -MAX_SCORE

    return (-10000 * (open_w[4] + semi_open_w[4])+
                500  * open_b[4]                     +
                50   * semi_open_b[4]                +
                -100  * open_w[3]                    +
                -30   * semi_open_w[3]               +
                50   * open_b[3]                     +
                10   * semi_open_b[3]                +
                open_b[2] + semi_open_b[2] - open_w[2] - semi_open_w[2])


def is_win(board):
    #double check this function and its helper functions
    if max_length(board, "w") == True:
        return "White won"
    if max_length(board, "b") == True:
        return "Black won"
    if board_full(board) == True:
        return "Draw"
    else:
        return "Continue playing"

#helper functions
def max_length(board, col):
    search_string =""
    search_string = col*5
    y_start = 0
    x_start = 0

    for i in range (0, 1):
        for i in range (0, 8): #for left to right
            y_start += i
            s = string_creator(board, y_start, x_start, 0, 1, col)
            if s.count(search_string)== 1 and s.count(col*6) == 0:
                return True
            y_start = 0
            x_start = 0

        for i in range (0, 8): #for top to bottom
            x_start += i
            s = string_creator(board, y_start, x_start, 1, 0, col)
            if s.count(search_string)== 1 and s.count(col*6) == 0:
                return True
            y_start = 0
            x_start = 0

        for i in range (0, 8): #for upper left to lower right
            y_start += i
            s = string_creator(board, y_start, x_start, 1, 1, col)
            if s.count(search_string)== 1 and s.count(col*6) == 0:
                return True
            y_start = 0
            x_start = 0

        for i in range (1, 8): #for upper left to lower right
            x_start += i
            s = string_creator(board, y_start, x_start, 1, 1, col)
            if s.count(search_string)== 1 and s.count(col*6) == 0:
                return True
            y_start = 0
            x_start = 0

        y_start = 0
        x_start = 7

        for i in range (1, 8): #for upper right to lower left
            x_start = 7 - i
            s = string_creator(board, y_start, x_start, 1, -1, col)
            if s.count(search_string)== 1 and s.count(col*6) == 0:
                return True
            y_start = 0


        y_start = 0
        x_start = 7

        for i in range (0, 8): #for upper right to lower left
            y_start += i
            s = string_creator(board, y_start, x_start, 1, -1, col)
            if s.count(search_string)== 1 and s.count(col*6) == 0:
                return True
            y_start = 0
            x_start = 7

    return False

def string_creator(board, y_start, x_start, d_y, d_x, col):
    s = ""

    if d_y == 1 and d_x == 1:
        diagonal = max(x_start, y_start)
    elif d_x == -1 and (8-y_start) != 8:
        diagonal = y_start
    elif d_x == -1 and (8-y_start) == 8:
        diagonal = 7 - x_start
    else:
        diagonal = 0

    for i in range(0, (8-diagonal)): #creating the string
        s += board [y_start] [x_start]
        y_start += d_y
        x_start += d_x


    if len(s) < 8:
        x = 8 - len(s)
        for i in range(0, x):
            s+= "N"
    return s

def board_full(board):
    x = 0
    y = 0
    count = 0
    for i in range (0, 8): #left to right
        y += i
        for j in range (0, 8):
            x += j
            if board[y][x] != " ":
                count += 1
            x = 0
        y = 0

    if count == 64:
        return True
    else:
        return False


def print_board(board):
    '''Print Gomoku board'''
    s = "*"
    for i in range(len(board[0])-1):
        s += str(i%10) + "|"
    s += str((len(board[0])-1)%10)
    s += "*\n"

    for i in range(len(board)):
        s += str(i%10)
        for j in range(len(board[0])-1):
            s += str(board[i][j]) + "|"
        s += str(board[i][len(board[0])-1])

        s += "*\n"
    s += (len(board[0])*2 + 1)*"*"

    print(s)


def make_empty_board(sz):
    board = []
    for i in range(sz):
        board.append([" "]*sz)
    return board



def analysis(board):
    for c, full_name in [["b", "Black"], ["w", "White"]]:
        print("%s stones" % (full_name))
        for i in range(2, 6):
            open, semi_open = detect_rows(board, c, i);
            print("Open rows of length %d: %d" % (i, open))
            print("Semi-open rows of length %d: %d" % (i, semi_open))


def play_gomoku(board_size):
    board = make_empty_board(board_size)
    board_height = len(board)
    board_width = len(board[0])

    while True:
        print_board(board)
        if is_empty(board):
            move_y = board_height // 2
            move_x = board_width // 2
        else:
            move_y, move_x = search_max(board)

        print("Computer move: (%d, %d)" % (move_y, move_x))
        board[move_y][move_x] = "b"
        print_board(board)
        analysis(board)

        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res


        print("Your move:")
        move_y = int(input("y coord: "))
        move_x = int(input("x coord: "))
        board[move_y][move_x] = "w"
        print_board(board)
        analysis(board)

        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res



def put_seq_on_board(board, y, x, d_y, d_x, length, col):
    '''Adds the sequence of stones of colour col of length length to board'''
    for i in range(length):
        board[y][x] = col
        y += d_y
        x += d_x


def test_is_empty():
    board  = make_empty_board(8)
    if is_empty(board):
        print("TEST CASE for is_empty PASSED")
    else:
        print("TEST CASE for is_empty FAILED")

def test_is_bounded():

    # test case 1
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)

    y_end = 3
    x_end = 5

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'OPEN':
        print("TEST CASE 1 for is_bounded PASSED")
    else:
        print("TEST CASE 1 for is_bounded FAILED")


    # test case 2
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 1; d_y = 0; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)

    y_end = 1
    x_end = 7

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'SEMIOPEN':
        print("TEST CASE 2 for is_bounded PASSED")
    else:
        print("TEST CASE 2 for is_bounded FAILED")

    #test case 3
    board = make_empty_board(8)
    x = 5; y = 0; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)

    y_end = 2
    x_end = 5

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'SEMIOPEN':
        print("TEST CASE 3 for is_bounded PASSED")
    else:
        print("TEST CASE 3 for is_bounded FAILED")


    #test case 4
    board = make_empty_board(8)
    x = 5; y = 5; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)


    y_end = 7
    x_end = 5

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'SEMIOPEN':
        print("TEST CASE 4 for is_bounded PASSED")
    else:
        print("TEST CASE 4 for is_bounded FAILED")



    # test case 5
    board = make_empty_board(8)
    x = 2; y = 1; d_x = 1; d_y = 0; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)


    y_end = 1
    x_end = 4

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'OPEN':
        print("TEST CASE 5 for is_bounded PASSED")
    else:
        print("TEST CASE 5 for is_bounded FAILED")

    # test case 6
    board = make_empty_board(8)
    x = 0; y = 1; d_x = 1; d_y = 0; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)


    y_end = 1
    x_end = 2

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'SEMIOPEN':
        print("TEST CASE 6 for is_bounded PASSED")
    else:
        print("TEST CASE 6 for is_bounded FAILED")

    # test case 7

    board = make_empty_board(8)
    x = 5; y = 1; d_x = 1; d_y = 0; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)


    y_end = 1
    x_end = 7

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'SEMIOPEN':
        print("TEST CASE 7 for is_bounded PASSED")
    else:
        print("TEST CASE 7 for is_bounded FAILED")

    #test case 8

    board = make_empty_board(8)
    x = 2; y = 1; d_x = 1; d_y = 0; length = 3
    put_seq_on_board(board, 1, 5, 0, 1, 1, "b")
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)


    y_end = 1
    x_end = 4


    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'SEMIOPEN':
        print("TEST CASE 8 for is_bounded PASSED")
    else:
        print("TEST CASE 8 for is_bounded FAILED")


    # test case 9

    board = make_empty_board(8)
    x = 2; y = 6; d_x = 1; d_y = 0; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    put_seq_on_board(board, 6, 1, 0, 1, 1, "b")
    put_seq_on_board(board, 6, 5, 0, 1, 2, "b")
    print_board(board)


    y_end = 6
    x_end = 4

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'CLOSED':
        print("TEST CASE 9 for is_bounded PASSED")
    else:
        print("TEST CASE 9 for is_bounded FAILED")


    #test case 10
    board = make_empty_board(8)
    x = 1; y = 0; d_x = 0; d_y = 1; length = 8
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)


    y_end = 7
    x_end = 5

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'CLOSED':
        print("TEST CASE 10 for is_bounded PASSED")
    else:
        print("TEST CASE 10 for is_bounded FAILED")

    #test case 11
    board = make_empty_board(8)
    x = 5; y = 5; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    put_seq_on_board(board, 4, 5, 1, 0, 1, "b")
    print_board(board)


    y_end = 7
    x_end = 5

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'CLOSED':
        print("TEST CASE 11 for is_bounded PASSED")
    else:
        print("TEST CASE 11 for is_bounded FAILED")

    #test case 12
    board = make_empty_board(8)
    x = 3; y = 2; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    put_seq_on_board(board, 1, 3, 1, 0, 1, "b")
    put_seq_on_board(board, 5, 3, 0, 1, 3, "b")
    print_board(board)


    y_end = 4
    x_end = 3

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'CLOSED':
        print("TEST CASE 12 for is_bounded PASSED")
    else:
        print("TEST CASE 12 for is_bounded FAILED")

    #test case 13
    board = make_empty_board(8)
    x = 3; y = 2; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    put_seq_on_board(board, 5, 3, 0, 1, 3, "b")
    print_board(board)


    y_end = 4
    x_end = 3

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'SEMIOPEN':
        print("TEST CASE 13 for is_bounded PASSED")
    else:
        print("TEST CASE 13 for is_bounded FAILED")

    # test case 14
    board = make_empty_board(8)
    x = 1; y = 1; d_x = 1; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)


    y_end = 3
    x_end = 3

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'OPEN':
        print("TEST CASE 14 for is_bounded PASSED")
    else:
        print("TEST CASE 14 for is_bounded FAILED")

    # test case 15
    board = make_empty_board(8)
    x = 1; y = 1; d_x = 1; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    put_seq_on_board(board, 0, 0, 0, 1, 1, "b")
    print_board(board)


    y_end = 3
    x_end = 3

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'SEMIOPEN':
        print("TEST CASE 15 for is_bounded PASSED")
    else:
        print("TEST CASE 15 for is_bounded FAILED")

    # test case 16
    board = make_empty_board(8)
    x = 1; y = 1; d_x = 1; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    put_seq_on_board(board, 0, 0, 0, 1, 1, "b")
    put_seq_on_board(board, 4, 4, 0, 1, 1, "b")
    print_board(board)


    y_end = 3
    x_end = 3

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'CLOSED':
        print("TEST CASE 16 for is_bounded PASSED")
    else:
        print("TEST CASE 16 for is_bounded FAILED")

    # test case 17
    board = make_empty_board(8)
    x = 1; y = 0; d_x = 1; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)


    y_end = 2
    x_end = 3

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'SEMIOPEN':
        print("TEST CASE 17 for is_bounded PASSED")
    else:
        print("TEST CASE 17 for is_bounded FAILED")

    # test case 18
    board = make_empty_board(8)
    x = 2; y = 6; d_x = 1; d_y = 1; length = 2
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)


    y_end = 7
    x_end = 3

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'SEMIOPEN':
        print("TEST CASE 18 for is_bounded PASSED")
    else:
        print("TEST CASE 18 for is_bounded FAILED")

    # test case 19
    board = make_empty_board(8)
    x = 0; y = 2; d_x = 1; d_y = 1; length = 6
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)


    y_end = 7
    x_end = 5

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'CLOSED':
        print("TEST CASE 19 for is_bounded PASSED")
    else:
        print("TEST CASE 19 for is_bounded FAILED")

    # test case 20
    board = make_empty_board(8)
    x = 4; y = 2; d_x = 1; d_y = 1; length = 4
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)


    y_end = 5
    x_end = 7

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'SEMIOPEN':
        print("TEST CASE 20 for is_bounded PASSED")
    else:
        print("TEST CASE 20 for is_bounded FAILED")


    # test case 21
    board = make_empty_board(8)
    x = 4; y = 2; d_x = -1; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)


    y_end = 4
    x_end = 2

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'OPEN':
        print("TEST CASE 21 for is_bounded PASSED")
    else:
        print("TEST CASE 21 for is_bounded FAILED")

    # test case 22
    board = make_empty_board(8)
    x = 4; y = 2; d_x = -1; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    put_seq_on_board(board, 5, 1, d_y, d_x, 1, "b")
    put_seq_on_board(board, 1, 5, d_y, d_x, 1, "b")
    print_board(board)


    y_end = 4
    x_end = 2

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'CLOSED':
        print("TEST CASE 22 for is_bounded PASSED")
    else:
        print("TEST CASE 22 for is_bounded FAILED")

    # test case 23
    board = make_empty_board(8)
    x = 4; y = 2; d_x = -1; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    put_seq_on_board(board, 5, 1, d_y, d_x, 1, "b")
    print_board(board)


    y_end = 4
    x_end = 2

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'SEMIOPEN':
        print("TEST CASE 23 for is_bounded PASSED")
    else:
        print("TEST CASE 23 for is_bounded FAILED")

    # test case 24
    board = make_empty_board(8)
    x = 4; y = 4; d_x = -1; d_y = 1; length = 4
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    #put_seq_on_board(board, 3, 5, d_y, d_x, 1, "b")
    print_board(board)


    y_end = 7
    x_end = 1

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'SEMIOPEN':
        print("TEST CASE 24 for is_bounded PASSED")
    else:
        print("TEST CASE 24 for is_bounded FAILED")

    # test case 25
    board = make_empty_board(8)
    x = 2; y = 3; d_x = -1; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    put_seq_on_board(board, 2, 3, d_y, d_x, 1, "b")
    print_board(board)


    y_end = 5
    x_end = 0

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'CLOSED':
        print("TEST CASE 25 for is_bounded PASSED")
    else:
        print("TEST CASE 25 for is_bounded FAILED")

    # test case 26
    board = make_empty_board(8)
    x = 5; y = 0; d_x = -1; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)


    y_end = 2
    x_end = 3

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'SEMIOPEN':
        print("TEST CASE 26 for is_bounded PASSED")
    else:
        print("TEST CASE 26 for is_bounded FAILED")

    # test case 27
    board = make_empty_board(8)
    x = 7; y = 1; d_x = -1; d_y = 1; length = 7
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)


    y_end = 7
    x_end = 1

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'CLOSED':
        print("TEST CASE 27 for is_bounded PASSED")
    else:
        print("TEST CASE 27 for is_bounded FAILED")

    # test case 28
    board = make_empty_board(8)
    x = 7; y = 0; d_x = -1; d_y = 1; length = 8
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)


    y_end = 7
    x_end = 0

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'CLOSED':
        print("TEST CASE 28 for is_bounded PASSED")
    else:
        print("TEST CASE 28 for is_bounded FAILED")


def test_detect_row():

    # test case 1
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_row(board, "w", 0,x,length,d_y,d_x) == (1,0):
        print("TEST CASE for detect_row PASSED")
    else:
        print("TEST CASE for detect_row FAILED")

    # test case 2
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_row(board, "w", 0,x,length,d_y,d_x) == (1,0):
        print("TEST CASE for detect_row PASSED")
    else:
        print("TEST CASE for detect_row FAILED")

    #test case 3
    board = make_empty_board(8)
    x = 5; y = 0; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)

    y_start = 0
    x_start = 5

    if detect_row(board, "w", y_start,x,length,d_y,d_x) == (0,1):
        print("TEST CASE for detect_row PASSED")
    else:
        print("TEST CASE for detect_row FAILED")

    #test case 4
    board = make_empty_board(8)
    x = 5; y = 5; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)


    if detect_row(board, "w", 0,x,length,d_y,d_x) == (0,1):
        print("TEST CASE for detect_row PASSED")
    else:
        print("TEST CASE for detect_row FAILED")

    # test case 5
    board = make_empty_board(8)
    x = 2; y = 1; d_x = 1; d_y = 0; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)


    if detect_row(board, "w", y,0,length,d_y,d_x) == (1,0):
        print("TEST CASE for detect_row PASSED")
    else:
        print("TEST CASE for detect_row FAILED")

def test_detect_rows():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_rows(board, col,length) == (1,0):
        print("TEST CASE for detect_rows PASSED")
    else:
        print("TEST CASE for detect_rows FAILED")

    board = make_empty_board(8)
    x = 5; y = 0; d_x = 0; d_y = 1; length = 4; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    print_board(board)
    if detect_rows(board, col,length) == (0,1):
        print("TEST CASE for detect_rows PASSED")
    else:
        print("TEST CASE for detect_rows FAILED")

    x = 6; y = 0; d_x = 0; d_y = 1; length = 4; col = 'b'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    put_seq_on_board(board, 2, 7, 1, 0, 1, "b")
    print_board(board)
    if detect_rows(board, col,4) == (0,1):
        print("TEST CASE for detect_rows PASSED")
    else:
        print("TEST CASE for detect_rows FAILED")



def test_search_max():
    board = make_empty_board(8)
    x = 5; y = 0; d_x = 0; d_y = 1; length = 4; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    x = 6; y = 0; d_x = 0; d_y = 1; length = 4; col = 'b'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    print_board(board)
    if search_max(board) == (4,6):
        print("TEST CASE for search_max PASSED")
    else:
        print("TEST CASE for search_max FAILED")

    board = make_empty_board(8)
    x = 5; y = 0; d_x = 0; d_y = 1; length = 4; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    x = 4; y = 0; d_x = 0; d_y = 1; length = 4; col = 'b'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    print_board(board)
    if search_max(board) == (4,4):
        print("TEST CASE for search_max PASSED")
    else:
        print("TEST CASE for search_max FAILED")

    board = make_empty_board(8)
    board[0][0] = "w"
    board[0][2] = "w"
    board[1][1] = "w"
    board[0][4] = "b"
    board[6][5] = "w"
    board[7][2] = "w"
    board[7][6] = "b"

    x = 5; y = 0; d_x = 0; d_y = 1; length = 3; col = 'b'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    x = 6; y = 0; d_x = 0; d_y = 1; length = 2; col = 'b'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    x = 3; y = 3; d_x = 1; d_y = 0; length = 3; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    x = 6; y = 2; d_x = 0; d_y = 1; length = 5; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    x = 7; y =3; d_x = 0; d_y = 1; length = 3; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    x = 6; y = 4; d_x = 0; d_y = 1; length = 3; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    x = 4; y = 5; d_x = 0; d_y = 1; length = 3; col = 'b'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    x = 2; y = 6; d_x = 1; d_y = 0; length = 2; col = 'b'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    print_board(board)
    if search_max(board) == (3,2):
        print("TEST CASE for search_max PASSED")
    else:
        print("TEST CASE for search_max FAILED")

def easy_testset_for_main_functions():
    test_is_empty()
    test_is_bounded()
    test_detect_row()
    test_detect_rows()
    #test_search_max()


def some_tests():

    board = make_empty_board(8)

    board[0][0] = "b"

    y = 0; x = 6; d_x = 0; d_y = 1; length = 4
    put_seq_on_board(board, y, x, d_y, d_x, length, "b")
    print_board(board)
    y = 0; x = 5; d_x = 0; d_y = 1; length = 4
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    analysis(board)


    board = make_empty_board(8)

    board[0][5] = "w"
    board[0][6] = "b"
    y = 5; x = 2; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    analysis(board)

    # Expected output:
    #       *0|1|2|3|4|5|6|7*
    #       0 | | | | |w|b| *
    #       1 | | | | | | | *
    #       2 | | | | | | | *
    #       3 | | | | | | | *
    #       4 | | | | | | | *
    #       5 | |w| | | | | *
    #       6 | |w| | | | | *
    #       7 | |w| | | | | *
    #       *****************
    #       Black stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 0
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0
    #       White stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 1
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0

    y = 3; x = 5; d_x = -1; d_y = 1; length = 2

    put_seq_on_board(board, y, x, d_y, d_x, length, "b")
    print_board(board)
    analysis(board)

    # Expected output:
    #        *0|1|2|3|4|5|6|7*
    #        0 | | | | |w|b| *
    #        1 | | | | | | | *
    #        2 | | | | | | | *
    #        3 | | | | |b| | *
    #        4 | | | |b| | | *
    #        5 | |w| | | | | *
    #        6 | |w| | | | | *
    #        7 | |w| | | | | *
    #        *****************
    #
    #         Black stones:
    #         Open rows of length 2: 1
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 0
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #         White stones:
    #         Open rows of length 2: 0
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 1
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #

    y = 5; x = 3; d_x = -1; d_y = 1; length = 1
    put_seq_on_board(board, y, x, d_y, d_x, length, "b");
    print_board(board);
    analysis(board);

    #        Expected output:
    #           *0|1|2|3|4|5|6|7*
    #           0 | | | | |w|b| *
    #           1 | | | | | | | *
    #           2 | | | | | | | *
    #           3 | | | | |b| | *
    #           4 | | | |b| | | *
    #           5 | |w|b| | | | *
    #           6 | |w| | | | | *
    #           7 | |w| | | | | *
    #           *****************
    #
    #
    #        Black stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0
    #        White stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0




if __name__ == '__main__':
    #play_gomoku(8)
    #test_is_empty()
    #print(make_empty_board(8))
    #test_is_bounded()
    #test_detect_row()
    #test_detect_rows()
    easy_testset_for_main_functions()
    #some_tests()
    #test_search_max()