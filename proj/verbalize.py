"""
Atiq Sujela
Assignment 07
CSE 30 Spring 2021
"""
import sys

verb_dict = {}
final_key = 0
key = 0
zero_flag = True


def load_dict():
  global key
  global verb_dict
  global final_key
  ky = 0
  larr = []
  fin = open("/srv/datasets/number_names.txt", "r")
  for line in fin:
    larr = line.split()
    ky = int(larr[1])
    verb_dict[ky] = str(larr[0])
  key = ky
  final_key = ky
  fin.close()


def verbalize(value: int):
  global key
  global final_key
  global zero_flag
  numstr = ""
  new_val = 0
  if value < 1000:
    key = final_key
    numstr = verb_part_two(value)
    return [numstr]
  else:
    if value // key > 0:
      numstr = verb_part_two(value // key) + " " + verb_dict[key]
      new_val = value % key
      key //= 1000
      zero_flag = False
      return list(filter(None, [numstr] + verbalize(new_val)))
    else:
      key //= 1000
      zero_flag = False
      return list(filter(None, [numstr] + verbalize(value)))


def verb_part_two(val: int):
  numstr = ""
  global zero_flag
  if val > 99:
    numstr = verb_dict[val // 100] + " " + verb_dict[100]
    zero_flag = False
    return str((numstr + " " + verb_part_two(val % 100)).strip())
  elif val > 19:
    if val % 10 == 0:
      numstr = verb_dict[val // 10 * 10] + " "
    else:
      numstr = verb_dict[val // 10 * 10] + "-"
    zero_flag = False
    return str((numstr + verb_part_two(val % 10)).strip())
  else:
    if val == 0 and zero_flag:
      return str(verb_dict[0])
    elif val == 0 and not zero_flag:
      zero_flag = True
      return ""
    else:
      zero_flag = True
      return str(verb_dict[val])


load_dict()

if __name__ == '__main__':
  print('\n'.join(verbalize(int(sys.argv[1]))))
