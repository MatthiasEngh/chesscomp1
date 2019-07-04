import chess, chess.pgn, random

def count_responses(fen):
  return len(list(chess.Board(fen).legal_moves))

def move_minimum(fen):
  if chess.Board(fen).is_checkmate():
    return 9001
  return min([count_responses(new_position(fen, move)) for move in chess.Board(fen).legal_moves])

def new_position(fen, move):
  board = chess.Board(fen)
  board.push(move)
  return board.fen()

def make_move(fen):
  moves = list(chess.Board(fen).legal_moves)
  random.shuffle(moves)
  evaluations = [move_minimum(new_position(fen, move)) for move in moves]
  return moves[evaluations.index(max(evaluations))]
