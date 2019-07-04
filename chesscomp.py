import chess, chess.pgn, random

def count_responses(fen):
  return len(list(chess.Board(fen).legal_moves))

def move_minimum(fen):
  return chess.Board(fen).is_checkmate() and 9001 or min([count_responses(new_position(fen, move)) for move in chess.Board(fen).legal_moves])

def new_position(fen, move):
  board = chess.Board(fen)
  board.push(move)
  return board.fen()

def make_move(fen):
  moves = list(chess.Board(fen).legal_moves)
  random.shuffle(moves)
  evaluations = [move_minimum(new_position(fen, move)) for move in moves]
  return moves[evaluations.index(max(evaluations))]
