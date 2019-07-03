import re
import chess
import chess.pgn
import io
import random

import random

def count_responses(move, board):
  board.push(move)
  move_count = len(list(board.legal_moves))
  board.pop()
  return move_count

def move_minimum(move1, board):
  board.push(move1)
  result = min([count_responses(move2, board) for move2 in board.legal_moves])
  board.pop()
  return result

def make_move(pgn_string):
  pgn = io.StringIO(pgn_string)
  game = chess.pgn.read_game(pgn)
  board = game.board()

  next_turn_options_count_minima = []
  for move in board.legal_moves:
    next_turn_options_count_minima.append([move, move_minimum(move, board)])

  result = next_turn_options_count_minima[0]
  for evaluation in next_turn_options_count_minima[1:]:
    if result[1] > evaluation[1]:
      pass
    elif result[1] == evaluation[1]:
      result = random.choice([best_move_with_value, evaluation])
    else:
      result = evaluation

  return result[0]
