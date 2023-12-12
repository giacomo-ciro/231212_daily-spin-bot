import tkinter as tk
from tkinter import filedialog

from driver import spin
import datetime as dt

USERNAME = ""
PASSWORD = ""
PATH = ""

def save_login_info():
    global USERNAME, PASSWORD
    USERNAME = username_entry.get()
    PASSWORD = password_entry.get()

    if USERNAME == "" or PASSWORD == "" or PATH == "":
        loginAlert_label.configure(text='Please provide complete login info and folder directory.')
        print(USERNAME, PASSWORD, PATH)
    else:
        loginAlert_label.configure(text=f'Login info for "{USERNAME}" successfuly saved')
        toggle_btn.pack(side='bottom', pady=10)
        spin_now_btn.pack(side='bottom', pady=10)
        username_entry.delete(0, 'end')
        password_entry.delete(0, 'end')
        save_login_info_btn.configure(text='Update Login Info')

    return


def browse_folder():
    global PATH
    PATH = filedialog.askdirectory()
    if PATH:
        chosenPath_label.config(text="Selected folder: " + PATH)


def toggle_loop():
    global running
    if running:
        running = False
        toggle_btn.config(text="Initiate")
    else:
        running = True
        toggle_btn.config(text="Pause")
        run_loop()

def run_loop():

    if running:

        H,M = 0,1
        current_time = dt.datetime.now()
        target_time = dt.datetime(current_time.year, current_time.month, current_time.day, H,M,0)
        delta = target_time - dt.datetime.now()
        hours = delta.seconds // 3600
        minutes = delta.seconds % 3600 // 60
        seconds = delta.seconds % 3600 % 60
        countdown_label.configure(text = f'{hours}:{minutes}:{seconds}')

        if (hours + minutes + seconds) < 1:
            spin(USERNAME, PASSWORD)
            spin(USERNAME, PASSWORD, PATH, screenshot=True)

        root.after(1000, run_loop)

root = tk.Tk()
root.title("Daily Spin Bot")
root.iconbitmap('G:/My Drive/[02] Projects/230106_Selenium/231209_DailySpinBot/icon.ico')
root.geometry('300x500')

description_label = tk.Label(root, text=open('G:/My Drive/[02] Projects/230106_Selenium/231209_DailySpinBot/description.txt', 'r').read())
username_label = tk.Label(root, text="Username:")
username_entry = tk.Entry(root)
password_label = tk.Label(root, text="Password:")
password_entry = tk.Entry(root, show="*")
chosenPath_label = tk.Label(root, text="No path selected.")
browse_btn = tk.Button(root, text="Browse Folder", command=browse_folder)
save_login_info_btn = tk.Button(root, text="Save Login Info", command=save_login_info)
loginAlert_label = tk.Label(root, text="")
countdown_label = tk.Label(root, text="")
spin_now_btn = tk.Button(root, text="Spin Now", command=lambda: spin(USERNAME, PASSWORD, PATH))
credits_label = tk.Label(root, text='© 2023 | giacomo-ciro.github.io')
target_time_label = tk.Label(root, text = "")
toggle_btn = tk.Button(root, text="Initiate", command=toggle_loop)

description_label.pack(side='top', pady=10)
credits_label.pack(side='bottom', pady=10)
username_label.pack()
username_entry.pack()
password_label.pack()
password_entry.pack()
chosenPath_label.pack()
browse_btn.pack()
save_login_info_btn.pack(pady=10)
loginAlert_label.pack()
target_time_label.pack(pady=10)
countdown_label.pack(pady=10)

running = False

root.mainloop()





