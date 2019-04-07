import chess
import random

def make_move(fen_string):
  board = chess.Board(fen_string)
  move = random.sample(list(board.legal_moves),1)[0]
  board.push(move)
  return board.fen()
