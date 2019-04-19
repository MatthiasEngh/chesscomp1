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

def find_move_with_max_next_turn_options(board):
  move_data = moves_with_minimized_responses(board)
  result = library.maximize(move_data, library.node_value)
  return result[0]

def make_move(fen_string):
  board = chess.Board(fen_string)
  move = find_move_with_max_next_turn_options(board)
  board.push(move)
  return board.fen()
