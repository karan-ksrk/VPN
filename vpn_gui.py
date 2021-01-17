#!/usr/bin/python3

import tkinter as tk
from tkinter import filedialog, Text, font
import subprocess as sp
import os

root = tk.Tk()
root.resizable(width=False, height=False)

vpn_status = 'None'

def startVPN():
    print("Starting VPN...")
    p1 = sp.run(['protonvpn-cli',  'c', '-f'], stdout=sp.PIPE, text=True)
    print(p1.stdout)
    checkStatus()

def disconnectVPN():
    p2 = sp.run(['protonvpn-cli',  'disconnect'], stdout=sp.PIPE, text=True)
    print(p2.stdout)
    checkStatus()

def checkStatus():
    p3 = sp.run(['protonvpn-cli',  'status'], stdout=sp.PIPE, text=True)
    global vpn_status
    vpn_status = p3.stdout
    label.config(text=vpn_status)

canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
canvas.pack()

frame1 = tk.Frame(root, bg="yellow")
frame1.place(relwidth=0.8, relheight=0.2, relx=0.1, rely=0.1)
start = tk.Button(frame1, text="Start", padx=10, pady=5, fg="white", bg="black", command=startVPN)
disconnect = tk.Button(frame1, text="Disconnect", padx=10, pady=5, fg="white", bg="black", command=disconnectVPN)
status = tk.Button(frame1, text="Status", padx=10, pady=5, fg="white", bg="black", command=checkStatus)
start.grid(row=1, column=0)
disconnect.grid(row=1, column=1)
status.grid(row=1, column=2)

frame2 = tk.Frame(root, bg="grey")
frame2.place(relwidth=0.8, relheight=0.5, relx=0.1, rely=0.3)
label = tk.Label(frame2, text=f"{vpn_status}", bg="white", anchor="center")
label.grid(row=0, column=0, padx=(100, 100), pady=(10, 10))
checkStatus()


root.mainloop()
