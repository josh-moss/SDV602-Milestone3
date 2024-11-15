import PySimpleGUI as sg
from model.user_manager import UserManager

from GUIWindows.MainWindow import MainWindow
from GUIWindows.SubWindow import SubWindow
from GUIWindows.LoginWindow import LoginWindow
from GUIWindows.SignupWindow import SignupWindow
from GUIWindows.SubWindow2 import SubWindowTwo


#-------------------------------        TODO            -------------------------------




#------------------------------- MAIN CLASS FOR DES APP -------------------------------

class Main:
    def __init__(self):
        self.main_window = MainWindow()
        self.user_manager = UserManager()
        self.window_2 = SubWindow("Window 2")
        self.window_3 = SubWindowTwo("Window 3")
        self.login_window = LoginWindow("Login Window", self.user_manager)
        self.signup_window = SignupWindow("SignUpWindow", self.user_manager)
        self.charts = None
        
        self.windows = {
            "main_window": {"window": self.main_window, "hidden": False},
            "window_2": {"window": self.window_2, "hidden": True},
            "window_3": {"window": self.window_3, "hidden": True},
            "login_window": {"window": self.login_window, "hidden": True},
            "signup_window": {"window": self.signup_window, "hidden": True}
        }
        
        self.canvas = None
        self.logged_in = False

#------------------------------- METHODS -------------------------------
        
    def update_chat(self):
        self.chat_message = self.a_user_manager.get_chat()
        if self.chat_message:
            self.display_chat = "\n".join(f"{msg['Username']}: {msg['-MESSAGE-']}" for msg in self.chat_message)
        else:
            self.display_chat = ""
        self.main_window.get_window()["-CHAT-"].update(self.display_chat)

    def send_message(self, message):
        self.a_user_manager = UserManager()
        self.message_result = self.a_user_manager.chat(message)
        print(f"Got login result: {self.message_result}")

        self.update_chat()
        
    def logout(self):
        self.a_user_manager.logout()
        
#------------------------------- EVENTS -------------------------------

    def DesApp(self):
        while True:
            window, event, values = sg.read_all_windows()
            
            if event in (sg.WINDOW_CLOSED, "Exit"):
                break
            
            #perhaps better to handle events as mthods, call method instance ?

            if event == "-SEND-":
                self.message = values["-MESSAGE-"]
                if self.message:
                    self.send_message(self.message)
                    self.main_window.get_window()["-MESSAGE-"].update("")
                
            if event == "-OK_LOGIN-":   
                from model.user_manager import UserManager
                self.a_user_manager = UserManager()
                self.user_name = values["-USERNAME-"]
                self.password = values["-PASSWORD-"]
                self.login_result = self.a_user_manager.login(self.user_name,self.password)
                if self.login_result == "Login Success":
                    sg.popup(f"you are logged in as: {self.user_name}")
                    self.login_window.get_window().hide()
            
            if event == "-OK_SIGNUP-":
                from model.user_manager import UserManager
                a_user_manager = UserManager()
                self.user_name = values["-USERNAME-"]
                self.password = values["-PASSWORD-"]
                self.register_result = a_user_manager.register(self.user_name, self.password)
                self.signup_window.get_window().hide()
                sg.popup(f"{self.register_result}")
                self.login_window.get_window().un_hide()
            
            if event == "-LOGIN-":
                self.login_window.get_window().un_hide()
                if self.user_manager.current_status == "Logged In":
                    self.main_window.get_window()["-LOGIN-"].update("Logout")
                    self.logged_in = True
                else:
                    if event == "Logout":
                        self.user_manager.logout()
                        
            
            if event == "-SIGNUP-":
                self.login_window.get_window().hide()
                self.signup_window.get_window().un_hide()
            elif event == "-CANCEL_SIGNUP-":
                self.signup_window.get_window().hide()
                
            if event == "-CANCEL_LOGIN-":
                self.login_window.get_window().hide()
            
            if event == "-SHOW_2-":
                self.window_2.toggle_visibility(self.windows["window_2"])
            elif event == "-SHOW_3-":
                self.window_3.toggle_visibility(self.windows["window_3"])
            elif event == "-HIDE-":
                if window == self.window_2.get_window():
                    self.window_2.toggle_visibility(self.windows["window_2"])
                elif window == self.window_3.get_window():
                    self.window_3.toggle_visibility(self.windows["window_3"])
                    
            if event == "-DATA-":
                self.main_window.upload_csv()
            if event == "-SUB_DATA-":
                self.window_2.upload_csv()
            if event == "-SUB_DATA_2-":
                self.window_3.upload_csv()
            if event == "-JDROP_DATA-":
                self.user_manager.upload_json_drop()
            
            if self.window_3.charts is not None:
                self.window_3.handle_sub2_chart_events(event)
            if self.window_2.charts is not None:
                self.window_2.handle_sub_chart_events(event)
            if self.main_window.charts is not None:
                self.main_window.handle_chart_events(event)
                
                
        self.main_window.get_window().close()
        
if __name__ == "__main__":
    DESAPP = Main()
    DESAPP.DesApp()