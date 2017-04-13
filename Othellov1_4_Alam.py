import random
EMPTY, BLACK, WHITE, OUTER = '.', '@', 'o', '?'
PIECES = (EMPTY, BLACK, WHITE, OUTER)
PLAYERS = {BLACK: 'Black', WHITE: 'White'}

# To refer to neighbor squares we can add a direction to a square.
UP, DOWN, LEFT, RIGHT = -10, 10, -1, 1
UP_RIGHT, DOWN_RIGHT, DOWN_LEFT, UP_LEFT = -9, 11, 9, -11
DIRECTIONS = (UP, UP_RIGHT, RIGHT, DOWN_RIGHT, DOWN, DOWN_LEFT, LEFT, UP_LEFT)  
def squares():
	"""List all the valid squares on the board."""
	return [i for i in range(11, 89) if 1 <= (i % 10) <= 8]


def initial_board():
	"""Create a new board with the initial black and white positions filled."""
	othelloboard = [OUTER] * 100
	for x in squares():
	    othelloboard[x] = EMPTY
	othelloboard[44], othelloboard[45] = WHITE, BLACK
	othelloboard[54], othelloboard[55] = BLACK, WHITE
	return othelloboard


def print_board(board):
	"""Get a string representation of the board."""
	rep = ''
	rep += '  %s\n' % ' '.join(map(str, list(range(1, 9))))
	for row in range(1, 9):
	    begin, end = 10 * row + 1, 10 * row + 9
	    rep += '%d %s\n' % (row, ' '.join(board[begin:end]))
	return rep   
def is_valid(move):
	"""Is move a square on the board?"""
	if isinstance(move, int) and move in squares():
		return True
	else:
		return False

def opponent(player):
	"""Get player's opponent piece."""	
	if player == BLACK:
		return WHITE
	else:
		return BLACK

def find_bracket(square, player, board, direction):
	"""
	Find a square that forms a bracket with `square` for `player` in the given
	`direction`.  Returns None if no such square exists.
	Returns the index of the bracketing square if found
	"""
	bracket = square + direction
	if othelloboard[bracket] == player:
		return None
	theopponent = opponent(player)
	while othelloboard[bracket] == theopponent:
		bracket += direction
	if othelloboard[bracket] in (OUTER, EMPTY):
		return None 
	else:
		return bracket


def is_legal(move, player, board):
	"""Is this a legal move for the player?"""
	hasbr = lambda direction: find_bracket(move, player, board, direction)
	if board[move] == EMPTY and any(map(hasbr, DIRECTIONS)):
		return True
	else:
		return False

def make_move( move, player, board):
	"""Update the board to reflect the move by the specified player."""
	board[move] = player
	for i in DIRECTIONS:
		make_flips(move, player, board, i)
	return board

def make_flips(move, player, board, direction):
	"""Flip pieces in the given direction as a result of the move by player."""
	bracket = find_bracket(move, player, board, direction)
	if not bracket:
		return
	square = move + direction
	while square != bracket:
		board[square] = player
		square += direction

def legal_moves(player, board):
	"""Get a list of all legal moves for player, as a list of integers"""
	for square in squares():
		if is_legal(square, player, board):
			return square

def any_legal_move(player, board):
	"""Can player make any moves? Returns a boolean"""
	return any(is_legal(sq, player, board) for sq in squares())

def next_player(board, prev_player):
	"""Which player should move next?  Returns None if no legal moves exist."""
	theopponent = opponent(prev_player)
	if any_legal_move(theopponent, board):
		return opponent
	if any_legal_move(prev_player, board):
		return prev_player
	return None

def score(player, board):
	"""Compute player's score (number of player's pieces minus opponent's)."""
	me, otherplayer = 0, 0
	opp = opponent(me)
	for square in squares():
		piece = board[squar]
		if piece == player: mine += 1
		if piece == opp: otherplayer += 1
	return me - otherplayer


class IllegalMoveError(Exception):
	def __init__(self, player, move, board):
		self.player = player
		self.move = move
		self.board = board
	def __str__():
		return '%s cannot move to square %d' % (PLAYERS[self.player], self.move)

SQUARE_WEIGHTS = [
    0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
    0, 120, -20,  20,   5,   5,  20, -20, 120,   0,
    0, -20, -40,  -5,  -5,  -5,  -5, -40, -20,   0,
    0,  20,  -5,  15,   3,   3,  15,  -5,  20,   0,
    0,   5,  -5,   3,   3,   3,   3,  -5,   5,   0,
    0,   5,  -5,   3,   3,   3,   3,  -5,   5,   0,
    0,  20,  -5,  15,   3,   3,  15,  -5,  20,   0,
    0, -20, -40,  -5,  -5,  -5,  -5, -40, -20,   0,
    0, 120, -20,  20,   5,   5,  20, -20, 120,   0,
    0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
]

def random_strategy(player, board):
    randomstrat = random.choice(legal_moves(player, board))
    return randomstrat
def minimax(player, board, depth, evaluate):
	def value(board):
		return -minimax(opponent(player), board, depth-1, evaluate)[0]
	if depth == 0:
		return evaluate(player, board), None
	
	possiblemoves = legal_moves(player, board)

	if not possiblemoves:
		if not any_legal_move(opponent(player), board):
			return final_value(player, board), None

		return value(board), None


	return max((value(make_move(m, player, list(board))), m) for m in possiblemoves)


maxval = sum(map(abs, SQUARE_WEIGHTS))
minval = maxval*-1


def final_value(player, board):

    difference = score(player, board)
    if difference > 0:
        return maxval
    else:
        return minval
    
    return difference



