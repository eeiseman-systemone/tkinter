# Need to rework to not us globals and pass variables between functions

from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title("Learn Tkinter")
root.iconbitmap("icon.ico")
root.geometry("400x600")

# Create Table
'''
c.execute("""CREATE TABLE addresses (
    first_name text,
    last_name text,
    address text,
    city text,
    state text,
    zipcode integer
  )""")
'''

# Create text boxes with initial values
# must do .grid after object generation or 
# delete function doesn't work.
# .grid doesn't return anything so the variable never gets set
f_name = Entry(root, width=30)
f_name.grid(row=0,column=1,padx=20, pady=(10,0))
l_name = Entry(root, width=30)
l_name.grid(row=1,column=1,padx=20)
address = Entry(root, width=30)
address.grid(row=2,column=1,padx=20)
city = Entry(root, width=30)
city.grid(row=3,column=1,padx=20)
state = Entry(root, width=30)
state.grid(row=4,column=1,padx=20)
zipcode = Entry(root, width=30)
zipcode.grid(row=5,column=1,padx=20)

delete_box = Entry(root, width=30)
delete_box.grid(row=9, column=1, pady=5)

# Create text box labels
f_name_label =  Label(root,text="First Name")
f_name_label.grid(row=0, column=0, padx=20, pady=(10,0))
l_name_label =  Label(root,text="Last Name")
l_name_label.grid(row=1, column=0)
address_label =  Label(root,text="Address")
address_label.grid(row=2, column=0)
city_label =  Label(root,text="City")
city_label.grid(row=3, column=0)
state_label =  Label(root,text="State")
state_label.grid(row=4, column=0)
zipcode_label =  Label(root,text="Zipcode")
zipcode_label.grid(row=5, column=0)



delete_box_label = Label(root, text="Select ID")
delete_box_label.grid(row=9, column=0, pady=5)



def edit():
  editor = Tk()
  editor.title("Learn Tkinter")
  editor.iconbitmap("icon.ico")
  editor.geometry("400x600")

  conn = sqlite3.connect('address_book.db')

  # Create cursor
  c = conn.cursor()  

  record_id = delete_box.get()
  f_name_editor = Entry(editor, width=30)
  f_name_editor.grid(row=0,column=1,padx=20, pady=(10,0))
  l_name_editor = Entry(editor, width=30)
  l_name_editor.grid(row=1,column=1,padx=20)
  address_editor = Entry(editor, width=30)
  address_editor.grid(row=2,column=1,padx=20)
  city_editor = Entry(editor, width=30)
  city_editor.grid(row=3,column=1,padx=20)
  state_editor = Entry(editor, width=30)
  state_editor.grid(row=4,column=1,padx=20)
  zipcode_editor = Entry(editor, width=30)
  zipcode_editor.grid(row=5,column=1,padx=20)

  f_name_label_editor =  Label(editor,text="First Name")
  f_name_label_editor.grid(row=0, column=0, padx=20, pady=(10,0))
  l_name_label_editor =  Label(editor,text="Last Name")
  l_name_label_editor.grid(row=1, column=0)
  address_label_editor =  Label(editor,text="Address")
  address_label_editor.grid(row=2, column=0)
  city_label_editor =  Label(editor,text="City")
  city_label_editor.grid(row=3, column=0)
  state_label_editor =  Label(editor,text="State")
  state_label_editor.grid(row=4, column=0)
  zipcode_label_editor =  Label(editor,text="Zipcode")
  zipcode_label_editor.grid(row=5, column=0)



def update():
  conn = sqlite3.connect('address_book.db')

  # Create cursor
  c = conn.cursor()    

  # Create globals
  global f_name_editor
  global f

  c.execute("""UPDATE addresses SET 
            first_name = :first,
            last_name = :last,
            address = :address,
            city = :city,
            state = :state,
            zipcode = :zipcode

            WHERE oid = :oid""",
           {
              'first': f_name_editor.get(),
              'last': l_name.get(),
              'address': address.get(),
              'city': city.get(),
              'state': state.get(),
              'zipcode': zipcode.get()
            }


            
            )

  #Commit Changes
  conn.commit()

  # Close Connection 
  conn.close()

  # Query the database
  c.execute("SELECT * FROM addresses WHERE oid=" + record_id)
  records = c.fetchall()
  # print(records)

  # Loop through results
  for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        state_editor.insert(0, record[4])
        zipcode_editor.insert(0, record[5])

  edit_btn = Button(editor, text="Save Record", command=update)
  edit_btn.grid(row=6, column=0, columnspan=2, padx=10, pady=10, ipadx=133)

  #Commit Changes
  conn.commit()

  # Close Connection 
  conn.close()



# Create Function to Delete a record
def delete():
    # Create a database or connect to one
  conn = sqlite3.connect('address_book.db')

  # Create cursor
  c = conn.cursor()

  # Delete a record
  c.execute("DELETE FROM addresses WHERE oid=" + delete_box.get())

  #Commit Changes
  conn.commit()

  # Close Connection 
  conn.close()

# Create submit function for database
def submit():
  # Create a database or connect to one
  conn = sqlite3.connect('address_book.db')

  # Create cursor
  c = conn.cursor()

  # Intert into table
  c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
            {
              'f_name': f_name.get(),
              'l_name': l_name.get(),
              'address': address.get(),
              'city': city.get(),
              'state': state.get(),
              'zipcode': zipcode.get()
            }
          )

  # Clear the text boxes
  f_name.delete(0, END)
  l_name.delete(0, END)
  address.delete(0, END)
  city.delete(0, END)
  state.delete(0, END)
  zipcode.delete(0, END)

  #Commit Changes
  conn.commit()

  # Close Connection 
  conn.close()

def query():
  conn = sqlite3.connect('address_book.db')

  # Create cursor
  c = conn.cursor()  

  # Query the database
  c.execute("SELECT *, oid FROM addresses")
  records = c.fetchall()
  # print(records)
  
  # Loop through results
  print_records = ''
  for record in records:
    print_records += str(record[0]) + " " + str(record[1]) + " " + "\t" + str(record[6]) + "\n"

  query_label = Label(root, text=print_records)
  query_label.grid(row=12, column=0, columnspan=2)



  #Commit Changes
  conn.commit()

  # Close Connection 
  conn.close()  

# Create submit button
submit_btn = Button(root, text="Add Record to Database", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, padx=10, pady=10, ipadx=100)

query_btn = Button(root, text="Show Records", command=query)
query_btn.grid(row=7, column=0, columnspan=2, padx=10, pady=10, ipadx=127)

# Create a delete button
delete_btn = Button(root, text="Delete Record", command=delete)
delete_btn.grid(row=10, column=0, columnspan=2, padx=10, pady=10, ipadx=126)

# Create an update button
edit_btn = Button(root, text="Edit Record", command=edit)
edit_btn.grid(row=11, column=0, columnspan=2, padx=10, pady=10, ipadx=133)


root.mainloop()
