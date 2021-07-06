"""
A module demonstrating generator functions and related concepts.
"""

__author__ = "A student in CSE 30, asujela@ucsc.edu"

from collections.abc import Callable, Iterator  # For typing hints (we'll talk about "abc" later)


def elements_under(sequence: Iterator[int], bound: int, predicate: Callable[[int], bool] = None) \
    -> Iterator[int]:
  """
  Yields a finite sequence of elements under a given bound, optionally matching a predicate.

  :param sequence: an infinite sequence of integers, e.g. primes()
  :param bound: an exclusive upper bound for the yielded sequence
  :param predicate: an optional function used to select values from the sequence
  :yield: all elements from sequence comparing less than bound. If predicate is not None, only
          yields values for which predicate returns True
  """
  val_current = 0
  if predicate is None:
    while True:
      val_current = next(sequence)
      if val_current < bound:
        yield val_current
      else:
        break
  else:
    while True:
      val_current = next(sequence)
      if val_current < bound:
        if predicate(val_current):
          yield val_current
      else:
        break


def is_prime(n: int) -> bool:
  """ Returns whether n is prime. """
  if n > 2:
    if n % 2 != 0:
      for x in range(3, int(n / 2)):
        if n % x == 0:
          return False
      return True
  elif n == 2:
    return True

  return False


def nth_element(sequence: Iterator[int], n: int) -> int:
  """
  Returns the nth element of a possibly infinite sequence of integers.

  :param sequence: a sequence of integers, e.g. primes()
  :param n: the sequence index desired
  :return: the value at index n of the sequence
  """
  value = 0
  while n >= 0:
    value = next(sequence)
    n -= 1

  return value


def primes() -> Iterator[int]:
  """ Yields an infinite sequence of prime numbers, in ascending order. """
  two_back, back, current = 2, 3, 5
  n = 6
  yield two_back
  yield back
  yield current
  while True:
    if is_prime(n):
      two_back = back
      back = current
      current = n
      yield current
    n += 1


def prime_factors(n: int) -> list[int]:
  """ Returns a list of prime numbers with product n, in ascending order. """
  factors = []
  while True:
    if n % 2 == 0:
      factors.append(2)
      n = n / 2
    else:
      break
  for x in range(3, int(n / 2)):
    if is_prime(x):
      while True:
        if n % x == 0:
          factors.append(x)
          n = n / x
        else:
          break
  if is_prime(n):
    factors.append(n)
  return factors


def semiprimes():
  """ Yields an infinite sequence of semiprimes, in ascending order. """
  n = 10
  two_back, back, current = 4, 6, 9
  yield two_back
  yield back
  yield current
  while True:
    for x in range(2, int(n**0.5) + 1):
      if n % x == 0:
        y = n / x
        if is_prime(x) and is_prime(y):
          two_back = back
          back = current
          current = n
          yield current
    n += 1


if __name__ == '__main__':
  assert all(is_prime(n) for n in (2, 3, 5, 7))
  assert all(not is_prime(n) for n in (4, 6, 8, 9))
  assert list(elements_under(primes(), 10)) == [2, 3, 5, 7]
  assert list(elements_under(semiprimes(), 10)) == [4, 6, 9]
  assert nth_element(primes(), 2) == 5
  assert nth_element(semiprimes(), 2) == 9
  assert list(elements_under(primes(), 1386, lambda p: not 1386 % p)) == [2, 3, 7, 11]
  assert prime_factors(1386) == [2, 3, 3, 7, 11]
