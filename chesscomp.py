import re
import chess
import chess.pgn
import random

def count_responses(board):
  return len(list(board.legal_moves))

def mate_or_minimum(response_counts):
  return len(response_counts) and min(response_counts) or 9001

def move_minimum(board):
  return mate_or_minimum([on_updated_board_do(board, move, count_responses) for move in board.legal_moves])

def on_updated_board_do(board, move, routine):
  board.push(move)
  result = routine(board)
  board.pop()
  return result

def make_move(board):
  moves = list(board.legal_moves)
  random.shuffle(moves)
  evaluations = [on_updated_board_do(board, move, move_minimum) for move in moves]
  return moves[evaluations.index(max(evaluations))]
