import re
import chess
import chess.pgn
import io
import random
import chess_library as library

def moves_with_minimized_responses(board):
  for move in board.legal_moves:
    board.push(move)
    min_result = library.minimize(library.legal_moves(board), library.count_moves_eval)[1]
    yield [move, min_result]
    board.pop()

def make_move(pgn_string):
  pgn = io.StringIO(pgn_string)
  game = chess.pgn.read_game(pgn)
  board = game.board()
  move_data = moves_with_minimized_responses(board)
  result = library.maximize(move_data, library.node_value)
  return result[0]
