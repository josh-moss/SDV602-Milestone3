import PySimpleGUI as sg
from .BaseWindow import BaseWindow

class MainWindow(BaseWindow):
    def __init__(self):
        super().__init__()
        sg.theme("DarkBlue")
        self.layout = [
            [sg.Text("Main Window", font=("Calibri", 24)), sg.Push(), sg.Button("Upload Data", key="-DATA-", size=(12,1)), sg.Button("Upload JSNDrop", key="-JDROP_DATA-", size=(12,1)), sg.Button("Login", key="-LOGIN-", size=(12,1))],
            [sg.Canvas(background_color="white", key="-CANVAS-", size=(600, 500)), sg.Multiline(size=(50, 30), key="-CHAT-", disabled=True, autoscroll=True)],
            [sg.Button("Previous Chart", key="-PREV-", size=(20,1)), sg.Button("Next Chart", key="-NEXT-", size=(20,1)), sg.Push(), sg.Column([[sg.Input(size=(40, 1), key="-MESSAGE-"), sg.Button("Send", key="-SEND-", bind_return_key=True, size=(10,1))]])],
            [sg.Column([[sg.Button("Show window 2", key="-SHOW_2-", size=(15,1)), sg.Button("Show Window 3", key="-SHOW_3-", size=(15,1))]]), sg.Push(), sg.Button("Exit", size=(10, 1))]
        ]
        
        self.window = sg.Window("DES App", self.layout, resizable=False, finalize=True)
        self.canvas_elem = self.window["-CANVAS-"]
        self.state = {"hidden": False}

    def get_window(self):
        return self.window