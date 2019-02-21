import tkinter as tk
import tkinter.ttk as ttk

from tkinter.filedialog import askopenfilename, askdirectory
from datepicker_edit import Datepicker



#TODO teha 
loc_7z = r"C:\\Program Files\\7-Zip\\7z.exe"


window = tk.Tk()
window.title("Blender Rendering Farm")
window.geometry('800x800')
window.configure(background='white')
window.resizable(0, 0)

# Frames for the app
titleFrame = tk.Frame(window, width=800, height=100, background='blue')
leftFrame = tk.Frame(window, width=400, height=300, background='red')
rightFrame = tk.Frame(window, width=400, height=300, background='green')
bottomFrame= tk.Frame(window, width=800, height=200, background='yellow')

#No resizing frames
titleFrame.pack_propagate(0)
leftFrame.pack_propagate(0)
rightFrame.pack_propagate(0)
bottomFrame.pack_propagate(0)

# Frame placement

titleFrame.pack(anchor='n', side=tk.TOP)

leftFrame.pack(anchor="n", side=tk.LEFT)
rightFrame.pack(anchor="n", side=tk.RIGHT)

bottomFrame.pack(anchor="n", side=tk.TOP)


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

#filename = askopenfilename()
#print(filename)
#filedialog.askdirectory()
#
#askopenfilename(title="Select file", filetypes=(("all files", "*.*"),("RAR files", "*.rar"), ("ZIP files", "*.zip"),("7z files", "*.7z"),("TAR files", "*.tar")))

#file_pick_button = tk.Button(bottomFrame, text="Pick File")
#file_pick_button.pack(fill=tk.BOTH, expand=1)

window.mainloop()