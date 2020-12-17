"""
    Desktop App
    Python GUI | tkinter
    Reference Read: https://docs.python.org/3/library/tkinter.html
"""

from tkinter import *
from tkinter import messagebox
import mysql.connector as db

def on_click():
    customer = {
        "name": entry_name.get(),
        "phone": entry_phone.get(),
        "email": entry_email.get()
    }
    # print("Button Clicked :)")
    #
    # print()
    # print("Data Entered Is:")
    # print(customer)
    connection = db.connect(user="root", password="", database="auridb", host="127.0.0.1", port="3306")
    cursor = connection.cursor()
    sql = "insert into Customer values (null, '{}', '{}', '{}')". \
        format(customer['name'], customer['phone'], customer['email'])
    cursor.execute(sql)
    connection.commit()
    cursor.close()
    # print(customer['name'], "Saved :)")
    messagebox.showinfo("Customer Saved", "{} Saved in DataBase Successfully"
                        .format(customer['name']))

# Window of our Application
window = Tk()
# print(window, type(window))

lbl_title = Label(window, text="Customer Management System")
lbl_title.pack()

lbl_name = Label(window, text="Enter Customer Name")
lbl_name.pack()

entry_name = Entry(window)
entry_name.pack()

lbl_phone = Label(window, text="Enter Customer Phone")
lbl_phone.pack()

entry_phone = Entry(window)
entry_phone.pack()

lbl_email = Label(window, text="Enter Customer Email")
lbl_email.pack()

entry_email = Entry(window)
entry_email.pack()

btn_add = Button(window, text="ADD CUSTOMER", command=on_click)
btn_add.pack()

window.mainloop()