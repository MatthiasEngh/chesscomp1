import re
import chess
import random

def find_move_with_fewest_opponent_options(board):
  moves = iter(board.legal_moves)
  current_best = apply_metric(board, next(moves))
  for move in moves:
    current_result = apply_metric(board, move)
    current_best = max_result(current_best, current_result)
  return current_best

def evaluate_position(board):
  return len(list(board.legal_moves))

def evaluate_move(board, move):
  board.push(move)
  evaluation = evaluate_position(board)
  board.pop()
  return evaluation

def apply_metric(board, move):
  result = [move, evaluate_move(board, move)]
  return result

def max_result(result1, result2):
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
