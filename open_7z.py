import subprocess
import re
from datetime import datetime

"""
Võtab antud käsu ja käivitab selle käsurealt
Väljastab kõik read, mida käsu täitmisel näidataks
"""
def run_process(command):    
    p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    while(True):
        retcode = p.poll() #returns None while subprocess is running
        line = p.stdout.readline().decode("utf8")
        yield line
        if(retcode is not None):
            break

"""
Võtab arhiivi nime ja tagastab kõikide seal olevate failide nimed
"""
def get_filenames(arch_loc):
    names=False
    name_list=[]
    command= loc_7z + " l " + arch_loc
    for line in run_process(command):
        if line.startswith("----"):
            names=not names
            continue
        if names:
            #Juhuks, kui failinimed pole õiges formaadis
            try:
                name_list.append(line.rsplit(" ", 1)[1].strip())
            except:
                pass
    return name_list

"""
Avab arhiivi ja võtab seal välja failid, mille nimed on antud
Argumentideks on arhiivi asukoht, failinimed, väljundkaust
"""
def unpack(arch_loc, filenames, output='*'):
    command = loc_7z+" e "+ arch_loc +" -aoa -o"+output+" "+" ".join(filenames)
    for i in run_process(command):
        print(i, end="")
    

#Vaja programmile anda, globaalne
loc_7z = r"C:\\Program Files\\7-Zip\\7z.exe"


start=datetime(2016, 11, 26, hour=12, minute=20, second=0)
end=datetime(2017, 9, 9, hour=16, minute=0, second=0)

arch_loc="C:\\Users\\Villem\\Desktop\\L-put-\\pakk.7z"

all_filenames=get_filenames(arch_loc)
filenames=[]
for name in all_filenames:
    #Juhuks, kui mõne faili nime on muudetud
    try:
        date=datetime.strptime(name.rsplit("_", 1)[0], '%Y-%m-%d_%H-%M-%S')
        if date>start and date<end:
            filenames.append(name)
    except:
        pass

unpack(arch_loc, filenames, output="C:\\Users\\Villem\\Desktop\\L-put-\\pakk1")