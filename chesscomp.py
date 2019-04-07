import re
import chess
import random

def evaluate_moves(board, evaluator):
  moves = iter(board.legal_moves)
  for move in moves:
    yield apply_metric(board, move, evaluator)

def maximize(evaluated_moves):
  current_result = next(evaluated_moves)
  for move_evaluation in evaluated_moves:
    current_result = min_result(current_result, move_evaluation)
  return current_result

def minimize(evaluated_moves):
  current_result = next(evaluated_moves)
  for move_evaluation in evaluated_moves:
    current_result = min_result(current_result, move_evaluation)
  return current_result

def find_move_with_fewest_opponent_options(board):
  moves_with_options = evaluate_moves(board, count_moves)
  result = minimize(moves_with_options)
  return result[0]

def find_move_with_max_next_turn_options(board):
  moves_with_minimized_options = (board)
  result = maximize(moves_with_minimized_options)
  return result[0]

def count_moves(board):
  return len(list(board.legal_moves))

def evaluate_move(board, move, evaluator):
  board.push(move)
  evaluation = evaluator(board)
  board.pop()
  return evaluation

def apply_metric(board, move, evaluator):
  return [move, evaluate_move(board, move, evaluator)]

def min_result(result1, result2):
  if result1[1] < result2[1]: # minimizes result
    return result1
  elif result1[1] == result2[1]:
    return random.choice([result1, result2])
  else:
    return result2

def max_result(result1, result2):
  if result1[1] > result2[1]: # max result
    return result1
  elif result1[1] == result2[1]:
    return random.choice([result1, result2])
  else:
    return result2

def make_move(fen_string):
  board = chess.Board(fen_string)
  move = find_move_with_fewest_opponent_options(board)
  board.push(move)
  return board.fen()
