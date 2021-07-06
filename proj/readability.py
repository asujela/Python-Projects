"""
Utility module for dealing with readability metrics of English text.
"""
from __future__ import annotations

__author__ = 'A student in CSE 30,asujela@ucsc.edu'

# import sys
import math
import re

syllables = {}


def loadDict():
  count = 1
  key = ""
  fin = open("/srv/datasets/syllables.txt", "r")
  lines = fin.readlines()

  for line in lines:
    count = line.count(";") + 1
    key = line.replace(";", "")
    key = key.replace("\n", "")
    if key in syllables:
      if syllables[key] < count:
        syllables[key] = int(count)
    else:
      syllables[key] = int(count)
  fin.close()


class Readability(str):
  """
  Represents a string that can be assessed for readability metrics of English text.
  """

  def words(self):
    words = re.split("[^A-Za-z0-9'-]", self)
    words_cleaned = [i.strip("-'") for i in words]
    words_cleaned = list(filter(None, words_cleaned))

    return words_cleaned

  def letters(self):
    count = 0
    words = self
    for w in words:
      if w.isalpha():
        count += 1
      elif w.isdigit():
        count += 1
    return count

  def has_alpha(self, word):
    count = 0
    for c in word:
      if c.isalpha():
        count += 1
        break
      elif c.isdigit():
        count += 1
        break
    return count >= 1

  def sentences(self):
    sentences = []
    s2 = []
    s = self.split()
    s = [w.strip(":;\",()[]{}-@$%&_+=*'#/\\|") for w in s]
    s = [w.replace("\u00ad", "") for w in s]
    s = list(filter(None, s))
    for w in s:
      s2.append(w)
      if w.endswith('.') or w.endswith('!') or w.endswith('?'):
        if self.has_alpha(w):
          sentences.append(s2)
          s2 = []
    return sentences

  def num_syllables(self):
    count = 0
    word = self.words()
    for w in word:
      w = w.rstrip("-")
      w = w.lstrip("-")
      w = w.rstrip("'")
      w = w.lstrip("'")
      if w.lower() in syllables:
        count += syllables[w.lower()]
      else:
        count += 1
    return count

  def polysyllabic_words(self):
    count = []
    word = self.words()
    for w in word:
      w = w.rstrip("-")
      w = w.lstrip("-")
      if w.lower() in syllables and syllables[w.lower()] > 2:
        count.append(w)

    return count

  def automated_readability_index(self) -> float:
    """
    Calculates and returns the automated readability index of this text.
    See: https://en.wikipedia.org/wiki/Automated_readability_index
    """
    w = float(len(self.words()))
    c = float(self.letters())
    s = float(len(self.sentences()))
    cw = c / w
    ws = w / s
    return float(4.71 * cw + 0.5 * ws - 21.43)

  def coleman_liau_index(self) -> float:
    """
    Calculates and returns the Coleman–Liau index of this text.
    See: https://en.wikipedia.org/wiki/Coleman%E2%80%93Liau_index
    """
    w = float(len(self.words()))
    c = float(self.letters())
    s = float(len(self.sentences()))
    L = (c / w) * 100.0
    S = (s / w) * 100.0
    return float((0.0588 * L) - (0.296 * S) - 15.8)

  def flesch_kincaid_grade(self) -> float:
    """
    Calculates and returns the Flesch–Kincaid grade level of this text.
    """
    w = float(len(self.words()))
    c = float(self.num_syllables())
    s = float(len(self.sentences()))
    return 0.39 * (w / s) + 11.8 * (c / w) - 15.59

  def smog_grade(self) -> float | None:
    """
    Calculates and returns the SMOG grade of this text,
    or None if the text contains fewer than 30 sentences.
    See: https://en.wikipedia.org/wiki/SMOG
    """
    s = float(len(self.sentences()))
    p = float(len(self.polysyllabic_words()))
    if s < 30:
      return None
    else:
      return 1.0430 * math.sqrt(p * (30.0 / s)) + 3.1291


loadDict()
