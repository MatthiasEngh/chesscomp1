import sys
import re
import chess
import random

# main target, random
fen_string = sys.argv[1]

board = chess.Board(fen_string)
moves = iter(board.legal_moves)

def evaluate_position(board):
  return len(board.legal_moves)

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

current_best = apply_metric(board, moves.next())

for move in moves:
  current_result = apply_metric(board, move)
  current_best = max_result(current_best, current_result)

# return decision
move = current_best[0]
board.push(move)

print board
