import tkinter as tk
import tkinter.ttk as ttk
import json
from tkinter.filedialog import askopenfilename, askopenfilenames
from pathlib import Path
from datepicker import Datepicker
from splitter import separate_by_ids
from unpacker import unpack_between_infile, unpack_all
from datetime import datetime

#filename = askopenfilename()
#print(filename)
#filedialog.askdirectory()
#askopenfilename(title="Select file", filetypes=(("all files", "*.*"),("RAR files", "*.rar"), ("ZIP files", "*.zip"),("7z files", "*.7z"),("TAR files", "*.tar")))

#start=datetime(2016, 11, 26, hour=12, minute=20)
#end=datetime(2017, 9, 9, hour=16, minute=0)

"""
Olenevalt kasutaja sisestusest, valib kas mitu või ühe faili
"""
def pick_file():
    global chosen_file, chosen_mode_var
    
    mode=chosen_mode_var.get()
    #1 file
    if mode=="1log":
        filename=Path(askopenfilename(title="Select file", filetypes=(("all files", "*.*"), ("text files", "*.txt"))))
        print(filename)
        chosen_file_var.set(filename)
    #1 archive
    if mode=="1arch":
        filename=Path(askopenfilename(title="Select file", filetypes=(("all files", "*.*"),
                ("RAR files", "*.rar"), ("ZIP files", "*.zip"),("7z files", "*.7z"),("TAR files", "*.tar"))))
        print(filename)
        chosen_file_var.set(filename)
    if mode=="2log":
        filenames = askopenfilenames(
                filetypes = [('Text', '.txt'), ('all files', '.*'),],
                title = "Select .txt files",
                multiple = True,
                )
        chosen_file_var.set(json.dumps(list(filenames)))

    if mode=="2arch":
        filenames = askopenfilenames(
                defaultextension = '*.*',
                filetypes = [("all files", "*.*"), ("RAR files", "*.rar"),
                             ("ZIP files", "*.zip"),("7z files", "*.7z"),("TAR files", "*.tar"),],
                title = "Select archive files",
                multiple = True,
                )
        chosen_file_var.set(json.dumps(list(filenames)))
    
    
    return

"""
Olenevalt kasutaja valikust, kas pakib lahti või ainult eraldab ülesannete kaupa
"""
def unpack():
    global start_date_picker, start_hour_picker, start_minute_picker
    global end_date_picker, end_hour_picker, end_minute_picker, chosen_file_field
    global separate_exercises_var, use_dates_var, chosen_mode_var
    
    separate=(separate_exercises_var.get()==1)
    use_dates=(use_dates_var.get()==1)
    mode=chosen_mode_var.get()
    #Siia tulevad failinimed, mis lahti pakiti
    filenames=[]
    
    if use_dates:
        start_date_str=start_date_picker.current_text+"-"+start_hour_picker.get()+"-"+start_minute_picker.get()
        start_date=datetime.strptime(start_date_str, "%Y-%m-%d-%H-%M")
        
        end_date_str=end_date_picker.current_text+"-"+end_hour_picker.get()+"-"+end_minute_picker.get()
        end_date=datetime.strptime(end_date_str, "%Y-%m-%d-%H-%M")
        
    #1 file
    if mode=="1log":
        filenames.append(chosen_file_field.get())
    #1 archive
    elif mode=="1arch":
        if use_dates:
            filenames=unpack_between_infile(chosen_file_field.get(), start_date, end_date)
        else:
            filenames=unpack_all(chosen_file_field.get())
        
    elif mode=="2log":
        if use_dates:
            pass
        else:
            filenames=json.loads(chosen_file_field.get())
    elif mode=="2arch":
        if use_dates:
            for f in json.loads(chosen_file_field.get()):
                filenames.extend(unpack_between_infile(f, start_date, end_date))
        else:
            for f in json.loads(chosen_file_field.get()):
                filenames.extend(unpack_all(f))
    
    if separate:
        for f in filenames:
            separate_by_ids(f)
    
    return

background='ghost white'

window = tk.Tk()
window.title("Log File Editor")
window.geometry('800x600')
window.configure(background=background)
window.resizable(0, 0)

# Frames for the app
titleFrame = tk.Frame(window, width=800, height=100, background=background, padx=25)
middleFrame = tk.Frame(window, width=800, height=250, background=background, padx=25)
leftFrame = tk.Frame(middleFrame, width=400, height=250, background=background)
rightFrame = tk.Frame(middleFrame, width=400, height=250, background=background)
bottomFrame= tk.Frame(window, width=800, height=250, background=background, padx=25)
leftBottomFrame= tk.Frame(bottomFrame, width=400, height=250, background=background)
rightBottomFrame= tk.Frame(bottomFrame, width=400, height=250, background=background)


