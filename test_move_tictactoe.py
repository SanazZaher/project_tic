from move_tictactoe import move

def test_move_wrong_mark_at_position():
    current_board = "----o----"
    mark = "x"
    position = 3
    board_after_mark = "---xo----"
    new_board= move(current_board, mark, position)
    assert new_board == board_after_mark #test passes, correct position mark

def test_move_wrong_mark():
    current_board = "-----x-----"
    mark ="o"
    position = 4
    board_after_mark = "----xx-----"
    new_board = move(current_board, mark, position)
    assert new_board == board_after_mark # test fails, wrong mark at the position


# By your own words - (as comments at the end of the created Python test file) describe:

# What is a Python module and how does it differ from a Python package? python modules are informations that we can use them when its needed and a python package can contain different modules in it and are the main package.

# What are side effects and give some examples:Each module has a task or a functionallitiy. I think we talk about side effects if there is an unexpected interruption in the task that the module is supposed to do outside of its function. for example if we have a module and we have the print statment for this module then use this module outside somewhere else we will have an unexpected print instead of the expected result we want from this module and this output(print)is a side effect.Ex: 
def remainder_of_division(number): 
    result = number % 2
    print(f"The remainder of {number} divided by 2 is {result}")
    return result

# What are Exceptions and what to do if third-party code that we use throws them? we use exceptions to hanlde unexpected situations that might make problems in our output. and we raise an exception to handle these unexpected errors.to handle the situation from a third party code I think we can use a more specific way with except Exception as e:

# Using which keywords can you create, throw and catch your new custom Exception? creat and define a custom exception/throw or raise the custom exception and catch or handle the custom exception with try and except. 

# Give examples of some benefits of testing? Testing helps to catch the bugs in the early stages of the code and this makes the developments process faster and the collaboration easier. it minimizes the risk of encountring bigger problems and preventing them before they make unexpected error in the process.