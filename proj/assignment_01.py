"""
Atiq Sujela
CSE 30 Assignment 1

This program is a solution to Rosalind DNA

Given: A DNA string s. Max length is 1000 nt

Return: Percent of CG content in the DNA String
"""

import sys


def main():
  # Variable to count the total length of the DNA String
  length = 0
  # Variable that counts the number of C and G nucleotides in the String
  CG_number = 0

  # loops through the input
  for nuc in sys.stdin.read():
    if nuc in ('A', 'C', 'T', 'G'):
      length += 1
      if nuc in ('C', 'G'):
        CG_number += 1

  if length == 0:
    length = 1
  # Converts into a percentage
  percent = CG_number / length
  print(round(percent * 100, 6))


main()
