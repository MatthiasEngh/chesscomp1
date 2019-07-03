import re
import chess
import chess.pgn
import random

def count_responses(fen):
  return len(list(chess.Board(fen).legal_moves))

def mate_or_minimum(response_counts):
  return len(response_counts) and min(response_counts) or 9001

def move_minimum(fen):
  return mate_or_minimum([on_updated_board_do(fen, move, count_responses) for move in chess.Board(fen).legal_moves])

def on_updated_board_do(fen, move, routine):
  board = chess.Board(fen)
  board.push(move)
  return routine(board.fen())

def make_move(fen):
  moves = list(chess.Board(fen).legal_moves)
  random.shuffle(moves)
  evaluations = [on_updated_board_do(fen, move, move_minimum) for move in moves]
  return moves[evaluations.index(max(evaluations))]
