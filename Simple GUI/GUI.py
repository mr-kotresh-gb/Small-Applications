_author_ = "Kotresh G B"

import os
try:
    import tkinter
except ImportError: #python 2
    import Tkinter as tkinter

mainwindow = tkinter.Tk()

mainwindow.title("Grid Demo")
mainwindow.geometry('640x480-8-200')
mainwindow['padx'] = 8

lable = tkinter.Label(mainwindow, text="TKinter Grid Demo")
lable.grid(row=0, column=0, columnspan=3)

mainwindow.columnconfigure(0, weight=100)
mainwindow.columnconfigure(1, weight=1)
mainwindow.columnconfigure(2, weight=1000)
mainwindow.columnconfigure(3, weight=600)
mainwindow.columnconfigure(4, weight=1000)
mainwindow.rowconfigure(0, weight=1)
mainwindow.rowconfigure(1, weight=10)
mainwindow.rowconfigure(2, weight=1)
mainwindow.rowconfigure(3, weight=3)
mainwindow.rowconfigure(4, weight=3)

file_list = tkinter.Listbox(mainwindow)
file_list.grid(row=1, column=0, sticky='nsew', rowspan=2)
file_list.config(border=2.5, relief='sunken')
for zone in os.listdir('C:\Windows\System32'): # You can use any file locations u want
    file_list.insert(tkinter.END, zone)

list_scroll = tkinter.Scrollbar(mainwindow, orient=tkinter.VERTICAL, command=file_list.yview)
list_scroll.grid(row=1, column=1, sticky='nsw', rowspan=2)
file_list['yscrollcommand'] = list_scroll.set

# Frame for the radio buttons
option_frame = tkinter.LabelFrame(mainwindow, text='File Details')
option_frame.grid(row=1, column=2, sticky='ne')

rb_value = tkinter.IntVar()
rb_value.set(1)

# Radio Buttons
radio1 = tkinter.Radiobutton(option_frame, text="File name", value=1, variabl=rb_value)
radio2 = tkinter.Radiobutton(option_frame, text="Path", value=2, variabl=rb_value)
radio3 = tkinter.Radiobutton(option_frame, text="Timestamp", value=3, variabl=rb_value)
radio1.grid(row=0, column=0, sticky='w')
radio2.grid(row=1, column=0, sticky='w')
radio3.grid(row=2, column=0, sticky='w')

# Widget to display the result.
result_lable = tkinter.Label(mainwindow, text="Result", )
result_lable.grid(row=2, column=2, sticky='nw')
result = tkinter.Entry(mainwindow)
result.grid(row=2, column=2, sticky='sw')

# Frame for the time spinners
time_frame = tkinter.LabelFrame(mainwindow, text="Time")
time_frame.grid(row=3, column=0, sticky='new')
# Time spinners
hour_spinner = tkinter.Spinbox(time_frame, width=2, values=tuple(range(0, 24)))
minute_spinner = tkinter.Spinbox(time_frame, width=2, from_=0, to=59)
second_spinner = tkinter.Spinbox(time_frame, width=2, from_=0, to=59)
hour_spinner.grid(row=0, column=0)
tkinter.Label(time_frame, text=':').grid(row=0, column=1)
minute_spinner.grid(row=0, column=2)
tkinter.Label(time_frame, text=':').grid(row=0, column=3)
second_spinner.grid(row=0, column=4)
time_frame['padx'] = 36

# Frame for the date spinners
date_frame = tkinter.Frame(mainwindow)
date_frame.grid(row=4, column=0, sticky='new')
# Date lables
day_lable = tkinter.Label(date_frame, text='Day')
month_lable = tkinter.Label(date_frame, text='Month')
year_lable = tkinter.Label(date_frame, text='Year')
day_lable.grid(row=0, column=0, sticky='w')
month_lable.grid(row=0, column=1, sticky='w')
year_lable.grid(row=0, column=2, sticky='w')
# Date spinners
day_spin = tkinter.Spinbox(date_frame, width=5, from_=1, to=31)
year_spin = tkinter.Spinbox(date_frame, width=5, from_=2000, to=2099)
month_spin = tkinter.Spinbox(date_frame, width=5, values=('Jan','Feb',"Mar",'Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'))
day_spin.grid(row=1, column=0)
month_spin.grid(row=1, column=1)
year_spin.grid(row=1, column=2)

# Buttons
ok_button = tkinter.Button(mainwindow, text="OK")
cancle_button = tkinter.Button(mainwindow, text="Cancle", command=mainwindow.destroy)
# If we put () after mainwindow.quit method then id doesn't work and we can also use 'destroy' method
ok_button.grid(row=4, column=3, sticky='e')
cancle_button.grid(row=4, column=4, sticky='w')

mainwindow.mainloop()

print(rb_value.get())