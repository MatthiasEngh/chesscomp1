import re
import chess
import chess.pgn
import io
import random

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

def node_value(move_and_value):
  return move_and_value[1]

def make_move(pgn_string):
  pgn = io.StringIO(pgn_string)
  game = chess.pgn.read_game(pgn)
  board = game.board()

  all_legal_moves = list(board.legal_moves)
  move_data = [None] * len(all_legal_moves)
  for i in range(len(all_legal_moves)):
    move = all_legal_moves[i]
    board.push(move)

    node_evaluations = evaluate_nodes(legal_moves(board), count_moves_eval)
    current_result = next(node_evaluations)
    for evaluation in node_evaluations:
      if current_result[1] < evaluation[1]:
        pass
      elif current_result[1] == evaluation[1]:
        current_result = random.choice([current_result, evaluation])
      else:
        current_result = evaluation

    move_data[i] = [move, current_result[1]]
    board.pop()

  node_evaluations = evaluate_nodes(move_data, node_value)
  current_result = next(node_evaluations)
  for evaluation in node_evaluations:
    if current_result[1] > evaluation[1]:
      pass
    elif current_result[1] == evaluation[1]:
      current_result = random.choice([current_result, evaluation])
    else:
      current_result = evaluation
  result = current_result

  return result[0]
