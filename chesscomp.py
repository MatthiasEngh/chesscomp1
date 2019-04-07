import re
import chess
import random

def evaluate_moves_by_options(board):
  moves = iter(board.legal_moves)
  for move in moves:
    yield apply_metric(board, move)

def minimize(evaluated_moves):
  current_result = next(evaluated_moves)
  for move_evaluation in evaluated_moves:
    current_result = min_result(current_result, move_evaluation)
  return current_result

def find_move_with_fewest_opponent_options(board):
  evaluated_moves = evaluate_moves_by_options(board)
  result = minimize(evaluated_moves)
  return result[0]

def evaluate_position(board):
  return len(list(board.legal_moves))

def evaluate_move(board, move):
  board.push(move)
  evaluation = evaluate_position(board)
  board.pop()
  return evaluation

def apply_metric(board, move):
  return [move, evaluate_move(board, move)]

def min_result(result1, result2):
  if result1[1] < result2[1]: # minimizes opponent moves
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
