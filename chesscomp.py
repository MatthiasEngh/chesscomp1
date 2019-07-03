import re
import chess
import chess.pgn
import random

def count_responses(fen):
  return len(list(chess.Board(fen).legal_moves))

def mate_or_minimum(response_counts):
  return len(response_counts) and min(response_counts) or 9001

def move_minimum(fen):
  return mate_or_minimum([count_responses(update_fen(fen, move)) for move in chess.Board(fen).legal_moves])

def update_fen(fen, move):
  board = chess.Board(fen)
  board.push(move)
  return board.fen()

def make_move(fen):
  moves = list(chess.Board(fen).legal_moves)
  random.shuffle(moves)
  evaluations = [move_minimum(update_fen(fen, move)) for move in moves]
  return moves[evaluations.index(max(evaluations))]
