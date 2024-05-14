from PyQt5.QtWidgets import *
from UI import Ui_Form
from tkinter import *
import requests


class Appointments():
    def __init__(self, UI: Ui_Form, MW):
        self.LineEdit = QLineEdit()
        self.main_win = QMainWindow()
        self.ui = UI
        self.mw = MW

    def SearchByCustomer(self):
        name = self.ui.SearchByCustomerLineEdit.text()
        results = requests.get(f"http://localhost:8000/api/appointment_by_customer?fullname={name}")
        data = results.json()
        for i in data["results"]:
            self.ui.AppointmentsPrintLabel.setText(f'''
Client: {i["Client"]}
Pet: {i["Pet"]}
Date: {i["Date"]}
Service/s: {i["Services"]}
Staff: {i["Staff"]}
Address: {i["Address"]}
''')
            
    def InitialiseAPCombobox(self):
        results =  requests.get(f"http://localhost:8000/api/list_customers")
        data = results.json()

        for i in data["results"]:
            pull = requests.get(f'http://localhost:8000/api/appointment_by_customer?fullname={i["FirstName"]} {i["LastName"]}')
            final = pull.json()
            if final["results"] != False:
                for b in final["results"]:
                    self.ui.SearchAppointmentComboBox.addItem(f"{b['Client']} - {b['Date']}")

    def APComboBoxChanged(self):
        date = self.ui.SearchCustomersComboBox.currentText().split(" ")
        results = requests.get(f"http://localhost:8000/api/appointment_by_date?date={date[1]}")
        data = results.json()
        

