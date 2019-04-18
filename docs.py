import chesscomp
import doctest
import chess
import chess_library as library

def apply_metric(*args, **kwargs):
  """ returns a result formatted [move, evaluation]
    >>> board = chess.Board()
    >>> def evaluator(move_and_board):
    ...   return 1
    >>> move = next(iter(board.legal_moves))
    >>> result = apply_metric([move, board], evaluator)
    >>> type(result[1])
    <class 'int'>
    >>> result[0] == move
    True
  """
  return library.apply_metric(*args, **kwargs)

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
