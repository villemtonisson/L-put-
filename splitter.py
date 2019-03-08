import json
from pathlib import Path

dir=Path("test")
p=Path("test").joinpath("logi.txt")
with open(p, 'r', encoding="UTF8") as f:
    data=json.loads(f.read())
    

#text_widget_id
#text_widget_class
#"ShellText"
#"CodeViewText"
output={}
prev_id=-2
for d in data:
    if d.get("text_widget_class")=="CodeViewText":
        if d.get("text_widget_id", -1)!=prev_id:
            prev_id = d.get("text_widget_id")
            
    if output.get(prev_id)==None:
        output[prev_id]=[]
    output[prev_id].append(d)        

for i in output:
    p=dir.joinpath(str(i)+".txt")
    with open(p, 'w', encoding="UTF8") as f:
        json.dump(output[i], f)