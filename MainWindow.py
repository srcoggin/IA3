from PyQt5.QtWidgets import QMainWindow, QMessageBox
from UI import Ui_Form
from PyQt5.QtWidgets import *
from Customers import Customers





class NewMainWindow():
    def __init__(self):
        self.LineEdit = QLineEdit()
        self.ui = Ui_Form()
        self.main_win = QMainWindow()
        self.ui.setupUi(self.main_win)
        self.ui.stackedWidget.setCurrentWidget(self.ui.Home)
        self.CP = Customers(self.ui, self)

        #initialises the comboboxes
        self.ui.SearchCustomersComboBox.addItem(" ")
        self.CP.InitialiseCombobox()

        #Home Page Buttons
        self.ui.CustomersButton_HomePage.clicked.connect(self.CustomerPage)
        self.ui.AppointmentButton_HomePage.clicked.connect(self.Appointment1Page)
        self.ui.PetsButton_HomeButton.clicked.connect(self.PetsPage)
        self.ui.ExitButton_HomePage.clicked.connect(self.Exit)

        #Customer Page Buttons
        self.ui.HomeButton_CustomersPage.clicked.connect(self.HomePage)
        self.ui.AppointmentButton_CustomersPage.clicked.connect(self.Appointment1Page)
        self.ui.PetsButton_CustomersPage.clicked.connect(self.PetsPage)
        self.ui.ExitButton_CustomersPage.clicked.connect(self.Exit)
        self.ui.SearchByFirstNameButton.clicked.connect(self.CP.SearchByFirstName)
        self.ui.SearchCustomersComboBox.currentIndexChanged.connect(self.CP.ComboBoxChange)
        self.ui.SearchByLastNameButton.clicked.connect(self.CP.SearchByLastName)
        self.ui.SearchByPhoneButton.clicked.connect(self.CP.SearchByPhone)

        #Appointment Page 1 Buttons
        self.ui.HomeButton_AppointmentsPage1.clicked.connect(self.HomePage)
        self.ui.CustomersButton_AppointmentsPage1.clicked.connect(self.CustomerPage)
        #Appointment Page 1 - Page 2 Button Goes Here
        self.ui.PetsButton_AppointmentsPage1.clicked.connect(self.PetsPage)
        self.ui.ExitButton_AppointmentsPage1.clicked.connect(self.Exit)

        #Appointment Page 2 Buttons
        self.ui.HomeButton_AppointmentsPage2.clicked.connect(self.HomePage)
        self.ui.CustomersButton_AppointmentsPage2.clicked.connect(self.CustomerPage)
        self.ui.AppointmentButton_AppointmentsPage2.clicked.connect(self.Appointment1Page)
        self.ui.ExitButton_AppointmentsPage2.clicked.connect(self.Exit)

        #Pets Page Buttons
        self.ui.HomeButton_PetsPage.clicked.connect(self.HomePage)
        self.ui.CustomersButton_PetsPage.clicked.connect(self.CustomerPage)
        self.ui.AppointmentButton_PetsPage.clicked.connect(self.Appointment1Page)
        self.ui.ExitButton_PetsPage.clicked.connect(self.PetsPage)



    #Page Selections
    def HomePage(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Home)
    def CustomerPage(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Customers)
    def Appointment1Page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Appointments1)
    def Appointment2Page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Appointments2)
    def PetsPage(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Pets)

    #Exits the program
    def Exit(self):
        exit()

    #Shows the user interface
    def show(self):
        self.main_win.show()