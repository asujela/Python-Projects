'''
Atiq Sujela
CSE 30
Assignment 2: Protein and Genes
'''

amino = {}


def loadDict():
  key = ""
  letter = ""
  file = open("/srv/datasets/amino", "r")
  lines = file.readlines()
  for line in lines:
    key = line[0:3]
    key = key.replace("T", "U")
    letter = line[8]
    amino[key] = letter
  file.close()


def prot(rna):
  length = len(rna)
  protein = ""
  flag = False
  flag2 = True
  start = 0
  x = 0
  number_stop = 0
  while x < length:
    try:
      if not flag and rna[x:(x + 3)] == "AUG":
        protein += amino[rna[x:(x + 3)]]
        start = x
        flag = True
        x += 3
      elif flag and rna[x:(x + 3)] in ("UAA", "UGA", "UAG"):
        if (x - start) >= 36 and flag2:
          protein += amino[rna[x:(x + 3)]]
          flag2 = False
        else:
          number_stop += 1
          break
        x += 3
      elif flag:
        protein += amino[rna[x:(x + 3)]]
        x += 3
        if not flag2:
          number_stop += 1
      else:
        x += 1
    except KeyError:
      break

  if len(protein) >= 11 and number_stop < 1:
    if protein[len(protein) - 1] == "O":
      protein = protein.replace("O", "")
    else:
      protein = None
  else:
    protein = None

  return protein


def potential_proteins(rna):
  length = int(len(rna))
  sequence = ""
  proteins = []

  for x in range(0, length):
    x2 = x + 3
    try:
      if rna[x:x2] == "AUG":
        sequence = ""
        for d in range(x, length, 3):
          d2 = d + 3
          if rna[d:d2] in ("UAA", "UGA", "UAG") and len(sequence) > 10:
            proteins.append(sequence)
            sequence = ""
            break
          else:
            sequence += amino[rna[d:d2]]
            if rna[d:d2] in ("UAA", "UGA", "UAG"):
              break
    except KeyError:
      continue
  rna = ""
  return proteins


loadDict()
