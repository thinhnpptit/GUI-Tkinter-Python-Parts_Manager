from tkinter import *
from tkinter import messagebox
from db_part import Database

db = Database('store_parts.db')

tk = Tk()
tk.geometry("750x500")
tk.title("Part Manager")

# define Functions

def select_item(event):
    global selected_item
    index = parts_list.curselection()
    selected_item = parts_list.get(index)
    clear_text()
    part_entry.insert(END, selected_item[1])
    customer_entry.insert(END, selected_item[2])
    amount_entry.insert(END, selected_item[3])
    price_entry.insert(END, selected_item[4])
    v.set(selected_item[5])

def add_item():
    if part_text.get() == '' or customer_text.get() == '' or amount_text.get() == '' or price_text.get() == ''or v.get() =='':
        messagebox.showerror("Error", "Please include all fields")
        return
    db.insert(part_text.get(), customer_text.get(),
              amount_text.get(), price_text.get(), v.get())
    parts_list.delete(0, END)
    parts_list.insert(END, (part_text.get(), customer_text.get(),
                            amount_text.get(), price_text.get(),v.get()))
    show_list()


def remove_item():
    db.remove(selected_item[0])
    # db.reset()
    show_list()


def update_item():
    db.update(selected_item[0],part_text.get(),customer_text.get(), amount_text.get(), price_text.get(),v.get())
    show_list()

def clear_text():
    part_entry.delete(0, END)
    customer_entry.delete(0, END)
    amount_entry.delete(0, END)
    price_entry.delete(0, END)
    radio1.deselect()
    radio2.deselect()

def show_list():
    parts_list.delete(0, END)
    for row in db.fetch():
        parts_list.insert(END, row)

# define UI


# Part Listbox
parts_list = Listbox(tk, height=8, width=50)
parts_list.grid(row=4, column=0, columnspan=3, rowspan=6, pady=20, padx=20)
# Create Scrollbar
scrollbar = Scrollbar(tk)
scrollbar.grid(row=6, column=3)
# Set scroll to listbox
parts_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=parts_list.yview)

parts_list.bind('<<ListboxSelect>>', select_item)

part_text = StringVar()
part_lb = Label(tk, text='Part Name', font=("bold", 14), pady=20, padx=20)
part_lb.grid(row=0, column=0)
part_entry = Entry(tk, textvariable=part_text)
part_entry.grid(row=0, column=1)

customer_text = StringVar()
customer_lb = Label(tk, text='Customer', font=("bold", 14), padx=20)
customer_lb.grid(row=0, column=2)
customer_entry = Entry(tk, textvariable=customer_text)
customer_entry.grid(row=0, column=3)

amount_text = StringVar()
amount_lb = Label(tk, text='Amount', font=("bold", 14), pady=20)
amount_lb.grid(row=1, column=0)
amount_entry = Entry(tk, textvariable=amount_text)
amount_entry.grid(row=1, column=1)

price_text = StringVar()
price_lb = Label(tk, text='Unit Price', font=("bold", 14), pady=20)
price_lb.grid(row=1, column=2)
price_entry = Entry(tk, textvariable=price_text)
price_entry.grid(row=1, column=3)

v = StringVar()
branch_lb = Label(tk, text="Branch", font=("bold", 14))
branch_lb.grid(row=2, column=0)
radio1 = Radiobutton(tk, text="Hà Nội", variable=v, value="Hà Nội")
radio1.grid(row=2, column=1)
radio2 = Radiobutton(tk, text="Hồ Chí Minh", variable=v, value="Hồ Chí Minh")
radio2.grid(row=2, column=2)

# Buttons
add_btn = Button(tk, text="Add part", width=12, command=add_item)
add_btn.grid(row=3, column=0, pady=20)

remove_btn = Button(tk, text="Remove part", width=12, command=remove_item)
remove_btn.grid(row=3, column=1, pady=20)

update_btn = Button(tk, text="Update part", width=12, command=update_item)
update_btn.grid(row=3, column=2, pady=20)

clear_btn = Button(tk, text="Clear input", width=12, command=clear_text)
clear_btn.grid(row=3, column=3, pady=20)

show_list()

tk.mainloop()
