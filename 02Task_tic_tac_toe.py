# Создайте программу для игры в ""Крестики-нолики"".
def print_board(board):
    for row in board:
        print(row)
# Таже функция в одну строку
# def print_board(board):
#    [print(row) for row in board]


def convert_selection(selection):  # возвращает правильную пару i, j в виде кортежа
    selection -= 1  # вычитаю единицу, так что теперь мой диапазон составляет 0–8
    # возвращаю кортеж — неизменяемый тип данных, который не изменится — с помощью круглых скобок.
    return (selection // 3, selection % 3)


# поместим «X» в место, которое выбирает пользователь
# принимает кортеж выбора и доску в качестве аргументов и вносит изменения в доску
def place_piece(selection, is_x, board):
    # проверяем, что квадрат пуст, прежде чем поместить туда фигуру. Таким образом, игроки не могут перезаписывать друг друга.
    if board[selection[0]][selection[1]] == "_":
        board[selection[0]][selection[1]] = "X"if is_x else "O"
    else:  # Если пытаемся записать на занятый квадрат выдаем ошибку. Что бы не потерять ход добавим continue в  try
        raise ValueError
        # Для наглядности могли бы записать так
    #     def place_piece(selection, is_x, board):
    #           i, j = selection
    #       if board[i][j] == "_":
    #           board[i][j] = "X" if is_x else "O"


def select_square():
    selection = int(input("Выбирете квадрат 1-9: "))
    if not 1 <= selection <= 9:
        raise ValueError
    return selection


def is_draw(board):
    for row in board:
        for val in row:
            if val == "_":
                return False
        print('Ничья! Больше никаких ходов!')
        return True


def is_win(board):
    winner = None
    for i in range(3):
        # horizontal
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != "_":
            winner = board[i][0]
            break
        # vertical
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != "_":
            winner = board[0][i]
            break
    # diagonal
    if board[1][1] != "_":
        if (board[0][0] == board[1][1] == board[2][2]
                or board[0][2] == board[1][1] == board[2][0]):
            winner = board[1][1]
    if winner is not None:
        print_board(board)
        print(f"{winner} is the winner!")
        return True
    return False


board = [["_" for _ in range(3)] for _ in range(3)]
is_x = True
game_over = False
while not game_over:

    print_board(board)
    try:
        selection = convert_selection(select_square())
        place_piece(selection, is_x, board)
        print('нажмите Enter для пердачи хода')

    except ValueError:
        print("Выбирете квадрат 1-9")
        continue
    game_over = is_win(board) or is_draw(board)
    is_x = not is_x

    print('нажмите Enter для пердачи хода')

print_board(board)
