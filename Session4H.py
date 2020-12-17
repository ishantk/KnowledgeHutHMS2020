from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from tkinter import scrolledtext

def on_click():
    # messagebox.showinfo("This is Title", "This is Message in Message Box")
    # messagebox.showerror("This is Title", "This is Message in Message Box")
    # messagebox.showwarning("This is Title", "This is Message in Message Box")

    # response = messagebox.askquestion("Delete", "Would You Like to Delete?")
    # print(response, type(response))

    response = messagebox.askokcancel("Delete", "Would You Like to Delete?")
    print(response, type(response))

window = Tk()
window.title("My App")

lbl_title = Label(window, text="Customer Management System")
# lbl_title.pack()

# Layout as Grid rather than just packing it :)
lbl_title.grid(column=0, row=0)

btn_submit = Button(window, text="SUBMIT", command=on_click)
btn_submit.grid(column=1, row=0)

combo_box = Combobox(window)
combo_box['values'] = ("Select City", "Delhi", "Bangalore", "Chennai", "Hyderabad", "Mumbai")
combo_box.current(0)
combo_box.grid(column=0, row=2)

check_button_state = BooleanVar()
check_button_state.set(True)
check_button = Checkbutton(window, text="I Accept Terms and Conditions", var=check_button_state)
check_button.grid(column=0, row=3)

scrolled_text = scrolledtext.ScrolledText(window, width=40, height=10)
scrolled_text.grid(column=0, row=4)

window.geometry('350x350')
window.mainloop()