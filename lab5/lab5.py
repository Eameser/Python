from tkinter import *
from tkinter import messagebox as mb
import tkinter as tk
from tkinter import filedialog as fd
from tkinter.filedialog import askopenfilename

class Automobile:
    def __init__(self, code, mark, model, producting_year, condition, type_of_carcass, price):
        self.code = code
        self.mark = mark
        self.model = model
        self.producting_year = producting_year
        self.condition = condition
        self.type_of_carcass = type_of_carcass
        self.price = price

auto = [Automobile(1, "chevrolet", "corvette", "1967", "Б/У", "sedan", 10000),
Automobile(2, "lada", "largus", "2014", "Новая", "CUV", 7000),
Automobile(3, "Shcoda", "octavia", "2014", "Новая", "liftback", 7000)]

type_of_carcass = ["sedan", "coupe", "van", "hatchback", "pickup", "CUV", "liftback"]

def hat(i, j, frame):
    r_var = IntVar()
    r_var.set(0)
    lable_code = Label(frame, text="Код авто", font=("Courier", 10), background="maroon", padx="20", pady="8", width=12, height=1, borderwidth=2, relief="groove")
    lable_code.grid(row=1+i, column=1+j)
    lable_mark = Label(frame, text="Марка", font=("Courier", 10), background="maroon", padx="20", pady="8", width=8, height=1, borderwidth=2, relief="groove")
    lable_mark.grid(row=1+i, column=2+j)
    lable_model = Label(frame, text="Модель", font=("Courier", 10), background="maroon", padx="20", pady="8", width=8, height=1, borderwidth=2, relief="groove")
    lable_model.grid(row=1+i, column=3+j)
    lable_producting_year = Label(frame, text="Год выпуска", font=("Courier", 10), background="maroon", padx="20", pady="8", width=8, height=1, borderwidth=2, relief="groove")
    lable_producting_year.grid(row=1+i, column=4+j)
    lable_condition = Label(frame, text="Состояние", font=("Courier", 10), background="maroon", padx="20", pady="8", width=8, height=1, borderwidth=2, relief="groove")
    lable_condition.grid(row=1+i, column=5+j)
    lable_type_of_carcass = Label(frame, text="Тип кузова", font=("Courier", 10), background="maroon", padx="20", pady="8", width=8, height=1, borderwidth=2, relief="groove")
    lable_type_of_carcass.grid(row=1+i, column=6+j)
    lable_price = Label(frame, text="Цена", font=("Courier", 10), background="maroon", padx="20", pady="8", width=8, height=1, borderwidth=2, relief="groove")
    lable_price.grid(row=1+i, column=7+j)

def body(i,k,h, frame):
    code = Label(frame, text=str(auto[i].code), font=("Courier", 10), background="gray", padx="20", pady="8", width=12, height=1, borderwidth=2, relief="groove")
    code.grid(row=i + k, column=1+h)
    mark = Label(frame, text=str(auto[i].mark), font=("Courier", 10), background="gray", padx="20", pady="8", width=8, height=1, borderwidth=2, relief="groove")
    mark.grid(row=i + k, column=2+h)
    model = Label(frame, text=str(auto[i].model), font=("Courier", 10), background="gray", padx="20", pady="8", width=8, height=1, borderwidth=2, relief="groove")
    model.grid(row=i + k, column=3+h)
    producting_year = Label(frame, text=str(auto[i].producting_year), font=("Courier", 10), background="gray", padx="20", pady="8", width=8, height=1, borderwidth=2, relief="groove")
    producting_year.grid(row=i + k, column=4+h)
    condition = Label(frame, text=str(auto[i].condition), font=("Courier", 10), background="gray", padx="20", pady="8", width=8, height=1, borderwidth=2, relief="groove")
    condition.grid(row=i + k, column=5+h)
    type_of_carcass = Label(frame, text=str(auto[i].type_of_carcass), font=("Courier", 10), background="gray", padx="20", pady="8",width=8, height=1, borderwidth=2, relief="groove")
    type_of_carcass.grid(row=i + k, column=6+h)
    price = Label(frame, text=str(auto[i].price), font=("Courier", 10), background="gray", padx="20", pady="8", width=8, height=1, borderwidth=2, relief="groove")
    price.grid(row=i + k, column=7+h)