#No resizing frames
titleFrame.pack_propagate(0)
middleFrame.pack_propagate(0)
leftFrame.pack_propagate(0)
rightFrame.pack_propagate(0)
bottomFrame.pack_propagate(0)
leftBottomFrame.pack_propagate(0)
rightBottomFrame.pack_propagate(0)

# Frame placement
titleFrame.pack(anchor='n', side=tk.TOP)
middleFrame.pack(anchor='n', side=tk.TOP)
leftFrame.pack(anchor="n", side=tk.LEFT)
rightFrame.pack(anchor="n", side=tk.RIGHT)
bottomFrame.pack(anchor="s", side=tk.TOP)
leftBottomFrame.pack(anchor="n", side=tk.LEFT)
rightBottomFrame.pack(anchor="n", side=tk.RIGHT)

## TOP
#Title
title_label = tk.Label(titleFrame, text="Log File Editor", bg=background, font=("Arial Bold", 30), pady=15)
title_label.pack()

### MIDDLE
## LEFT
#Elements on the left
start_label = tk.Label(leftFrame, text="Start", bg=background, font=("Arial Bold", 14))
start_label.pack(anchor='c')

start_date_label = tk.Label(leftFrame, text="Date", bg=background, font=("Arial", 12))
start_date_label.pack(anchor='c')

start_date_picker = Datepicker(leftFrame)
start_date_picker.pack(anchor="c")

#Hour
start_hour_label = tk.Label(leftFrame, text="Hour", bg=background, font=("Arial", 12))
start_hour_label.pack(anchor='c')

start_hour_picker = ttk.Combobox(leftFrame)
start_hour_picker['values']= list(range(24))
start_hour_picker.current(0) #set the selected item
start_hour_picker.pack(anchor='c')

#Minute
start_minute_label = tk.Label(leftFrame, text="Minute", bg=background, font=("Arial", 12))
start_minute_label.pack(anchor='c')

start_minute_picker = ttk.Combobox(leftFrame)
start_minute_picker['values']= list(range(60))
start_minute_picker.current(0) #set the selected item
start_minute_picker.pack(anchor='c')

## RIGHT
#Elements on the right
end_label = tk.Label(rightFrame, text="End", bg=background, font=("Arial Bold", 12))
end_label.pack(anchor='c')

end_date_label = tk.Label(rightFrame, text="Date", bg=background, font=("Arial", 12))
end_date_label.pack(anchor='c')

end_date_picker = Datepicker(rightFrame)
end_date_picker.pack(anchor="c")

#Hour
end_hour_label = tk.Label(rightFrame, text="Hour", bg=background, font=("Arial", 12))
end_hour_label.pack(anchor='c')

end_hour_picker = ttk.Combobox(rightFrame)
end_hour_picker['values']= list(range(24))
end_hour_picker.current(0) #set the selected item
end_hour_picker.pack(anchor='c')

#Minute
end_minute_label = tk.Label(rightFrame, text="Minute", bg=background, font=("Arial", 12))
end_minute_label.pack(anchor='c')

end_minute_picker = ttk.Combobox(rightFrame)
end_minute_picker['values']= list(range(60))
end_minute_picker.current(0) #set the selected item
end_minute_picker.pack(anchor='c')


### BOTTOM
## RIGHTBOTTOM
# File Picker
file_pick_button = tk.Button(rightBottomFrame, text="Pick File(s)", command=pick_file)
file_pick_button.pack(anchor='c')

chosen_file_var = tk.StringVar()
chosen_file_field = tk.Entry(rightBottomFrame, width=150, textvariable=chosen_file_var, state='disabled')
chosen_file_field.pack(anchor='c')

unpack_button = tk.Button(rightBottomFrame, text="Unpack", command=unpack)
unpack_button.pack(anchor='c')

## LEFTBOTTOM
# Select mode label
select_mode_label = tk.Label(leftBottomFrame, text="Select mode", bg=background, font=("Arial", 11))
select_mode_label.pack(anchor='c')

# Creating radiobuttons for selecting mode
MODES = [
        ("One logfile", "1log"),
        ("One archive", "1arch"),
        ("Multiple logfiles", "2log"),
        ("Multiple archives", "2arch"),
    ]

chosen_mode_var = tk.StringVar()
chosen_mode_var.set("1arch") # initialize

for text, mode in MODES:
    b = tk.Radiobutton(leftBottomFrame, text=text,
                    variable=chosen_mode_var, value=mode)
    b.pack(anchor='c')

# Checkbutton for using date system
use_dates_var = tk.IntVar()
use_dates_button = tk.Checkbutton(leftBottomFrame, text="Unpack using dates", variable=use_dates_var)
use_dates_button.pack(anchor='c', pady="8")

# Checkbutton for separating exercises from logs 
separate_exercises_var = tk.IntVar()
separate_exercises_button = tk.Checkbutton(leftBottomFrame, text="Separate by .py files", variable=separate_exercises_var)
separate_exercises_button.pack(anchor='c')

## Start program
window.mainloop()