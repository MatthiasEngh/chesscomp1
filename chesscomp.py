import re
import chess
import random
import chess_library as library

def moves_with_minimized_responses(board):
  for move in board.legal_moves:
    board.push(move)
    min_result = library.minimize(library.legal_moves(board), library.count_moves_eval)[1]
    yield [move, min_result]
    board.pop()

def make_move(fen_string):
  board = chess.Board(fen_string)
  move_data = moves_with_minimized_responses(board)
  result = library.maximize(move_data, library.node_value)
  board.push(result[0])
  return board.fen()
