import py7zlib

f7file = "pakk.7z"

with open(f7file, 'rb') as f:
     z = py7zlib.Archive7z(f)
     z.list()

"""#Vaja tõmmata
import libarchive
#https://dustinoprea.com/2014/04/17/writing-and-reading-7-zip-from-python/


for state in libarchive.pour('pakk.7z'):
    if state.pathname == 'dont/write/me':
        state.set_selected(False)
        continue
 
    # (The state evaluates to a filename.)
    print("Writing: %s" % (state))"""