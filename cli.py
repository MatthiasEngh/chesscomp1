import sys
import chesscomp
import chess

# main target, random
fen_string = sys.argv[1]

new_fen = chesscomp.make_move(fen_string)

print(chess.Board(new_fen))
