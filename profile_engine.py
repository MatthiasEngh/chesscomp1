import cProfile
import chesscomp
import chess
import pstats
import io

fen_string = chess.Board().fen()

pr = cProfile.Profile()
pr.enable()
chesscomp.make_move(fen_string)
pr.disable()

s = io.StringIO()
ps = pstats.Stats(pr, stream=s).sort_stats('cumulative')
ps.print_stats()
print(s.getvalue())
