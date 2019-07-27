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

def max_next_move(board, move):
  board.push(move)
  if board.is_checkmate():
    result = -9001
  elif board.is_game_over():
    result = -25
  else:
    result = max([count_responses(board, move) for move in board.legal_moves])
  board.pop()
  return result

def move_minimum(board, move):
  board.push(move)
  if board.is_checkmate():
    result = 9001
  elif board.is_game_over():
    result = -25
  else:
    result = min([max_next_move(board, move) for move in board.legal_moves])
  board.pop()
  return result

def new_board(fen):
  return chess.Board(fen)

def make_move(fen):
  moves = list(new_board(fen).legal_moves)
  random.shuffle(moves)
  evaluations = [move_minimum(new_board(fen), move) for move in moves]
  found_max = max(evaluations)
  return moves[evaluations.index(found_max)]
