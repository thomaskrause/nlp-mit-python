import sys
from os.path import exists

if len(sys.argv) < 2:
    print("No file given")
else:
    if exists(sys.argv[1]):
        with open(sys.argv[1], 'r') as f:
            print(f.read())
    else:
        print("Datei existiert nicht!")
