import sys
sys.dont_write_bytecode = True
import PySimpleGUI as sg

#------------------------------- SIGNUP WINDOW -------------------------------

class SignupWindow:
    def __init__(self, title, user_manager):
        self.user_manager = user_manager
        sg.theme("DarkBlue")
        self.title = title
        self.layout = [
            [sg.Titlebar(f"{title}", key="-SUB_WINDOW-")],
            [sg.Text(f"{self.title}")],
            [sg.Text("Username"), sg.Input("", key="-USERNAME-")],
            [sg.Text("Password"), sg.Input("", key="-PASSWORD-", password_char='*')],
            [sg.Button("OK", key="-OK_SIGNUP-"), sg.Button("Cancel", key="-CANCEL_SIGNUP-")]
        ]
        
        self.window = sg.Window("DES App", self.layout, finalize=True)
        self.window.hide()
     
    def get_window(self):
        return self.window
    
    #------------------------------- SIGNUP WINDOW METHODS -------------------------------