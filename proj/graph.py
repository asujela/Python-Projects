"""
Assignment 08
Atiq Sujela
CSE 30 Spring 2021
"""


class Graph(dict):
  """
  This is class creates an object that allows data storage in graph that is based
  off of a dictionary
  """
  out = []

  def __setitem__(self, vertex, edge):
    self[vertex] = edge

  def __missing__(self, vertex):
    if vertex not in self:
      super().__setitem__(vertex, {})
      self.out.append(vertex)
    return super().__getitem__(vertex)

  def __delitem__(self, vertex):
    self.pop(vertex)
    self.out.remove(vertex)
    for k in self:
      if vertex in self[k]:
        self[k].pop(vertex)

  def copy(self):
    gtemp = Graph()
    for k in self:
      if self[k] == {}:
        gtemp[k] == {}
        continue
      for i in self[k]:
        gtemp[k][i] = self[k][i]
    return gtemp

  def __len__(self):
    return len(self.vertices())

  def vertices(self):
    temp = []
    for key in self:
      for key2 in self[key]:
        temp.append(key2)
      temp.append(key)
    return set(temp)

  def edges(self):
    temp = []
    for src in self:
      for dst in self[src]:
        temp.append((src, dst, self[src][dst]))
    return set(temp)

  def adjacent(self, src, dst):
    return dst in self[src]

  def neighbors(self, vertex):
    temp = []
    for k in self[vertex]:
      temp.append(k)
    return set(temp)

  def degree(self, vertex):
    return len(self[vertex])

  def path_valid(self, vertices):
    flag = True
    for i in range(len(vertices) - 1):
      if vertices[i] in self:
        if vertices[i + 1] not in self[vertices[i]]:
          flag = False
          break
      else:
        flag = False
        break
    return flag

  def path_length(self, vertices):
    path = 0
    if not self.path_valid(vertices) or len(vertices) < 2:
      return None

    for i in range(len(vertices) - 1):
      if vertices[i] in self:
        path += self[vertices[i]][vertices[i + 1]]
    return path

  def is_connected(self):
    re = {}
    vert = self.vertices()

    for le in vert:
      re[le] = False

    for i in range(len(self.out)):
      root = self.out[i]
      reached = re
      q = []
      q.append(root)

      while q:
        ver = q.pop(0)
        for v in self[ver]:
          if not reached[v]:
            q.append(v)
            reached[v] = True
      if all(val for val in reached.values()):
        return True

    return False
