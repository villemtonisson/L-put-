import json
import os
from pathlib import Path

#text_widget_id
#text_widget_class
#"ShellText"
#"CodeViewText"

"""
Võtab faili täistee ja eraldab sealt erinevate id'dega text widgetid.
Kõik muud paneb kaasa kõigile
"""
def separate_by_ids(file_loc):
    #Loeb sisse kogu info failist
    with open(file_loc, 'r', encoding="UTF8") as f:
        data=json.loads(f.read())
      
    # Filename_ids : id'd, mis sellele failile kuuluvad 
    filename_ids={}
    for d in data:
        if "filename" in d:
            fname=d['filename']
            if fname not in filename_ids:
                filename_ids[fname]=[]
            filename_ids[fname].append(d.get("text_widget_id", -1))
    
    # Hoiab täistee-failinimi paare
    py_files={}
    for fname in filename_ids:
        py_file= os.path.splitext(os.path.split(fname)[1])[0]
        # Juhuks, kui mitu sama nimega faili avati on
        # Paneb arvu lõppu, kui vaja
        i=1
        while True:
            if py_file not in py_files.values():
                py_files[fname]=py_file
                break
            if i>1:
                py_file=py_file[:-2]
            py_file+="_"+str(i)
            i+=1
    
    # Output - mis kirjed kuhu faili
    output={}   
    for fname in filename_ids:
        output[fname]=[]

    # Jätame meelde, millised id'd on seotud failidega
    meaningful_ids=set([x for y in filename_ids.values() for x in y])
    
    #Kui on tegemist codeviewtextiga, paneb selle vaid kindlasse faili
    # Muidu paneb kõikidesse failidesse
    prev_id=-2
    for d in data:
        if d.get("text_widget_class")=="CodeViewText":
            current_id = d.get("text_widget_id", -1)
            if current_id!=prev_id and current_id in meaningful_ids:
                prev_id = d.get("text_widget_id")
            for fname in output:
                if prev_id in filename_ids[fname]:
                    output[fname].append(d)
        else:
            for fname in output:
                output[fname].append(d)
      
   
    # Poolitada failitee, et saaks sinna vahele liita  
    name, ext = os.path.splitext(file_loc)
    
    for i in output:
        # Poolitame leitud failinime
        p=Path(name+"_"+py_files[i]+ext)
        with open(p, 'w', encoding="UTF8") as f:
            json.dump(output[i], f, indent=4)

#separate_by_ids("C:/Loputoo/debug/samanimi2.txt")