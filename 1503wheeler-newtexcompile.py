# This is a script to compile a latex document and clean up afterwards
# Originally written by Nick Wheeler
import os

################################################################################
# Clean out the repo, and recompile the tex
################################################################################

# Options

def clean_aux():
    suffixlist = ['aux','out','toc','lot','lof','log','bbl','blg']

    files = []
    for (dirpath, dirnames, filenames) in os.walk('.'):
      files.extend(os.path.join(dirpath, filename) for filename in filenames)
      for subdir in dirnames:
        for (subdirpath, subdirnames, subfilenames) in os.walk(subdir):
          files.extend(os.path.join(subdirpath, subfilename) for subfilename in subfilenames)
      break

    print('\nPrinting all files...')
    print files

    found = []
    for f in files:
      for s in suffixlist:
        if s in f:
          found.append(f)

    print '\nPrinting matches for removal...'
    print found

    for f in found:
      if os.path.isfile('.' + os.sep + f):
        print f
        os.remove('.' + os.sep + f)


# What is the file name?
# texfile = "DL_Zhang2018"
texfile = "Introduction_to_Deep_Learning"

# Also run bibtex to compile references?
bibtex=False

# Call up the resulting pdf with mupdf when finished?
view=False

################################################################################
# Code
################################################################################
clean_aux()
# os.system("python 1501wheeler-pytexrepoclean.py")
os.system("pdflatex " + texfile + ".tex")
# os.system("pdflatex " + texfile + ".tex")
if bibtex:
  os.system("bibtex " + texfile + ".aux")
  os.system("pdflatex " + texfile + ".tex")
  os.system("pdflatex " + texfile + ".tex")
clean_aux()
# os.system("python 1501wheeler-pytexrepoclean.py")
if view:
  os.system("mupdf " + texfile + ".pdf")
