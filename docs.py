import chesscomp
import doctest
import chess
import chess_library as library

def make_move(*args, **kwargs):
  """ takes fen as argument and returns different fen
    >>> fen_string = chess.Board().fen()
    >>> new_fen = make_move(fen_string)
    >>> type(new_fen)
    <class 'str'>
    >>> chess.Board(new_fen).is_valid()
    True
  """
  return chesscomp.make_move(*args, **kwargs)

doctest.testmod()
