import core
# 
def check(move, player, board):
    return core.is_valid(move) and core.is_legal(move, player, board)
#
def human(player, board):
    print (core.print_board(board))
    print ('Your move?')
    while True:
        move = input('> ')
        if move and check(int(move), player, board):
            return int(move)
        elif move:
            print ('Illegal move--try again.')
#
def get_choice(prompt, options):
    return(options['random']  )
#
def get_players():
    options = { 'random': core.random_strategy,
                }
    black = get_choice('BLACK: choose a strategy', options)
    white = get_choice('WHITE: choose a strategy', options)
    return black, white
#
def main():
    try:
        black, white = get_players()
        board, score = core.play(black, white)
    except core.IllegalMoveError as e:
        print (e)
        return
    except EOFError as e:
        print ('Goodbye.')
        return
    
    print ('%s wins!' % ('Black' if score > 0 else 'White'))
    print (core.print_board(board))
    print ('Final score:', score)
main()