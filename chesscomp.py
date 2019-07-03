import re
import chess
import chess.pgn
import random

def count_responses(move, board):
  board.push(move)
  move_count = len(list(board.legal_moves))
  board.pop()
  return move_count

def mate_or_minimum(response_counts):
  if len(response_counts):
    return min(response_counts)
  else:
    return 9001

def move_minimum(move1, board):
  board.push(move1)
  result = mate_or_minimum([count_responses(move2, board) for move2 in board.legal_moves])
  board.pop()
  return result

def make_move(board):
  moves = list(board.legal_moves)
  random.shuffle(moves)
  evaluations = [move_minimum(move, board) for move in moves]
  return moves[evaluations.index(max(evaluations))]
