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
    board.push(all_legal_moves[i])

    next_turn_options_count = [[move, count_responses(move, board)] for move in board.legal_moves]

    worst_response_with_value = next_turn_options_count[0]
    for evaluation in next_turn_options_count[1:]:
      if worst_response_with_value[1] < evaluation[1]:
        pass
      elif worst_response_with_value[1] == evaluation[1]:
        worst_response_with_value = random.choice([worst_response_with_value, evaluation])
      else:
        worst_response_with_value = evaluation

    next_turn_options_count_minima[i] = [all_legal_moves[i], worst_response_with_value[1]]
    board.pop()

  best_move_with_value = next_turn_options_count_minima[0]
  for evaluation in next_turn_options_count_minima[1:]:
    if best_move_with_value[1] > evaluation[1]:
      pass
    elif best_move_with_value[1] == evaluation[1]:
      best_move_with_value = random.choice([best_move_with_value, evaluation])
    else:
      best_move_with_value = evaluation

  return best_move_with_value[0]
