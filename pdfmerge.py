#!/Users/pbuur/anaconda3/bin/python

# simple function to merge pdf files
# argument can either be
# - a list of files
# - a wildcard
# - a directory containing pdf files

import glob, os
import sys
from PyPDF2 import PdfFileMerger as pdfmerge
import argparse

parser = argparse.ArgumentParser(description='simple PDF merger')
parser.add_argument('-i', dest='file_in', nargs='+', required=True, help='file names separated by comma / wildcard / directory')
parser.add_argument('-o', dest='file_out', nargs=1, required=True, help='output file name')
args = parser.parse_args()

# input argument logic:
# if narg == 1
#   -> dir: check if dir exists
#   -> wildcard: check if there are any matching files
# if narg > 1
#   -> list of files

# check for arguments
f_in = args.file_in
print(len(f_in))
print(f_in)
chars = '?*'
if (len(f_in) == 1):
  if (os.path.isdir(f_in[0])):
  # make filelist from dir content
    flist = glob.glob('./*.pdf')
    print(flist)
  elif any((c in chars) for c in f_in[0]):
  # make filelist from wildcard
    flist = glob.glob('./'+f_in[0])
else:
  flist = f_in[:]

# print(flist)

mergedpdf = pdfmerge()
idx = 0;
for i in flist:
  try:
    mergedpdf.append(i)
    print('appending '+i)
    idx += 1
  except:
    print('*** not appending '+i+' ***')
if idx>1:
  mergedpdf.write(args.file_out[0])
  print('writing '+args.file_out[0])
else:
  mergedpdf.close()
  print('not making merged pdf: less than 2 files to merge')
