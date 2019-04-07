import re
import chess
import random

def evaluate_nodes(nodes, evaluator):
  for node in nodes:
    yield apply_metric(node, evaluator)

def maximize(itermoves, count_moves_eval):
  evaluated_moves = evaluate_nodes(itermoves, count_moves_eval)
  current_result = next(evaluated_moves)
  for move_evaluation in evaluated_moves:
    current_result = max_result(current_result, move_evaluation)
  return current_result

def minimize(itermoves, count_moves_eval):
  evaluated_moves = evaluate_nodes(itermoves, count_moves_eval)
  current_result = next(evaluated_moves)
  for move_evaluation in evaluated_moves:
    current_result = min_result(current_result, move_evaluation)
  return current_result

def legal_moves(board):
  for move in board.legal_moves:
    yield [move, board]

def find_move_with_fewest_opponent_options(board):
  result = minimize(legal_moves(board), count_moves_eval)
  return result[0]

def min_personal_moves(board):
  for move in board.legal_moves:
    board.push(move)
    min_result = minimize(legal_moves(board), count_moves_eval)[1]
    yield [move, min_result]
    board.pop()

def node_value_eval(move_and_value):
  return move_and_value[1]

def find_move_with_max_next_turn_options(board):
  moves_with_minimized_responses = min_personal_moves(board)
  result = maximize(moves_with_minimized_responses, node_value_eval)
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
  move = find_move_with_max_next_turn_options(board)
  board.push(move)
  return board.fen()
