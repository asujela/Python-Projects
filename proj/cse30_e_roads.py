"""
Atiq Sujela
CSE 30 Spring 2021
Assignment 09
"""
import sys
import math
from collections import defaultdict


def loadNames():
  fin = open("/srv/datasets/e-roads/vertex_names.txt", "r")
  tict = {}
  tict2 = {}
  key = 0
  nme = ""
  for line in fin:
    key = int(line.split()[0])
    nme = str(" ".join(line.split()[1:]))
    tict[nme] = key
    tict2[key] = nme
  fin.close()
  return tict, tict2


def loadCoordinates():
  fin = open("/srv/datasets/e-roads/vertex_lcations.txt", "r")
  tict = {}
  key = 0
  l1 = 0
  l2 = 0
  for line in fin:
    key = int(line.split()[0])
    l1 = float(line.split()[1])
    l2 = float(line.split()[2])
    tict[key] = [l1, l2]
  fin.close()
  return tict


def loadGraph():
  g = defaultdict(dict)
  fin = open("/srv/datasets/e-roads/network.txt", "r")
  k1 = 0
  k2 = 0
  for line in fin:
    k1 = int(line.split()[0])
    k2 = int(line.split()[1])
    ed = edge(k1, k2)
    g[k1][k2] = ed
    g[k2][k1] = ed
  fin.close()
  return g


def edge(key1, key2):
  """
  Code is ported from Javascript version
  from moveable-type.co.uk
  """
  global coord
  r = 6371000
  lat1 = coord[key1][0]
  lon1 = coord[key1][1]

  lat2 = coord[key2][0]
  lon2 = coord[key2][1]
  t1 = lat1 * (math.pi / 180)
  t2 = lat2 * (math.pi / 180)
  ct = (lat2 - lat1) * (math.pi / 180)
  cl = (lon2 - lon1) * (math.pi / 180)

  a1 = math.sin(ct / 2) * math.sin(ct / 2)
  a2 = math.cos(t1) * math.cos(t2)
  a3 = math.sin(cl / 2) * math.sin(cl / 2)
  a = a1 + (a2 * a3)
  c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

  d = (r * c) / 1000
  return float(d)


def isPath(l1, l2):
  global graph
  point = l1
  visit = [False] * len(graph)
  visitList = []
  visitList.append(point)
  while visitList:
    point = visitList.pop(0)
    for lc in graph[point]:
      if not visit[lc]:
        visitList.append(lc)
        visit[lc] = True
      if lc == l2:
        break
    if visit[l2]:
      return True
  return False


def fastestPath(start, end):
  global graph
  dist = {}
  prev = {}
  prioQ = []
  new_dist = 0
  lg = 0
  node = 0
  a = []
  for i in graph:
    dist[i] = float('inf')
    prev[i] = None
  dist[start] = 0
  prioQ.append((0, start))
  while prioQ:
    lg, node = prioQ.pop()
    for n in graph[node]:
      new_dist = lg + graph[node][n]
      if new_dist < dist[n]:
        dist[n] = new_dist
        prev[n] = node
        prioQ.append((new_dist, n))
  node = end
  while node != start:
    a.insert(0, node)
    node = prev[node]
  a.insert(0, start)
  return a


def url(arr):
  u1 = "https://www.google.com/maps/dir"
  for i in arr:
    u1 += "/"
    u1 += "%.3f" % round(coord[i][0], 3) + ","
    u1 += "%.3f" % round(coord[i][1], 3)
  return u1


if __name__ == '__main__':
  name, name2 = loadNames()
  coord = loadCoordinates()
  graph = loadGraph()
  lc1 = sys.argv[1]
  lc2 = sys.argv[2]

  try:
    num1 = name[lc1]
  except KeyError:
    err = "Error: Unknown city: '{}'\n".format(lc1)
    sys.stderr.write(err)
    sys.exit(1)

  try:
    num2 = name[lc2]
  except KeyError:
    err = "Error: Unknown city: '{}'\n".format(lc2)
    sys.stderr.write(err)
    sys.exit(1)

  ans = [1]

  if lc1 == lc2:
    ans = [num1]
  elif isPath(num1, num2):
    ans = fastestPath(num1, num2)
  else:
    sys.stderr.write("No path from {} to {}!\n".format(lc1, lc2))
    sys.exit(1)

  if len(sys.argv) > 3:
    print(url(ans))
  else:
    for nm in ans:
      print(name2[nm])
