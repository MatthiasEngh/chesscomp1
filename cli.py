import sys
import chesscomp

# main target, random
fen_string = sys.argv[1]

new_fen = chesscomp.make_move(fen_string)

print(new_fen)
