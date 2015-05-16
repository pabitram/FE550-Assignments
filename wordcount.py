#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/


import sys
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec


def word_count_dict(filename):
  """Returns a word/count dict for this filename."""
  # Utility used by count() and Topcount().
  word_count = {}  # Map each word to its count
  input_file = open(filename, 'r')
  igonorewords = ["the", "with", "they", "this", "here", "have", "chicken", "its"]
  for line in input_file:
    words = line.split()
    for word in words:
	  if len(word) > 3:
		  if  word not in igonorewords:
			word = word.lower().replace('\'', "")
			# Special case if we're seeing this word for the first time.
			if not word in word_count:
				word_count[word] = 1
			else:
				word_count[word] = word_count[word] + 1
  input_file.close()  # Not strictly required, but good form.
  return word_count


def get_count(word_count_tuple):
  """Returns the count from a dict word/count tuple  -- used for custom sort."""
  return word_count_tuple[1]


def print_top(filename):
  """Prints the top count listing for the given file."""
  word_count = word_count_dict(filename)

  # Each item is a (word, count) tuple.
  # Sort them so the big counts are first using key=get_count() to extract count.
  items = sorted(word_count.items(), key=get_count, reverse=True)

  # Print the first 10
  name = []
  value = []
  for item in items[:10]:
	print item[0], item[1]
	name.append(item[0])
	value.append(item[1])
  
  plot_graph(name, value)

def plot_graph(labels, fracs):
	plt.pie(fracs, labels=labels,
        autopct='%1.1f%%', shadow=True, startangle=90)
	# Set aspect ratio to be equal so that pie is drawn as a circle.
	title_font = {'fontname':'Arial', 'size':'10', 'color':'black', 'weight':'normal',
              'verticalalignment':'bottom'}
	plt.axis('equal')
	plt.title('YELP most frequently words in tips', **title_font)
	plt.show()


def main():
  if len(sys.argv) != 2:
    print 'usage: ./wordcount.py  file'
    sys.exit(1)

  filename = sys.argv[1]
  print_top(filename)
	

if __name__ == '__main__':
  main()
