import sys
import re
import chess
import random

# main target, random
fen_string = sys.argv[1]

board = chess.Board(fen_string)
moves = list(board.legal_moves)

move = random.sample(moves,1)[0]
board.push(move)

print board
