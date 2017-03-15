"""
"""

import csv
import os

DATAFILE = os.path.join(os.path.dirname(__file__), 'cards.csv')

def balance():
  """
  Show total cards balance for each currency from cards.csv
  """
  with open(DATAFILE, 'rb') as cardfile:
    cardfile.next()  # skip header
    bal = dict()
    for card, cur, value, date in csv.reader(cardfile):
      cur = cur.strip()
      value = float(value)
      if cur not in bal:
        bal[cur] = value
      else:
        bal[cur] += value
    for cur in sorted(bal.keys()):
      print("{0} {1}".format(cur, bal[cur]))

if __name__ == '__main__':
  balance()
