import chess
import chesscomp

board = chess.Board()

while not board.is_game_over():
  move = chesscomp.make_move(board.fen())
  print(move)
  board.push(move)
