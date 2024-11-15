import PySimpleGUI as sg
from .BaseWindow import BaseWindow

#------------------------------- SUBWINDOW CLASS -------------------------------

class SubWindow(BaseWindow):
    def __init__(self, title="Sub Window"):
        super().__init__()
        sg.theme("DarkBlue")
        self.title = title
        self.layout = [
            [sg.Titlebar(f"{self.title}", key="-SUB_WINDOW-")],
            [sg.Text(f"{self.title}"), sg.Push(), sg.Button("Upload Data", key="-SUB_DATA-", size=(10,1))],
            [sg.Canvas(background_color="white", key="-CANVAS-", size=(500, 500)), sg.Multiline(size=(50, 31), key="-CHAT-", disabled=True, autoscroll=True)],
            [sg.Button("Previous Chart", key="-SUB_PREV-", size=(20,1)), sg.Button("Next Chart", key="-SUB_NEXT-", size=(20,1)), sg.Push(), sg.Column([[sg.Input(size=(40, 1), key="-MESSAGE-"), sg.Button("Send", key="-SEND-", bind_return_key=True, size=(10,1))]])],
            [sg.Push(), sg.Button("Hide", key="-HIDE-", size=(10,1))]
        ]
        
        self.window = sg.Window(self.title, self.layout, finalize=True)
        self.window.hide()
        self.canvas_elem = self.window["-CANVAS-"]
        self.state = {"hidden": True}

    def get_window(self):
        return self.window
