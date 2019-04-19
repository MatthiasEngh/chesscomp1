import chesscomp
import doctest
import chess
import chess_library as library

def is_sorted(iterable):
  iterator = iter(iterable)
  previous_value = library.node_value(next(iterator))
  for node in iterator:
    next_value = library.node_value(node)
    if next_value < previous_value:
      raise ValueError("not sorted %s" % [previous_value, next_value])
    previous_value = next_value

def sort(iterable):
  """ takes iterable of evaluated nodes and returns sorted iterable
    >>> iterable1 = library.legal_moves(chess.Board("rnb1kb1r/pp3ppp/4pq2/2pp4/3P4/2N2N2/PPP1PPPP/R2QKB1R w KQkq c6 0 6"))
    >>> iterable2 = library.evaluate_nodes(iterable1, library.count_moves_eval)
    >>> sorted_iterable = library.sort(iterable2)
    >>> is_sorted(sorted_iterable)
  """

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