def click_show(frame_lable,frame, window):

    for widget in frame_lable.winfo_children():
        widget.destroy()

    for widget in frame.winfo_children():
        widget.destroy()

    # frame.grid_forget()
    r_var = IntVar()
    r_var.set(0)
    hat(0, 0, frame)
    radiobutton = []

    for i in range(len(auto)):
        r = Radiobutton(frame, background="dark gray", activebackground="dark gray", variable=r_var, value=i)
        r.grid(row=i + 2, column=0)
        body(i, 2, 0, frame)
        radiobutton.append(r)

def click_create(frame_lable, str_code, str_mark, str_model, str_producting_year, str_price, variable, r_var):
    condition = "" 
    if (r_var.get()):
        condition = "new"
    else:
        condition = "used"
    auto.append(
        Automobile(str(str_code.get()), str(str_mark.get()), str(str_model.get()), str(str_producting_year.get()),
                str(condition), str(str_price.get()), str(variable.get())))

    hint = Label(frame_lable, text="Запись добавлена", font=("Courier", 8), background="white",padx="20", pady="8", width=15, height=1).grid(row=0, column=0)

def click_delete(frame_table, window, r_var):
    if len(auto) != 0:
        auto.pop(r_var.get())
    hint = Label(frame_lable, text="Запись удалена", font=("Courier", 8), background="white", padx="20", pady="8", width=15, height=1).grid(row=0, column=0)

def click_find(frame_table, variable):

    for widget in frame_table.winfo_children():
        widget.destroy()
    hat(0, 0, frame_table)
    for i in range(len(auto)):
        if(auto[i].producting_year == str_producting_year.get()):
            body(i, 2, 0, frame_table)

def click_allexit():
    window.destroy()

def click_info():
    mb.showinfo("Информация", "Информация о правах приложения и разработчике ")

def click_new_record():
    text_code.delete(0, tk.END)
    text_mark.delete(0, tk.END)
    text_model.delete(0, tk.END)
    text_producting_year.delete(0, tk.END)
    text_price.delete(0, tk.END)
    r_var.set(0)
    variable.set(discipline[0])

def click_open(frame_lable,frame, window):
    auto.clear()
    f = askopenfilename()
    for line in f:
        Automobile =line.split(" ")
        auto.append(Automobile(str(Automobile[0]),Automobile[1],Automobile[2],Automobile[3],Automobile[4],str(Automobile[5]),str(Automobile[6]),Automobile[7],str(Automobile[8])))
    click_show(frame_lable, frame, window)

def click_save():
    try:
        f = open('text.dat', 'x')
        file_name = fd.asksaveasfilename()
        f = open(file_name, 'w')
        for i in range(len(auto)):
            f.write(str(auto[i].code) + " " + auto[i].mark + " " + auto[i].model + " " + auto[
                i].producting_year + " " + auto[i].producting_year + " " + " " + str(
                auto[i].price) + " " + auto[i].type_of_carcass + " "  + "\n")
        f.close()
    except:
        f = open('text.dat', 'w')
        for i in range(len(auto)):
            f.write(str(auto[i].code) + " " + auto[i].mark + " " + auto[i].model + " " + auto[
                i].producting_year + " " + auto[i].producting_year + " " + " " + str(
                auto[i].price) + " " + auto[i].type_of_carcass + " "  + "\n")
        f.close()

def click_saveas():
    file_name = fd.asksaveasfilename()
    f = open(file_name, 'w')
    for i in range(len(auto)):
        f.write(str(auto[i].code) + " " + auto[i].mark + " " + auto[i].model + " " + auto[
                i].producting_year + " " + auto[i].producting_year + " " + " " + str(
                auto[i].price) + " " + auto[i].type_of_carcass + " "  + "\n")
    f.close()

window = Tk()
window.title("Автомобили")
window.geometry('800x600')
window["bg"] = "white"

mainmenu = Menu(window)
window.config(menu=mainmenu)
filemenu = Menu(mainmenu, tearoff=0)
helpmenu = Menu(mainmenu, tearoff=0)

filemenu.add_command(label="Создать",command=lambda: click_new_record())
filemenu.add_command(label="Открыть",command=lambda: click_open(frame_lable,frame_table, window))
filemenu.add_command(label="Сохранить",command=lambda: click_save())
filemenu.add_command(label="Сохранить как...", command=lambda: click_saveas())
filemenu.add_command(label="Выход", command=lambda: click_allexit())
helpmenu.add_command(label="Информация", command=lambda: click_info())
mainmenu.add_cascade(label="Файл", menu=filemenu)
mainmenu.add_cascade(label="Справка", menu=helpmenu)

