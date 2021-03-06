import subprocess
import os
import json
from datetime import datetime
from pathlib import Path


with open("settings.json", encoding="utf8") as f:    
    try:
        data=json.loads(f.read())
        loc_7z=Path(data['loc_7z'])
        encoding=data['encoding']
    except:
        loc_7z = Path("C:\\Program Files\\7-Zip\\7z.exe")
        encoding="utf8"


"""
Võtab antud käsu ja käivitab selle käsurealt
Väljastab kõik read, mida käsu täitmisel näidataks
"""
def run_process(command):    
    print(command)
    p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    while(True):
        retcode = p.poll() #returns None while subprocess is running
        #https://superuser.com/questions/1170656/windows-10-terminal-encoding
        line = p.stdout.readline().decode(encoding)
        yield line
        if(retcode is not None):
            break

"""
Võtab arhiivi nime ja tagastab kõikide seal olevate failide nimed
"""
def get_filenames(arch_loc):
    names=False
    name_list=[]
    prev_line=""
    startindex=0
    command = stringify(str(loc_7z)) + " l " + stringify(arch_loc)
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
def unpack(arch_loc, filenames, output='*'):
    filenames_str=[stringify(filename) for filename in filenames]
    command = stringify(str(loc_7z))+" e "+ stringify(arch_loc) + " -aoa -o"+ stringify(output)+ " ".join(filenames_str)
    for i in run_process(command):
        print(i, end="")
 
"""
Avab arhiivi ja võtab sealt välja kõik failid
Tagastab failinimed
"""
def unpack_all(arch_loc, output='*'):
    all_filenames=get_filenames(arch_loc)
    if output=='*':
        output, ext = os.path.splitext(arch_loc)
    
    unpack(arch_loc, [], output=output)
        
    filenames=[str(Path(output).joinpath(x)) for x in all_filenames]
    return filenames
    
"""
Avab arhiivi ja võtab sealt välja kõik failid
Seejärel vaatab failid läbi ja eemaldab need, mis ei kuulu antud ajavahemikku

Tulemuskaust peab olema tühi selle töötamiseks
Tagastab allesjäänud failide nimed
"""  
def unpack_between_infile(arch_loc, start, end, output='*'):
    all_filenames=get_filenames(arch_loc)
    if output=='*':
        output, ext = os.path.splitext(arch_loc)
    unpack_all(arch_loc, output=output)
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
Võtab failinime ja paneb sinna ümber jutumärgid.
Vajalik selleks, et failinimes saaks "-" sees olla
"""
def stringify(fname):
    return '"'+fname+'"'
    
