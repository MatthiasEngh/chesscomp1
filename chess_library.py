import random

def count_moves_eval(move_and_board):
  board = move_and_board[1]
  move = move_and_board[0]
  board.push(move)
  move_count = len(list(board.legal_moves))
  board.pop()
  return move_count

def evaluate_nodes(nodes, evaluator):
  for node in nodes:
    yield [node[0], evaluator(node)]

def legal_moves(board):
  for move in board.legal_moves:
    yield [move, board]

def max_result(result1, result2):
  if result1[1] > result2[1]: # max result
    return result1
  elif result1[1] == result2[1]:
    return random.choice([result1, result2])
  else:
    return result2

def maximize(nodes, node_eval):
  node_evaluations = evaluate_nodes(nodes, node_eval)
  current_result = next(node_evaluations)
  for evaluation in node_evaluations:
    current_result = max_result(current_result, evaluation)
  return current_result

def min_result(result1, result2):
  if result1[1] < result2[1]: # minimizes result
    return result1
  elif result1[1] == result2[1]:
    return random.choice([result1, result2])
  else:
    return result2

def minimize(nodes, node_eval):
  node_evaluations = evaluate_nodes(nodes, node_eval)
  current_result = next(node_evaluations)
  for evaluation in node_evaluations:
    current_result = min_result(current_result, evaluation)
  return current_result

def node_value(move_and_value):
  return move_and_value[1]

def sort(nodes):
  return sorted(nodes, key=node_value)


