#!/usr/bin/python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import subprocess

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them

def get_special_paths(dirname):
  """Returns a list of the absolute paths of the special files in the given directory."""
  special_paths = []
  filenames = os.listdir(dirname)
  for filename in filenames:
    if re.search(r'__\w+__', filename):
      special_paths.append(os.path.abspath(os.path.join(dirname, filename)))
  return special_paths

def copy_to(paths, todir):
  """Copies the files in the given list of paths to the specified directory."""
  if not os.path.exists(todir):
    os.makedirs(todir)
  for path in paths:
    shutil.copy(path, todir)

def zip_to(paths, tozip):
  """Zips the files in the given list of paths to the specified zip file."""
  cmd = ['zip', '-j', tozip] + paths
  subprocess.run(cmd)


def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print('usage: [--todir dir][--tozip zipfile] dir [dir ...]')
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print('error: must specify one or more dirs')
    sys.exit(1)

  # +++your code here+++
  # Call your functions
  # LAB(begin solution)

  # Gather all the special files
  paths = []
  for dirname in args:
    paths.extend(get_special_paths(dirname))

  if todir:
    copy_to(paths, todir)
  elif tozip:
    zip_to(paths, tozip)
  else:
    print('\n'.join(paths))
  # LAB(end solution)

if __name__ == '__main__':
  main()
