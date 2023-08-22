#A Python Based Project made by Krazy Programmer and Customised & released by Biswadeb Mukherjee.

from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
import mysql.connector
import re

# Modify these variables according to your MySQL server configuration
db_config = {
    'user': 'root',
    'password': '',
    'host': '127.0.0.1',
    'port':3306,
    'database': 'contacts',
}


#function to define database
def Database():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        cursor.execute("CREATE TABLE IF NOT EXISTS REGISTRATION (RID INT AUTO_INCREMENT PRIMARY KEY, `First Name` VARCHAR(255), `Last Name` VARCHAR(255), `Gender` VARCHAR(255), `Phone Number` VARCHAR(255), `Email Id` VARCHAR(255))")

        conn.commit()
    except mysql.connector.Error as err:
        print("Error:", err)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()


#defining function for creating GUI Layout
def DisplayForm():
    #creating window
    display_screen = Tk()
    #setting width and height for window
    display_screen.geometry("1080x700")
    #setting title for window
    display_screen.title("Biswadeb Mukherjee Official presents")
    global tree
    global SEARCH
    global First_Name, Last_Name, Gender, Phone_Number, Email_Id
    SEARCH = StringVar()
    First_Name = StringVar()
    Last_Name = StringVar()
    Gender = StringVar()
    Phone_Number = StringVar()
    Email_Id = StringVar()
    #creating frames for layout
    #topview frame for heading
    TopViewForm = Frame(display_screen, width=600, bd=1, relief=SOLID)
    TopViewForm.pack(side=TOP, fill=X)
    #first left frame for registration from
    LFrom = Frame(display_screen, width="350",bg="#13d450")
    LFrom.pack(side=LEFT, fill=Y)
    #seconf left frame for search form
    LeftViewForm = Frame(display_screen, width=500,bg="#0B4670")
    LeftViewForm.pack(side=LEFT, fill=Y)
    #mid frame for displaying lnames record
    MidViewForm = Frame(display_screen, width=600)
    MidViewForm.pack(side=RIGHT)
    #label for heading
    lbl_text = Label(TopViewForm, text="Contact Management System", font=("Cascadia code", 15, "bold"), width=600,bg="cyan")
    lbl_text.pack(fill=X)
    #creating registration form in first left frame
    Label(LFrom, text="First Name  ", font=("Arthura", 15, "bold"),bg="#13d450",fg="white").pack(side=TOP)
    Entry(LFrom,font=("Arthura", 15, "bold"),textvariable=First_Name).pack(side=TOP, padx=10, fill=X)
    Label(LFrom, text="Last Name ", font=("Arthura", 15, "bold"),bg="#13d450",fg="white").pack(side=TOP)
    Entry(LFrom, font=("Arthura", 15, "bold"),textvariable=Last_Name).pack(side=TOP, padx=10, fill=X)
    Label(LFrom, text="Gender ", font=("Arthura", 15, "bold"),bg="#13d450",fg="white").pack(side=TOP)
    Entry(LFrom, font=("Arthura", 15, "bold"),textvariable=Gender).pack(side=TOP, padx=10, fill=X)
    Gender.set("Select Gender")
    content={'Male','Female'}
    OptionMenu(LFrom,Gender,*content).pack(side=TOP, padx=10, fill=X)

    Label(LFrom, text="Phone Number ", font=("Arthura", 15, "bold"),bg="#13d450",fg="white").pack(side=TOP)
    Entry(LFrom, font=("Arthura", 15, "bold"),textvariable=Phone_Number).pack(side=TOP, padx=10, fill=X)
    Label(LFrom, text="Email Id ", font=("Arthura", 15, "bold"),bg="#13d450",fg="white").pack(side=TOP)
    Entry(LFrom, font=("Arthura", 15, "bold"),textvariable=Email_Id).pack(side=TOP, padx=10, fill=X)

    #creating search label and entry in second frame
    lbl_txtsearch = Label(LeftViewForm, text="Enter Search Term", font=('verdana', 10),bg="green")
    lbl_txtsearch.pack()
    #creating search entry
    search = Entry(LeftViewForm, textvariable=SEARCH, font=('verdana', 15), width=10)
    search.pack(side=TOP, padx=10, fill=X)
    search.bind("<KeyRelease>", LiveSearch)  # Bind the event to the function

    #creating view button
    btn_view = Button(LeftViewForm, text="View All", command=DisplayData,bg="cyan")
    btn_view.pack(side=TOP, padx=10, pady=10, fill=X)
    # creating delete button
    delete_button = Button(LeftViewForm, text="Delete", command=Delete, bg="cyan")
    delete_button.pack(side=TOP, padx=10, pady=10, fill=X)

    # creating the "Submit" button
    submit_button = Button(LFrom, text="Submit", font=("Arthura", 15, "bold"), command=register, bg="#15244C",
                           fg="white")
    submit_button.pack(side=TOP, padx=10, pady=5, fill=X)

    # connect "Enter" key to "Submit"
    display_screen.bind("<Return>", lambda event: submit_button.invoke())
    #setting scrollbar
    scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
    scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
    tree = ttk.Treeview(MidViewForm,columns=("Student Id", "First Name", "Last Name", "Gender", "Phone Number", "Email Id"),
                        selectmode="extended", height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    #setting headings for the columns
    tree.heading('Student Id', text="Id", anchor=W)
    tree.heading('First Name', text="First Name", anchor=W)
    tree.heading('Last Name', text="Last Name", anchor=W)
    tree.heading('Gender', text="Gender", anchor=W)
    tree.heading('Phone Number', text="Phone Number", anchor=W)
    tree.heading('Email Id', text="Email Id", anchor=W)
    #setting width of the columns
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=100)
    tree.column('#2', stretch=NO, minwidth=0, width=150)
    tree.column('#3', stretch=NO, minwidth=0, width=80)
    tree.column('#4', stretch=NO, minwidth=0, width=120)
    tree.pack()
    DisplayData()
    display_screen.mainloop()

