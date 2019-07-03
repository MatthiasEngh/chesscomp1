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

def make_move(pgn_string):
  pgn = io.StringIO(pgn_string)
  game = chess.pgn.read_game(pgn)
  board = game.board()

  all_legal_moves = list(board.legal_moves)
  next_turn_options_count_minima = [None] * len(all_legal_moves)
  for i in range(len(all_legal_moves)):
    move = all_legal_moves[i]
    board.push(move)

    next_turn_options_count = [[move, count_responses(move, board)] for move in board.legal_moves]

    current_result = next_turn_options_count[0]
    for evaluation in next_turn_options_count[1:]:
      if current_result[1] < evaluation[1]:
        pass
      elif current_result[1] == evaluation[1]:
        current_result = random.choice([current_result, evaluation])
      else:
        current_result = evaluation

    next_turn_options_count_minima[i] = [move, current_result[1]]
    board.pop()

  current_result = next_turn_options_count_minima[0]
  for evaluation in next_turn_options_count_minima[1:]:
    if current_result[1] > evaluation[1]:
      pass
    elif current_result[1] == evaluation[1]:
      current_result = random.choice([current_result, evaluation])
    else:
      current_result = evaluation
  result = current_result

  return result[0]
