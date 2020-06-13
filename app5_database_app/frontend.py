
from tkinter import *
from backend import Database

database = Database('book.db')

def get_selected_row(event): #event is a special parameter generated by the bind method
    try:
        global selected_tuple
        index = list1.curselection()[0] #store index of the item from output list
        selected_tuple = list1.get(index) #tuple id and item index from output list is different
        title_entry.delete(0, END)
        title_entry.insert(END,selected_tuple[1])
        author_entry.delete(0, END)
        author_entry.insert(END, selected_tuple[2])
        year_entry.delete(0, END)
        year_entry.insert(END,selected_tuple[3])
        isbn_entry.delete(0, END)
        isbn_entry.insert(END,selected_tuple[4])
    except IndexError:
        pass

def view_command():
    list1.delete(0,END)
    for i in database.view():
        list1.insert(END, i)

def search_command():
    list1.delete(0,END)
    for i in  database.search(title_entry.get(), author_entry.get(), year_entry.get(),isbn_entry.get() ):
        list1.insert(END, i)

def add_command():
    database.insert(title_entry.get(), author_entry.get(), year_entry.get(),isbn_entry.get())

def delete_command():
    list1.delete(0,END)
    database.delete(selected_tuple[0])
    for i in database.view():
        list1.insert(END, i)

def update_command():
    list1.delete(0,END)
    database.update(selected_tuple[0],title_entry.get(),author_entry.get(), year_entry.get(),isbn_entry.get() )
    for i in database.view():
        list1.insert(END, i)

#create a pop up window widget
window = Tk()
window.wm_title("Book Store")

#create label fields
title_label = Label(window, text = 'Title') 
title_label.grid(row = 0, column = 0)

year_label = Label(window, text = 'Year') 
year_label.grid(row = 1, column = 0)

author_label = Label(window, text = 'Author') 
author_label.grid(row = 0, column = 2)

isbn_label = Label(window, text = 'ISBN') 
isbn_label.grid(row = 1, column = 2)

#create entry fields
title_val = StringVar()
title_entry = Entry(window, textvariable= title_val)
title_entry.grid(row = 0, column = 1 )

year_val = StringVar()
year_entry = Entry(window, textvariable= year_val)
year_entry.grid(row = 1, column = 1 )

author_val = StringVar()
author_entry = Entry(window, textvariable= author_val)
author_entry.grid(row = 0, column = 3 )

isbn_val = StringVar()
isbn_entry = Entry(window, textvariable= isbn_val)
isbn_entry.grid(row = 1, column = 3 )

#create output box
list1 = Listbox(window, height = 6, width = 35)
list1.grid(row = 2, column = 0, rowspan = 6, columnspan = 2)

list1.bind('<<ListboxSelect>>', get_selected_row)

#create scrollbar
sb1 = Scrollbar(window)
sb1.grid(row = 2, column = 2, rowspan = 6)
#where the scroll bar being use
list1.configure(yscrollcommand = sb1.set)
sb1.configure(command = list1.yview)

#create bottons
b1 = Button(window, text='View all', width = 12, command= view_command)
b1.grid(row = 2, column = 3 )

b2 = Button(window, text='Search entry', width = 12, command = search_command)
b2.grid(row = 3, column = 3 )

b3 = Button(window, text='Add entry', width = 12, command = add_command)
b3.grid(row = 4, column = 3 )

b4 = Button(window, text='Update', width = 12, command = update_command)
b4.grid(row = 5, column = 3 )

b5 = Button(window, text='Delete', width = 12, command = delete_command)
b5.grid(row = 6, column = 3 )

b6 = Button(window, text='Close', width = 12, command = window.destroy)
b6.grid(row = 7, column = 3 )

window.mainloop()


"""
This is a front end window allow users to:

1. View all data in database
2. Search entry
3. Add entry
4. Delete entry
5. Update entry
6. Close

Estimated grid outpit: 8 x 5

"""
