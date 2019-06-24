import sys
import chesscomp

# main target, random
pgn_string = sys.argv[1]

move = chesscomp.make_move(pgn_string)

print(move)
