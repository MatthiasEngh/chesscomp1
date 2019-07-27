import chess, chess.pgn, random

def count_responses(fen):
  board = new_board(fen)
  if board.is_checkmate():
    return 9001
  if board.is_game_over():
    return -25
  return - len(list(board.legal_moves))

def max_next_move(fen):
  board = new_board(fen)
  if board.is_checkmate():
    return -9001
  if board.is_game_over():
    return -25
  return max([count_responses(new_position(fen, move)) for move in board.legal_moves])

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
