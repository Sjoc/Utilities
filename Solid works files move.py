import os
import sys
import shutil
import string

File_Types = ['.sldprt', '.sldasm', '.stp', '.step', '.slddrw']

Files1 = []

Count = 0

Count2 = 0

Dir1 = raw_input('Search Folder:')
Dir2 = raw_input('Save Folder:')

Files0 = os.listdir(Dir1)

for n in Files0:
    n2=os.path.splitext(n)
    for ext in n2:
        ext = string.lower(ext)
        for fil in File_Types:
            if ext == fil:
                Files1.append(n)
                Count2 = Count2 + 1
print Files1

for n3 in Files1:
    Mover = os.path.join(Dir1, n3)
    shutil.move(Mover, Dir2)
    Count = Count + 1

print 'Total Files Found:', Count2
print 'Total Files Moved:', Count
