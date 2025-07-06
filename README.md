#  Password Manager CLI (Python)

A simple, menu-driven command-line password manager built in Python.  
Securely store, view, and delete your login credentials in a local file vault.

---

##  Features

-  Add new website credentials
-  View stored passwords (with masking)
-  Delete specific entries by number
-  Master-key protected access
-  File-based storage (no external database)

---

##  Project Structure
   password-manager/
- ├── main.py
- ├── data/
- │ └── vault.txt
- └── README.md

---

##  How to Run

###  Requirements
- Python 3.7+

###  Run the App

```bash
python main.py
'''

Enter master key: ********

--- Password Manager ---
1. Add Password
2. View Passwords
3. Delete Password
4. Exit

Choose an option: 1

Website: example.com
Username: user@example.com
Password: mysecurepass
✅Password saved.