#function to update data into database

def Update():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    first_name = First_Name.get()
    last_name = Last_Name.get()
    gender = Gender.get()
    phone_number = Phone_Number.get()
    email_id = Email_Id.get()

    if first_name == '' or last_name == '' or gender == '' or phone_number == '' or email_id == '':
        tkMessageBox.showinfo("Warning", "Fill in all fields!")
    else:
        try:
            curItem = tree.focus()
            contents = tree.item(curItem)
            selecteditem = contents['values']

            update_query = "UPDATE REGISTRATION SET `First Name`=%s, `Last Name`=%s, `Gender`=%s, `Phone Number`=%s, `Email Id`=%s WHERE ID = %s"
            values = (first_name, last_name, gender, phone_number, email_id, selecteditem[0])
            cursor.execute(update_query, values)
            conn.commit()

            tkMessageBox.showinfo("Message", "Updated successfully")
            DisplayData()
        except mysql.connector.Error as err:
            print("Error:", err)
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()
def register():
    first_name = First_Name.get()
    last_name = Last_Name.get()
    gender = Gender.get()
    phone_number = Phone_Number.get()
    email_id = Email_Id.get()

    if not first_name or not last_name:
        tkMessageBox.showinfo("Warning", "First Name and Last Name are required!")
    elif not first_name[0].isupper() or not last_name[0].isupper():
        tkMessageBox.showinfo("Warning", "First letter of First Name and Last Name must be in uppercase.")
    elif gender == "Select Gender":
        tkMessageBox.showinfo("Warning", "Please select a gender.")
    elif not re.match(r'^\d{10}$', phone_number):
        tkMessageBox.showinfo("Warning", "Invalid phone number! Please enter a 10-digit number.")
    elif not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email_id):
        tkMessageBox.showinfo("Warning", "Invalid email format! Please enter a valid email address.")
    else:
        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()

            # Check for existing records with the same phone number or email
            duplicate_query = "SELECT * FROM REGISTRATION WHERE `Phone Number` = %s OR `Email Id` = %s"
            cursor.execute(duplicate_query, (phone_number, email_id))
            duplicate_data = cursor.fetchall()

            if duplicate_data:
                tkMessageBox.showinfo("Warning", "A record with the same phone number or email already exists!")
            else:
                insert_query = "INSERT INTO REGISTRATION (`First Name`, `Last Name`, `Gender`, `Phone Number`, `Email Id`) VALUES (%s, %s, %s, %s, %s)"
                values = (first_name, last_name, gender, phone_number, email_id)
                cursor.execute(insert_query, values)
                conn.commit()

                tkMessageBox.showinfo("Message", "Stored successfully")
                DisplayData()
        except mysql.connector.Error as err:
            print("Error:", err)
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

