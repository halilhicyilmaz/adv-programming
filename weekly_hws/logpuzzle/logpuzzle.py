#!/usr/bin/python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib
import urllib.request

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""


def read_urls(filename):
  """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""
  # Extract the hostname from the filename
  underbar = filename.index('_')
  hostname = filename[underbar + 1:]

  # Read the log file
  with open(filename, 'r') as file:
    log_data = file.read()

  # Find all puzzle URLs using regular expressions
  puzzle_urls = re.findall(r'GET (\S+\.jpg)', log_data)
  # Remove duplicates and sort the URLs
  unique_urls = sorted(set(puzzle_urls))

  # Prepend the hostname to each URL
  complete_urls = [f'http://{hostname}{url}' for url in unique_urls]

  return complete_urls

def download_images(img_urls, dest_dir):
  """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """
  # +++your code here+++
  # Create the destination directory if it doesn't exist
  if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)
  # Download and save each image

  index = open(os.path.join(dest_dir, 'index.html'), 'w')
  
  for i, url in enumerate(img_urls):
    local_name = 'img%d' % i
    print('Retrieving...', url)
    urllib.request.urlretrieve(url, os.path.join(dest_dir, local_name))
    index.write('<img src="%s">' % (local_name,))

def main():
  args = sys.argv[1:]

  if not args:
    print('usage: [--todir dir] logfile ')
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  img_urls = read_urls(args[0])

  if todir:
    download_images(img_urls, todir)
  else:
    print('\n'.join(img_urls))

if __name__ == '__main__':
  main()
