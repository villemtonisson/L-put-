import subprocess
from datetime import datetime
import os
from pathlib import Path
import json


if __name__ == "__main__":
    loc_7z = Path("C:\\Program Files\\7-Zip\\7z.exe")
    with open("settings.json", encoding="utf8") as f:    
        try:
            loc_7z=Path(json.loads(f.read())['loc_7z'])
        except:
            loc_7z = Path("C:\\Program Files\\7-Zip\\7z.exe")
            
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
def get_filenames(loc_7z, arch_loc):
    names=False
    name_list=[]
    prev_line=""
    startindex=0
    command = str(loc_7z) + " l " + arch_loc
    for line in run_process(command):
        if line.startswith("----"):
            names=not names
            if names:
                startindex=prev_line.index("Name")
            continue
        if names:
            #Juhuks, kui failinimed pole õiges formaadis
            try:
                name_list.append(line[startindex:].strip())
            except:
                pass
        prev_line=line
    return name_list

"""
Avab arhiivi ja võtab seal välja failid, mille nimed on antud
Argumentideks on arhiivi asukoht, failinimed, väljundkaust
"""
def unpack(loc_7z, arch_loc, filenames, output='*'):
    command = str(loc_7z)+" e "+ arch_loc +" -aoa -o"+output+" "+" ".join(filenames)
    for i in run_process(command):
        print(i, end="")
 
"""
Avab arhiivi ja võtab sealt välja kõik failid
Tagastab failinimed
"""
def unpack_all(loc_7z, arch_loc, output='*'):
    all_filenames=get_filenames(loc_7z, arch_loc)
    if output=='*':
        output, ext = os.path.splitext(arch_loc)
    
    unpack(loc_7z, arch_loc, [], output=output)
        
    filenames=[str(Path(output).joinpath(x)) for x in all_filenames]
    return filenames
    
"""
Avab arhiivi ja võtab sealt välja kõik failid
Seejärel vaatab failid läbi ja eemaldab need, mis ei kuulu antud ajavahemikku

Tulemuskaust peab olema tühi selle töötamiseks
Tagastab allesjäänud failide nimed
"""  
def unpack_between_infile(loc_7z, arch_loc, start, end, output='*'):
    all_filenames=get_filenames(loc_7z, arch_loc)
    if output=='*':
        output, ext = os.path.splitext(arch_loc)
    unpack_all(loc_7z, arch_loc, output=output)
    for name in all_filenames[:]:
        to_remove=True
        p=Path(output).joinpath(name)
        with open(p, 'r', encoding="UTF8") as f:
            try:
                data=json.loads(f.read())
                date=datetime.strptime(data[0]['time'], '%Y-%m-%dT%H:%M:%S.%f')
                if date>start and date<end:
                    to_remove=False
            except:
                to_remove=True
        if to_remove:
            os.remove(p)
            all_filenames.remove(name)
    filenames=[str(Path(output).joinpath(x)) for x in all_filenames]
    return filenames

"""
Avab arhiivi ja võtab sealt välja failid, mille nimi on õiges ajavahemikus
Kui mõne logifaili nime on muudetud, võtab ka selle välja

def unpack_between_filenames(loc_7z, arch_loc, start, end, output='*'):
    all_filenames=get_filenames(loc_7z, arch_loc)
    filenames=[]
    for name in all_filenames:
        #Juhuks, kui mõne faili nime on muudetud
        try:
            date=datetime.strptime(name.rsplit("_", 1)[0], '%Y-%m-%d_%H-%M-%S')
            if date>start and date<end:
                filenames.append(name)
        except:
            filenames.append(name)
            #pass , juhuks, kui ei taha muudetud nimega
    unpack(loc_7z, arch_loc, filenames, output=output)
    return filenames
"""
#start=datetime(2016, 11, 26, hour=12, minute=20)
#end=datetime(2017, 9, 9, hour=16, minute=0)

#unpack_between_infile("C:/Loputoo/L-put-/pakk.7z", start, end, output='C:/Loputoo/L-put-/pakk2')

#unpack(loc_7z, arch_loc, filenames, output="C:\\Users\\Villem\\Desktop\\L-put-\\pakk1")
#print(get_filenames("C:/Loputoo/L-put-/pakk.7z"))    