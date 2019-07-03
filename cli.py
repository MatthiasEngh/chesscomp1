import chess
import chesscomp
import io
import sys

# main target, random
pgn_string = sys.argv[1]

pgn = io.StringIO(pgn_string)
game = chess.pgn.read_game(pgn)

move = chesscomp.make_move(game.board())

print(move)
