from PyQt5.QtWidgets import *
from UI import Ui_Form
from tkinter import *
import requests


class Customers():
    def __init__(self, UI: Ui_Form, MW):
        self.LineEdit = QLineEdit()
        self.main_win = QMainWindow()
        self.ui = UI
        self.mw = MW


    def SearchByFirstName(self):
        name = self.ui.SearchByFirstNameLineEdit.text()
        results = requests.get(f"http://localhost:8000/api/customer_by_first_name?name={name}")
        data = results.json()
        for i in data["results"]:
            self.ui.CustomersPrintLabel.setText(f''' 
Client: {i["Client"]}
Email: {i["Email"]}
Phone: {i["Phone"]}
Address: {i["Address"]}
''')
            
    def InitialiseCPCombobox(self):
        results = requests.get(f"http://localhost:8000/api/list_customers")
        data = results.json()
        for i in data["results"]:
            self.ui.SearchCustomersComboBox.addItem(f"{i['FirstName']} {i['LastName']}")
    
    def ComboBoxChange(self):
        lastname = self.ui.SearchCustomersComboBox.currentText().split(" ")
        results = requests.get(f"http://localhost:8000/api/customer_by_first_surname?name={lastname[1]}")
        data = results.json()
        for i in data["results"]:
            self.ui.CustomersPrintLabel.setText(f''' 
Client: {i["Client"]}
Email: {i["Email"]}
Phone: {i["Phone"]}
Address: {i["Address"]}
''')
            
    def SearchByLastName(self):
        lastname = self.ui.SearchByLastNameLineEdit.text()
        results = requests.get(f"http://localhost:8000/api/customer_by_first_surname?name={lastname}")
        data = results.json()
        for i in data["results"]:
            self.ui.CustomersPrintLabel.setText(f''' 
Client: {i["Client"]}
Email: {i["Email"]}
Phone: {i["Phone"]}
Address: {i["Address"]}
''')
            
    def SearchByPhone(self):
        phone = self.ui.SearchByPhoneLineEdit.text()
        results = requests.get(f"http://localhost:8000/api/customer_by_phone?phone={phone}")
        data = results.json()
        for i in data["results"]:
            self.ui.CustomersPrintLabel.setText(f''' 
Client: {i["Client"]}
Email: {i["Email"]}
Phone: {i["Phone"]}
Address: {i["Address"]}
''')
        
