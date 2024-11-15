import PySimpleGUI as sg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.pyplot as plt
from Charts.Charts import Charts

class BaseWindow:
    
    def __init__(self):
        
        self.canvas = None
        self.canvas_elem = None
        self.charts = None
        self.current_index = 0
        self.file_path = None
        self.toolbar = None

    def draw_chart(self):
        self.delete_figure_agg()
        
        if self.charts is not None:
            chart_name = self.charts.chart_keys[self.current_index]
            fig = self.charts.charts[chart_name]()
            self.canvas = FigureCanvasTkAgg(fig, self.canvas_elem.Widget)
            self.canvas.draw()
            self.canvas.get_tk_widget().pack(side="top", fill="both", expand=True)
            self.toolbar = NavigationToolbar2Tk(self.canvas, self.canvas_elem.Widget)
            self.toolbar.update()
            self.toolbar.pack(side="top", fill="x")

    def delete_figure_agg(self):
        
        if self.toolbar is not None:
            try:
                self.toolbar.pack_forget()
                self.toolbar.destroy()
            except Exception as e:
                print(f"eerror removeing toolbar: {e}")
            finally:
                self.toolbar = None
                

        if self.canvas is not None:
            try:
                self.canvas.get_tk_widget().pack_forget()
                self.canvas.get_tk_widget().destroy()
                self.canvas = None
            except Exception as e:
                sg.popup(f"error distroying canvas: {e}")
                
        plt.close("all")
        

    def upload_csv(self):
        
        file_path = sg.popup_get_file("select CSV file", file_types=(("CSV Files", "*.csv"),), no_window=True)
        
        if file_path:
            self.file_path = file_path
            self.charts = Charts(self.file_path)
            print("loaded CSV")
            self.current_index = 0
            self.draw_chart()
            
            
    def handle_chart_events(self, event):
        
        if self.charts:
            if event == "-NEXT-":
                self.current_index = (self.current_index + 1) % len(self.charts.chart_keys)
            elif event == "-PREV-":
                self.current_index = (self.current_index - 1) % len(self.charts.chart_keys)
            self.draw_chart()
    
    
    def handle_sub_chart_events(self, event):
        
        if self.charts:
            if event == "-SUB_NEXT-":
                self.current_index = (self.current_index + 1) % len(self.charts.chart_keys)
            elif event == "-SUB_PREV-":
                self.current_index = (self.current_index - 1) % len(self.charts.chart_keys)
            self.draw_chart()
    
    
    def handle_sub2_chart_events(self, event):
        
        if self.charts:
            if event == "-SUB_2_NEXT-":
                self.current_index = (self.current_index + 1) % len(self.charts.chart_keys)
            elif event == "-SUB_2_PREV-":
                self.current_index = (self.current_index - 1) % len(self.charts.chart_keys)
            self.draw_chart()
            
            
    def toggle_visibility(self, state):
        
        if state["hidden"]:
            self.window.un_hide()
            self.draw_chart()
        else:
            self.window.hide()
            if self.canvas:
                self.canvas.get_tk_widget().destroy()
                self.canvas = None
        state["hidden"] = not state["hidden"]
