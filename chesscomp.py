import re
import chess
import chess.pgn
import random

def legal_responses(move, board):
  board.push(move)
  result = list(board.legal_moves)
  board.pop()
  return result

def count_responses(move, board):
  move_count = len(legal_responses(move, board))
  return move_count

def mate_or_minimum(response_counts):
  if len(response_counts):
    return min(response_counts)
  else:
    return 9001

def move_minimum(move1, board):
  result = mate_or_minimum([count_responses(move2, board) for move2 in legal_responses(move1, board)])
  return result

def make_move(board):
  current_best = 0
  for move in board.legal_moves:
    evaluation = move_minimum(move, board)
    if current_best > evaluation:
      next
    elif current_best == evaluation:
      result = random.choice([result, move])
    else:
      current_best = evaluation
      result = move

  return result
