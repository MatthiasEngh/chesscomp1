import re
import chess
import random

def evaluate_nodes(nodes, evaluator):
  for node in nodes:
    yield apply_metric(node, evaluator)

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

def legal_moves(board):
  for move in board.legal_moves:
    yield [move, board]

def find_move_with_fewest_opponent_options(board):
  itermoves = legal_moves(board)
  moves_with_options = evaluate_nodes(itermoves, count_moves_eval)
  result = minimize(moves_with_options)
  return result[0]

def find_move_with_max_next_turn_options(board):
  moves_with_minimized_options = (board)
  result = maximize(moves_with_minimized_options)
  return result[0]

def count_moves_eval(move_and_board):
  board = move_and_board[1]
  move = move_and_board[0]
  board.push(move)
  move_count = len(list(board.legal_moves))
  board.pop()
  return move_count

def apply_metric(node, evaluator):
  return [node[0], evaluator(node)]

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
