from evaluate_tictactoe import evaluate

def test_evaluate_x_winner():
    board_test = "xxx-----------------"
    assert evaluate(board_test) == "x"# test passes, x winnes

def test_evaluate_o_winner():
    board_test ="------ooo-----------"
    assert evaluate(board_test) =="o"# test passes, o winns

def test_evaluate_game_continius():
    board_test ="x-------oo----------"
    assert evaluate(board_test) == "-"# test passes, there are spaces in the game, we can continue

def test_evaluate_game_draw():
    board_test = "xoxxooxoxoxxooxooxx"
    assert evaluate(board_test) == "!" # test passes, there are no spaces in the game, draw!

def test_evaluate_invalid_board():
    board_invalid = "i--------x-o-xx-f---"
    assert evaluate(board_invalid) == "" # test fails,board has invalid marks