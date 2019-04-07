import chesscomp
import doctest
import chess

def apply_metric(board, move):
  """ returns a result formatted [move, evaluation]
    >>> board = chess.Board()
    >>> move = next(iter(board.legal_moves))
    >>> result = apply_metric(board, move)
    >>> type(result[1])
    <class 'int'>
    >>> result[0] == move
    True
  """
  return chesscomp.apply_metric(board, move)

def make_move(fen_string):
  """ takes fen as argument and returns different fen
    >>> fen_string = chess.Board().fen()
    >>> new_fen = make_move(fen_string)
    >>> type(new_fen)
    <class 'str'>
    >>> chess.Board(new_fen).is_valid()
    True
  """
  return chesscomp.make_move(fen_string)

doctest.testmod()
