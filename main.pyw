import tkinter as tk
import subprocess as sub_proc
import requests as req
from tkinter import ttk


def get_key():
    if req.get('https://2m0j30.deta.dev/get_access/').json()['status'] == True:
        lisensi.set(sub_proc.check_output('wmic csproduct get UUID').decode('utf-8').split('\n')[1].strip())
    else:
        lisensi.set('Akses ditutup !')


def close():
    req.post('https://2m0j30.deta.dev/toggle_access/false/12457')
    root.destroy()


root = tk.Tk()
root.title('Key Gen - Program Koperasi')
root.geometry(f'340x80+{root.winfo_screenwidth()//2 - 170}+{root.winfo_screenheight()//2 - 40}')
root.wm_protocol('WM_DELETE_WINDOW', close)
root.resizable(tk.FALSE, tk.FALSE)
root.columnconfigure(1, weight=1)
root.rowconfigure(1, weight=1)

frame = ttk.Frame(root)
frame.grid(column=1, row=1, sticky=tk.NSEW)
lisensi = tk.StringVar()
frame.columnconfigure(1, weight=1)
frame.rowconfigure(1, weight=1)
frame.rowconfigure(2, weight=1)
ttk.Label(frame, text='Lisensi (Lisensi hanya dapat dilihat sekali, \nuntuk lisensi lainnya mohon hubungi airell_zulkarnain)', justify='center', anchor='center').grid(column=1, row=1, sticky=tk.NSEW)
ttk.Entry(frame, textvariable=lisensi, state='readonly', justify='center').grid(column=1, row=2, sticky=tk.NSEW)
get_key()



root.mainloop()
