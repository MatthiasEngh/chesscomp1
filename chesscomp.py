import chess, chess.pgn, random

def count_responses(fen):
  board = chess.Board(fen)
  if board.is_checkmate():
    return 9001
  return - len(list(board.legal_moves))

def max_next_move(fen):
  board = chess.Board(fen)
  if board.is_checkmate():
    return -9001
  return max([count_responses(new_position(fen, move)) for move in board.legal_moves])

def move_minimum(fen):
  board = chess.Board(fen)
  if board.is_checkmate():
    return 9001
  return min([max_next_move(new_position(fen, move)) for move in board.legal_moves])

def new_position(fen, move):
  board = chess.Board(fen)
  board.push(move)
  return board.fen()

def make_move(fen):
  moves = list(chess.Board(fen).legal_moves)
  random.shuffle(moves)
  evaluations = [move_minimum(new_position(fen, move)) for move in moves]
  found_max = max(evaluations)
  return moves[evaluations.index(found_max)]