def LiveSearch(event):
    search_term = SEARCH.get()

    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        tree.delete(*tree.get_children())

        search_query = (
            "SELECT * FROM REGISTRATION WHERE "
            "`Phone Number` LIKE %s OR "
            "`Email Id` LIKE %s OR "
            "`Last Name` LIKE %s"
        )
        cursor.execute(search_query, ('%' + search_term + '%', '%' + search_term + '%', '%' + search_term + '%'))
        fetch = cursor.fetchall()

        if not fetch:
            tkMessageBox.showinfo("Info", "No matching records found.")
        else:
            for data in fetch:
                tree.insert('', 'end', values=data)
    except mysql.connector.Error as err:
        tkMessageBox.showerror("Error", f"An error occurred: {err}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def DisplayData():
    tree.delete(*tree.get_children())

    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        select_query = "SELECT * FROM REGISTRATION"
        cursor.execute(select_query)
        fetch = cursor.fetchall()

        for data in fetch:
            tree.insert('', 'end', values=data)
    except mysql.connector.Error as err:
        print("Error:", err)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def DisplayData():
    tree.delete(*tree.get_children())

    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        select_query = "SELECT * FROM REGISTRATION"
        cursor.execute(select_query)
        fetch = cursor.fetchall()

        for data in fetch:
            tree.insert('', 'end', values=data)
    except mysql.connector.Error as err:
        print("Error:", err)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()


def Delete():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        selected_items = tree.selection()

        if not selected_items:
            tkMessageBox.showinfo("Info", "No rows selected for deletion.")
        else:
            result = tkMessageBox.askquestion('Confirm', 'Are you sure you want to delete the selected record(s)?', icon="warning")
            if result == 'yes':
                for selected_item in selected_items:
                    contents = tree.item(selected_item)
                    selected_data = contents['values']
                    delete_query = "DELETE FROM REGISTRATION WHERE `ID` = %s"
                    cursor.execute(delete_query, (selected_data[0],))
                    conn.commit()

                    tree.delete(selected_item)
                tkMessageBox.showinfo("Message", "Record(s) deleted successfully")
    except mysql.connector.Error as err:
        tkMessageBox.showerror("Error", f"An error occurred: {err}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()


#function to search data
def SearchRecord():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        search_term = SEARCH.get()

        if not search_term:
            tkMessageBox.showwarning("Warning", "Please enter the search data")
        else:
            tree.delete(*tree.get_children())

            search_query = (
                "SELECT * FROM REGISTRATION WHERE "
                "`Phone Number` LIKE %s OR "
                "`Email Id` LIKE %s OR "
                "`Last Name` LIKE %s"
            )
            cursor.execute(search_query, ('%' + search_term + '%', '%' + search_term + '%', '%' + search_term + '%'))
            fetch = cursor.fetchall()

            if not fetch:
                tkMessageBox.showinfo("Info", "No matching records found.")
            else:
                for data in fetch:
                    tree.insert('', 'end', values=data)
    except mysql.connector.Error as err:
        tkMessageBox.showerror("Error", f"An error occurred: {err}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

#defining function to access data from SQLite database
def DisplayData():
    conn = None
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        tree.delete(*tree.get_children())

        select_query = "SELECT * FROM REGISTRATION"
        cursor.execute(select_query)
        fetch = cursor.fetchall()

        for data in fetch:
            tree.insert('', 'end', values=data)
    except mysql.connector.Error as err:
        tkMessageBox.showerror("Error", f"An error occurred: {err}")
    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()

def OnDoubleClick(self):
    try:
        curItem = tree.focus()
        contents = tree.item(curItem)
        selecteditem = contents['values']

        First_Name.set(selecteditem[1])
        Last_Name.set(selecteditem[2])
        Gender.set(selecteditem[3])
        Phone_Number.set(selecteditem[4])
        Email_Id.set(selecteditem[5])
    except IndexError:
        pass

# Define the main function that sets up the GUI
def main():
    DisplayForm()

if __name__ == '__main__':
    # Run the main function to create the GUI and then start the main event loop
    main()
    mainloop()
