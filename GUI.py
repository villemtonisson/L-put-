import tkinter as tk
import tkinter.ttk as ttk
from tkinter.filedialog import askopenfilename, askdirectory
from pathlib import Path
from datepicker import Datepicker
from unpacker import unpack_between
from datetime import datetime


#TODO teha settings fail
loc_7z = r"C:\\Program Files\\7-Zip\\7z.exe"


#filename = askopenfilename()
#print(filename)
#filedialog.askdirectory()
#askopenfilename(title="Select file", filetypes=(("all files", "*.*"),("RAR files", "*.rar"), ("ZIP files", "*.zip"),("7z files", "*.7z"),("TAR files", "*.tar")))

def pick_file():
    global chosen_file
    filename=Path(askopenfilename(title="Select file", filetypes=(("all files", "*.*"),
                ("RAR files", "*.rar"), ("ZIP files", "*.zip"),("7z files", "*.7z"),("TAR files", "*.tar"))))
    print(Path(filename))
    chosen_file_var.set(filename)
    return


#start=datetime(2016, 11, 26, hour=12, minute=20)
#end=datetime(2017, 9, 9, hour=16, minute=0)
def unpack():
    global start_date_picker, start_hour_picker, start_minute_picker
    global end_date_picker, end_hour_picker, end_minute_picker, chosen_file_field
    
    start_date_str=start_date_picker.current_text+"-"+start_hour_picker.get()+"-"+start_minute_picker.get()
    start_date=datetime.strptime(start_date_str, "%Y-%m-%d-%H-%M")
    
    end_date_str=end_date_picker.current_text+"-"+end_hour_picker.get()+"-"+end_minute_picker.get()
    end_date=datetime.strptime(end_date_str, "%Y-%m-%d-%H-%M")
    
    print(start_date, end_date)
    
    unpack_between(chosen_file_field.get(), start_date, end_date)
    
    return

window = tk.Tk()
window.title("Blender Rendering Farm")
window.geometry('800x600')
window.configure(background='white')
window.resizable(0, 0)

# Frames for the app
titleFrame = tk.Frame(window, width=800, height=100, background='blue')
middleFrame = tk.Frame(window, width=800, height=300, background='cyan')
leftFrame = tk.Frame(middleFrame, width=400, height=300, background='red')
rightFrame = tk.Frame(middleFrame, width=400, height=300, background='green')
bottomFrame= tk.Frame(window, width=800, height=200, background='yellow')

#No resizing frames
titleFrame.pack_propagate(0)
middleFrame.pack_propagate(0)
leftFrame.pack_propagate(0)
rightFrame.pack_propagate(0)
bottomFrame.pack_propagate(0)

# Frame placement
titleFrame.pack(anchor='n', side=tk.TOP)
middleFrame.pack(anchor='n', side=tk.TOP)
leftFrame.pack(anchor="n", side=tk.LEFT)
rightFrame.pack(anchor="n", side=tk.RIGHT)
bottomFrame.pack(anchor="s", side=tk.BOTTOM)


#Title
title_label = tk.Label(titleFrame, text="Log File Editor", bg="white", font=("Arial Bold", 30), pady=15)
title_label.pack()


#Elements on the left
start_label = tk.Label(leftFrame, text="Start", bg="white", font=("Arial Bold", 14))
start_label.pack(anchor='c')

start_date_label = tk.Label(leftFrame, text="Date", bg="white", font=("Arial", 12))
start_date_label.pack(anchor='c')

start_date_picker = Datepicker(leftFrame)
start_date_picker.pack(anchor="c")

#Hour
start_hour_label = tk.Label(leftFrame, text="Hour", bg="white", font=("Arial", 12))
start_hour_label.pack(anchor='c')

start_hour_picker = ttk.Combobox(leftFrame)
start_hour_picker['values']= list(range(24))
start_hour_picker.current(0) #set the selected item
start_hour_picker.pack(anchor='c')

#Minute
start_minute_label = tk.Label(leftFrame, text="Minute", bg="white", font=("Arial", 12))
start_minute_label.pack(anchor='c')

start_minute_picker = ttk.Combobox(leftFrame)
start_minute_picker['values']= list(range(60))
start_minute_picker.current(0) #set the selected item
start_minute_picker.pack(anchor='c')


#Elements on the right
end_label = tk.Label(rightFrame, text="End", bg="white", font=("Arial Bold", 12))
end_label.pack(anchor='c')

end_date_label = tk.Label(rightFrame, text="Date", bg="white", font=("Arial", 12))
end_date_label.pack(anchor='c')

end_date_picker = Datepicker(rightFrame)
end_date_picker.pack(anchor="c")

#Hour
end_hour_label = tk.Label(rightFrame, text="Hour", bg="white", font=("Arial", 12))
end_hour_label.pack(anchor='c')

end_hour_picker = ttk.Combobox(rightFrame)
end_hour_picker['values']= list(range(24))
end_hour_picker.current(0) #set the selected item
end_hour_picker.pack(anchor='c')

#Minute
end_minute_label = tk.Label(rightFrame, text="Minute", bg="white", font=("Arial", 12))
end_minute_label.pack(anchor='c')

end_minute_picker = ttk.Combobox(rightFrame)
end_minute_picker['values']= list(range(60))
end_minute_picker.current(0) #set the selected item
end_minute_picker.pack(anchor='c')

# File Picker
file_pick_button = tk.Button(bottomFrame, text="Pick File", command=pick_file)
file_pick_button.pack(anchor='c')

chosen_file_var = tk.StringVar()
chosen_file_field = tk.Entry(bottomFrame, width=150, textvariable=chosen_file_var, state='disabled')
chosen_file_field.pack(anchor='c')


unpack_button = tk.Button(bottomFrame, text="Unpack", command=unpack)
unpack_button.pack(anchor='c')

window.mainloop()