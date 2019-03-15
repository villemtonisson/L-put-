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
    with open(file_loc, 'r', encoding="UTF8") as f:
        data=json.loads(f.read())
        
    output={}
    text_widget_ids=set()
    for d in data:
        text_widget_ids.add(d.get("text_widget_id", -1))
        
    text_widget_ids.remove(-1)

    for id in text_widget_ids:
        output[id]=[]

    prev_id=-2
    for d in data:
        if d.get("text_widget_class")=="CodeViewText":
            if d.get("text_widget_id", -1)!=prev_id:
                prev_id = d.get("text_widget_id")
            output[prev_id].append(d)
        else:
            for id in output:
                output[id].append(d)
                
    name, ext = os.path.splitext(file_loc)
    for i in output:
        p=Path(name+"_"+str(i)+ext)
        with open(p, 'w', encoding="UTF8") as f:
            json.dump(output[i], f, indent=4)

#separate_by_ids("C:/Loputoo/L-put-/test/logi.txt")