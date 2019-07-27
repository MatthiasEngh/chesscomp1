import chess, chess.pgn, random

def count_responses(board, move):
  board.push(move)
  if board.is_checkmate():
    result = 9001
  elif board.is_game_over():
    result = -25
  else:
    result = - len(list(board.legal_moves))
  board.pop()
  return result

def max_next_move(fen):
  board = new_board(fen)
  if board.is_checkmate():
    return -9001
  if board.is_game_over():
    return -25
  return max([count_responses(board, move) for move in board.legal_moves])

def move_minimum(fen):
  board = new_board(fen)
  if board.is_checkmate():
    return 9001
  if board.is_game_over():
    return -25
  return min([max_next_move(new_position(fen, move)) for move in board.legal_moves])

def new_board(fen):
  return chess.Board(fen)

def new_position(fen, move):
  board = new_board(fen)
  board.push(move)
  return board.fen()

def make_move(fen):
  moves = list(new_board(fen).legal_moves)
  random.shuffle(moves)
  evaluations = [move_minimum(new_position(fen, move)) for move in moves]
  found_max = max(evaluations)
  return moves[evaluations.index(found_max)]
