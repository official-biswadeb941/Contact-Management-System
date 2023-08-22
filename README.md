**_Contact Management Application_**

**_Description_**

The Contact Management System is a graphical user interface (GUI) program developed using Tkinter and MySQL. It was first made by "Krazy Programmer" in 2021 and it is Upgraded by Biswadeb Mukherjee in 2023. It allows users to manage their contacts by adding, viewing, updating, and deleting contact information such as names, genders, phone numbers, and email addresses.


**_1.Features_**

- Add new contacts with validation checks for name format, gender, phone number, and email address.
- View all existing contacts in a tabular format.
- Update contact information by selecting a contact from the table.
- Delete one or multiple selected contacts.
- Live search functionality to search for contacts based on phone number, email, or last name.
- User-friendly GUI for ease of use.


**_2.Requirements_**

- Python 3.1+ (including Tkinter, which is included by default)
- MySQL Server (local or remote)
- MySQL Connector/Python


**_3.Setup_**

- Install Python: Download and install Python from [python.org](https://www.python.org/downloads/).
- Install MySQL: Install and configure MySQL Server on your machine or use a remote MySQL server.
- Install Dependencies: Install the required dependencies using the following command:

pip install mysql-connector-python

- Configure Database: Modify the `db_config` dictionary in the code to match your MySQL server configuration.
- Run the Application: Open a terminal/command prompt, navigate to the project directory, and run the following command: 
- If you want to make this python code windows executable the Follow the procedure given below:

**_1.Install pyinstaller if you haven't already:_**

pip install pyinstaller

**_2.Navigate to the directory containing your Python script in the terminal._**

**_3.Run the following command to generate the executable without a console window:_**

pyinstaller --onefile --noconsole your_script.py

Replace your_script.py with the actual name of your Python script.

The --onefile flag bundles everything into a single executable file, and the --noconsole flag tells pyinstaller not to display a console window.

For example, if you have a script named my_script.py, you would run:

pyinstaller --onefile --noconsole my_script.py

The generated executable will be located in the dist folder within the directory where your script is located.
 
**_4.Usage_**

- Launch the application using the provided command.
- Fill in the contact details (First Name, Last Name, Gender, Phone Number, Email) and click the "Submit" button to add a new contact.
- Use the "View All" button to see a list of all existing contacts.
- Double-click on a contact in the table to populate the fields for updating. After making changes, click the "Update" button.
- To delete contacts, select one or more rows from the table and click the "Delete" button.
- Use the search bar to search for contacts based on phone number, email, or last name. The table will display the matching results in real time.


**_5.Screenshots_**
 

**_6.Known Issues_**

- Up to now, it's showing a " RuntimeError: Too early to run the main loop: no default root window".


**_7.License_**

- This project is licensed under the [MIT License](LICENSE).


**_8.Contact_**

- For questions or inquiries, please contact me at the given mail address: biswadebmukherjee941@gmail.com.

