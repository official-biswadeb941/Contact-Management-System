# Contact-Management-System

**_Contact Management Application_**

**_Description_**

The Contact Management Application is a graphical user interface (GUI) program developed using Tkinter and MySQL. It allows users to manage their contacts by adding, viewing, updating, and deleting contact information such as names, genders, phone numbers, and email addresses.


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

