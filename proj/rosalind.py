"""
Contains class Protein for working with protein-related information.
"""

__author__ = 'A student in CSE 30, asujela@ucsc.edu'

massTable = {}


def loadDict():
  m = 0.0
  key = ""
  file = open("/srv/datasets/amino-monoisotopic-mass", "r")
  lines = file.readlines()

  for line in lines:
    key = line[0]
    m = line[2:]
    massTable[key] = float(m)


class Protein:
  """ Represents an immutable sequence of amino acids. """
  amino = ""

  def __init__(self, aminos=None):
    """
    Constructs a protein from a sequence of amino acids.
    See: http://rosalind.info/problems/prot/

    :param aminos: A sequence of single-character strings, expected to be in the amino-acid alphabet
    :raise: ValueError if aminos contains characters not found in the amino-acid alphabet
    """
    x = ""
    if isinstance(aminos, list):
      x = "".join(aminos)
    else:
      x = aminos

    if any(base not in 'ARNDCQEGHILKMFPSTWYV' for base in x):
      raise ValueError('Invalid amino acid character')

    self.amino = x

  def __add__(self, addition):
    """
    The + operator concatenates two proteins.

    :param addition: a sequence of single-character strings in the amino-acid alphabet
    :return: a new Protein object representing the concatenation of this protein and the addition
    :raise: ValueError if addition contains characters not found in the amino acid-alphabet
    """
    x = ""
    if isinstance(addition, list):
      x = "".join(addition)
    else:
      x = str(addition)
    if any(base not in 'ARNDCQEGHILKMFPSTWYV' for base in x):
      raise ValueError('Invalid amino acid character: ')

    return Protein(str(self.amino) + x)

  def __eq__(self, other):
    """
    Two proteins will be equal if they represent the same sequence of amino acids.

    :param other: a sequence of single-character strings in the amino-acid alphabet
    :return: whether this protein is equal to the other
    """
    x = ""
    if isinstance(other, list):
      x = "".join(other)
    else:
      x = other

    return str(self.amino) == str(x)

  def __getitem__(self, key):
    """
    The [] operator allows users to retrieve individual amino acids in a protein by index,
    or a Protein object representing a slice of this protein.

    :param key: an index or slice
    :return: a single-character string (if key was an index) or a Protein (if key was a slice)
    :raise: IndexError if index is out of range
    """
    if isinstance(key, slice):

      return Protein(self.amino[key])
    else:
      if key < len(self.amino):
        return self.amino[key]
      else:
        raise IndexError('Key given is larger than protein length')

  def __len__(self):
    return len(self.amino)

  def __repr__(self):
    """ Returns a string that would result in reproducing this protein when interpreted. """
    return "Protein('" + str(self) + "')"

  def __str__(self):
    """ Returns a string containing the amino-acid letters for this protein. """
    return str(self.amino)

  def mass(self):
    """
    Returns the mass of this protein (in Daltons), according to the monoisotopic mass table.
    See: http://rosalind.info/problems/prtm/
    """
    mass = 0.0
    for n in self.amino:
      mass += massTable[n]
    return mass


loadDict()
