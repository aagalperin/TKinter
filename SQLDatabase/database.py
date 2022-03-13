from tkinter import *
import sqlite3

root = Tk()
root.title("SQL database GUI - by aagalperin")
root.iconbitmap('database_icon.ico')
root.geometry("350x500")

# Create a Databease or connect to one that already exists
conn = sqlite3.connect('address_book.db')

# Creatint my cursor - the one that will
my_cursor = conn.cursor()

# Create table
'''
my_cursor.execute("""
CREATE TABLE 
addresses(
first_name text, 
last_name text, 
address text, 
city text, 
state text, 
zipcode integer
)"""
                  )
# text, integer, real, null, blob
'''

# Create data entries / text boxes:
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10, 0))
l_name = Entry(root, width=30)
l_name.grid(row=1, column=1)
address = Entry(root, width=30)
address.grid(row=2, column=1)
city = Entry(root, width=30)
city.grid(row=3, column=1)
state = Entry(root, width=30)
state.grid(row=4, column=1)
zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1)

delete_box = Entry(root, width=30)
delete_box.grid(row=9, column=1, pady=5)

# Create text box label :
f_name_label = Label(root, text="First Name ")
f_name_label.grid(row=0, column=0, pady=(10, 0))
l_name_label = Label(root, text="Last Name ")
l_name_label.grid(row=1, column=0)
address_label = Label(root, text="Address ")
address_label.grid(row=2, column=0)
city_label = Label(root, text="City ")
city_label.grid(row=3, column=0)
state_label = Label(root, text="State ")
state_label.grid(row=4, column=0)
zipcode_label = Label(root, text="Zipcode ")
zipcode_label.grid(row=5, column=0)
delete_box_label = Label(root, text="Id number : ")
delete_box_label.grid(row=9, column=0, pady=5)

# Create submit button an its function:
def submit():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()
    c.execute("INSERT INTO addresses VALUES(:f_name, :l_name, :address, :city, :state, :zipcode)",
              {
                  'f_name': f_name.get(),
                  'l_name': l_name.get(),
                  'address': address.get(),
                  'city': city.get(),
                  'state': state.get(),
                  'zipcode': zipcode.get()
              })
    conn.commit()
    conn.close()

    # clear the text boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)


submit_btn = Button(root, text="Add record to DB", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)


# Create Query Button
def get_data():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()
    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()
    # facthany, fecthone

    print_records = ""
    for record in records:
        print_records += str(record[6]) + " : " + str(record[0]) + " " + str(record[1]) + "\n"

    query_label = Label(root, text=print_records)
    query_label.grid(row=8, column=0, columnspan=2)

    conn.commit()
    conn.close()


query_btn = Button(root, text="Show Records", command=get_data)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=110)


# Create Function to delete a record
def delete_item():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()

    c.execute("DELETE FROM addresses WHERE oid=" + delete_box.get())

    conn.commit()
    conn.close()


delete_btn = Button(root, text="Delete Record", command=delete_item)
delete_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=110)

# Create an Update
def update_windows():
    global editor
    editor = Tk()
    editor.title("Update a record- by aagalperin")
    editor.iconbitmap('database_icon.ico')
    editor.geometry("350x200")

    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()
    record_id = delete_box.get()
    c.execute("SELECT * FROM addresses WHERE oid=" + record_id)
    records = c.fetchall()

    conn.commit()
    conn.close()

    global f_name_editor
    global l_name_editor
    global address_editor
    global city_editor
    global state_editor
    global zipcode_editor

    # Create data entries / text boxes:
    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))
    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1)
    address_editor = Entry(editor, width=30)
    address_editor.grid(row=2, column=1)
    city_editor = Entry(editor, width=30)
    city_editor.grid(row=3, column=1)
    state_editor = Entry(editor, width=30)
    state_editor.grid(row=4, column=1)
    zipcode_editor = Entry(editor, width=30)
    zipcode_editor.grid(row=5, column=1)

    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        state_editor.insert(0, record[4])
        zipcode_editor.insert(0, record[5])

    # Create text box label :
    f_name_label_editor = Label(editor, text="First Name ")
    f_name_label_editor.grid(row=0, column=0, pady=(10, 0))
    l_name_label_editor = Label(editor, text="Last Name ")
    l_name_label_editor.grid(row=1, column=0)
    address_label_editor = Label(editor, text="Address ")
    address_label_editor.grid(row=2, column=0)
    city_label_editor = Label(editor, text="City ")
    city_label_editor.grid(row=3, column=0)
    state_label_editor = Label(editor, text="State ")
    state_label_editor.grid(row=4, column=0)
    zipcode_label_editor = Label(editor, text="Zipcode ")
    zipcode_label_editor.grid(row=5, column=0)


    save_btn = Button(editor, text="Save changes", command=update_entry)
    save_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=115)


def update_entry():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()
    record_id = delete_box.get()
    c.execute("""UPDATE addresses SET first_name = :first, last_name = :last, address = :address, city = :city, 
    state = :state, zipcode = :zipcode WHERE oid = :oid""",
              {
                  'first': f_name_editor.get(),
                  'last': l_name_editor.get(),
                  'address': address_editor.get(),
                  'city': city_editor.get(),
                  'state': state_editor.get(),
                  'zipcode': zipcode_editor.get(),
                  'oid': record_id

              })

    conn.commit()
    conn.close()
    editor.destroy()


update_btn = Button(root, text="Edit Record", command=update_windows)
update_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=115)


# Commit Changes
conn.commit()

# Close connection
conn.close()

root.mainloop()
