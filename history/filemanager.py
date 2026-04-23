import json
import datetime
import os

class calculator_history:
    
    def __init__(self, file="history.json"):
        self.file = file
        self.load_history()

    def load_history(self):
        #Loading the history from a json file
        if os.path.exists(self.file):
            with open(self.file, "r") as f:
                self.historial = json.load(f)

        else:
            self.historial = []

    #Saving the calc in history.json
    def save(self):
        with open(self.file, "w") as f:
            json.dump(self.archivo, f, indent=2)

    def add_calc(self, expression, result):
        #Adding a calc in this shit
        calc = {
            "expression": expression,
            "result": result,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.historial.append(calc)
        self.save()

    def get_historial(self):
        return self.historial

    def clean(self):
        self.historial = []
        self.save()

    def last_num(self, n=5):
        return self.historial[-n:] if self.historial else []