frame_lable = Frame(window)
frame_lable["bg"] = "gray"
hint = Label(frame_lable, text="", font=("Courier", 8), background="white",padx="20", pady="8", width=15, height=1).grid(row=0, column=0)
frame_btn = Frame(window)
frame_btn["bg"] = "gray"

frame_table = Frame()
frame_table["bg"] = "gray"
frame_new_record = Frame(window)
frame_new_record["bg"] = "gray"
frame_lable.pack()
frame_btn.pack()
frame_new_record.pack()
frame_table.pack()

create = Button(frame_btn, text="Добавление записи", background="maroon", foreground="white", padx="20", pady="8", font=("Courier", 10), command=lambda: click_create(frame_lable,str_code, str_mark, str_model, str_producting_year, str_price, variable, r_var)).grid(row=0, column=0)
delete = Button(frame_btn, text="Удаление записи", background="maroon", foreground="white", padx="20", pady="8", font=("Courier", 10), command=lambda: click_delete(frame_table, window,r_var)).grid(row=0, column=1)
show = Button(frame_btn, text="Отобразить записи", background="maroon", foreground="white", padx="20", pady="8", font=("Courier", 10),  command=lambda: click_show(frame_lable,frame_table, window)).grid(row=0, column=2)
find = Button(frame_btn, text="Найти запись", background="maroon", foreground="white", padx="20", pady="8", font=("Courier", 10),command=lambda: click_find(frame_table,variable)).grid(row=0, column=3)

lable_code = Label(frame_new_record, text="Код: ", font=("Courier", 10), background="dark gray",padx="20", pady="8", width=15, height=1).grid(row=0, column=0)
str_code = StringVar()
text_code = Entry(frame_new_record, font=("Courier", 10), textvariable = str_code).grid(row=0, column=1)
lable_mark = Label(frame_new_record, text="Марка: ", font=("Courier", 10), background="dark gray",padx="20", pady="8", width=15, height=1).grid(row=1, column=0)
str_mark = StringVar()
text_mark = Entry(frame_new_record, font=("Courier", 10), textvariable = str_mark).grid(row=1, column=1)
str_model = StringVar()
lable_model = Label(frame_new_record, text="Модель: ", font=("Courier", 10), background="dark gray",padx="20", pady="8", width=15, height=1).grid(row=2, column=0)
text_model = Entry(frame_new_record, font=("Courier", 10), textvariable = str_model ).grid(row=2, column=1)
str_producting_year = StringVar()
lable_producting_year = Label(frame_new_record, text="Год выпуска: ", font=("Courier", 10), background="dark gray",padx="20", pady="8", width=15, height=1).grid(row=3, column=0)
text_producting_year = Entry(frame_new_record, font=("Courier", 10), textvariable = str_producting_year).grid(row=3, column=1)
lable_condotion = Label(frame_new_record, text="Состояние: ", font=("Courier", 10), background="dark gray",padx="20", pady="8", width=15, height=1).grid(row=4, column=0)
r_var = BooleanVar()
r_var.set(0)
new = Radiobutton(frame_new_record, text="Новая", font=("Courier", 10), background="dark gray", activebackground="dark gray",  variable=r_var, value=0).grid(row=4, column=1)
used = Radiobutton(frame_new_record, text="Б/У", font=("Courier", 10), background="dark gray", activebackground="dark gray", variable=r_var, value=1).grid(row=4, column=2)
lable_type_of_carcass = Label(frame_new_record, text="Тип кузова: ", font=("Courier", 10), background="dark gray",padx="20", pady="8", width=15, height=1).grid(row=2, column=2)
variable = StringVar(frame_new_record)
variable.set(type_of_carcass[0])
w = OptionMenu(frame_new_record, variable, *type_of_carcass)
w.grid(row=2, column=3)
lable_price = Label(frame_new_record, text="Цена: ", font=("Courier", 10), background="dark gray",padx="20", pady="8", width=15, height=1).grid(row=0, column=2)
str_price = StringVar()
text_price = Entry(frame_new_record, font=("Courier", 10), textvariable = str_price).grid(row=0, column=3)

window.mainloop()