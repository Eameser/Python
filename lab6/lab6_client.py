import socket
from tkinter import *
import tkinter as tk

def click_send():
    sock.send(text_record.get().encode())
    text.insert(1.0,sock.recv(1024).decode() + "\n")
    text_record.delete(0, tk.END)

window = Tk()
window.title("Чат")
window.geometry('500x400')
window["bg"] = "beige"
frame = Frame(window)
frame["bg"] = "beige"
frame.pack()
sock = socket.socket()
sock.connect(("localhost", 9090))
str_record = StringVar()
text_record = Entry(frame, font=("Courier", 10), textvariable = str_record,width=45)
text_record.grid(row=0, column=0)
send = Button(frame, text="Отправить", background="white", foreground="black", padx="20", pady="8", font=("Courier", 8),command=lambda: click_send())
send.grid(row=0, column=1)
text = Text(frame, width=45, height=32,  wrap=WORD)
text.grid(row=1)
window.mainloop()
sock.close()