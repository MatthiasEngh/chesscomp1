import re
import chess
import chess.pgn
import random

def count_responses(move, board):
  board.push(move)
  move_count = len(list(board.legal_moves))
  board.pop()
  return move_count

def move_minimum(move1, board):
  board.push(move1)
  result = min([count_responses(move2, board) for move2 in board.legal_moves])
  board.pop()
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
