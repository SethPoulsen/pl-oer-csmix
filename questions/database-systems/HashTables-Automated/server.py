import random
import math
import json
import re

class HashTable:
    def __init__(self, threshold):
        self.threshold = threshold
        self.size = 0
        self.rows = 0
        self.nextExpansion = 2
        self.bits = 1
        self.contents = {}
        self.addRow()
    # 0, 1, 10, 11, 100, 101, 110, 111, 1000
    # 2+, 4+, 8+
    def addHashcode(self, d, hashcode):
      key = hashcode[-self.bits:]
      if key in d.keys():
        d[key].append(hashcode)
      else:
        d['0'+key[1:]].append(hashcode)

    def addRow(self):
      if (self.nextExpansion == self.rows):
        self.nextExpansion *= 2
        self.bits += 1
      self.rows += 1
      temp = {}
      for x in range(self.rows):
        temp[format(x, '0'+str(self.bits)+'b')] = []
      for l in self.contents.values():
        for value in l:
          self.addHashcode(temp, value)
      self.contents = temp

    def add(self, hashcode):
      self.size += 1
      if (self.size / self.rows >= self.threshold):
        self.addRow()
      self.addHashcode(self.contents, hashcode)
      return str(self.contents)

def generate(data):
    # Get a list of a few random values (7?). Insert the first 5, then ask for the results of the sixth and seventh.
    t = random.randint(140,200) / 100
    h = HashTable(t)
    inserted = []
    stages = []
    for i in range(7):
      ins = format(random.randint(0,31), '06b')
      while (ins in inserted):
        ins = format(random.randint(0,31), '06b')
      inserted.append(ins)
      stages.append(h.add(ins))
    # We want the result in the form of a dictionary.
    data['params']['threshold'] = str(t)
    data['params']['initial_table'] = str(stages[4])
    data['params']['insertion_I'] = str(inserted[5])
    data['params']['insertion_II'] = str(inserted[6])
    data['correct_answers']['question_I'] = str(stages[5])
    data['correct_answers']['question_II'] = str(stages[6])

def sort_table(t):
    # Take a string table, sort every row, convert to text.
    t = json.loads(t)
    for k in t:
        t[k].sort()
    return json.dumps(t)
    

def grade(data):
    for qn in ["question_I", "question_II"]:
        # Sort every bucket to ignore the order in which the student provides them.
        s = data["submitted_answers"][qn]
        c = data["correct_answers"][qn]
        # Remove quotes
        s = re.sub(r'["\']', '', s)
        c = re.sub(r'["\']', '', c)
        # Add quotes around every set of numbers.
        s = re.sub(r'(\d+)', '"\\1"', s)
        c = re.sub(r'(\d+)', '"\\1"', c)
        try:
            table_sub = sort_table(s)
            table_cor = sort_table(c)
        except (Exception):
            table_sub = "1"
            table_cor = "0"
        #
        s = "".join(table_sub.split())
        c = "".join(table_cor.split())
        #
        if (s == c):
            data["partial_scores"][qn]["score"] = data["score"] = 1
        else:
            data["partial_scores"][qn]["score"] = data["score"] = 0
    