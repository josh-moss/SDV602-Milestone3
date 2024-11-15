import matplotlib.pyplot as plt
import PySimpleGUI as sg
import pandas as pd


#------------------------------- MAIN CHART CLASS -------------------------------

class Charts:
    def __init__(self, csv_file):
        
        try:
            self.data = pd.read_csv(csv_file)
            print(f"loaded CSV success: {csv_file}")
            
        except Exception as errcsv:
            print(f"loading CSV error: {errcsv}")
        
        self.charts = {
            "multiple_plots": self.multiple_plots,
            "bar_chart": self.bar_chart,
            "histogram": self.histogram,
            "scatter_plots": self.scatter_plots
        }
        
        self.chart_keys = list(self.charts.keys())
        self.current_index = 0

#-------------------------------   CHARTS   -------------------------------
    
    def multiple_plots(self):
        
        try:
            celsius_min = self.data['value']
            celsius_max = self.data['value']
            
        except Exception as errcsv:
            sg.popup(f"missing column names/ incorrect column names for multiple_plots. {errcsv}")
            return plt.figure()

        fig, ax = plt.subplots()
        ax.set(xlabel='Day', ylabel='Temperature in Celsius', title='Temperature Graph')
        ax.plot(celsius_min, label='Min Temperature', color='blue', marker='o')
        ax.plot(celsius_max, label='Max Temperature', color='red', marker='o')
        ax.legend()
        return fig
    
    def bar_chart(self):
    
        try:
            years = self.data['value']
            visitors = self.data['value']
            
        except Exception as errcsv:
            sg.popup(f"missing column names/ incorrect column names for barchart. {errcsv}")
            return plt.figure()

        plt.bar(years, visitors, color="green")
        plt.xlabel("Years")
        plt.ylabel("Values")
        plt.title("Bar Chart Example")
        return plt.gcf()

    def histogram(self):
        
        try:
            values = self.data['value']
            
        except Exception as errcsv:
            sg.popup(f"missing column names/ incorrect column names. {errcsv}")
            return plt.figure()

        plt.hist(values, bins=20)
        plt.xlabel("Value")
        plt.ylabel("Frequency")
        return plt.gcf()

    def scatter_plots(self):
        
        try:
            x = self.data['value']
            y1 = self.data['value']
            y2 = self.data['value']
            y3 = self.data['value']
            
        except Exception as errcsv:
            sg.popup(f"missing column names/ incorrect column names for scatter_plots. {errcsv}")
            return plt.figure()

        plt.scatter(x, y1)
        plt.scatter(x, y2, marker='v', color='r')
        plt.scatter(x, y3, marker='^', color='m')
        plt.title('Scatter Plot Example')
        return plt.gcf()
