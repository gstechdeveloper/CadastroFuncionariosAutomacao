import pandas as pd
from Modules.Automation import *

class App:
    def __init__(self):
        self.registers= []
        self.automation= Automation(self.readRegister())
    def readRegister(self):
        arquivo= pd.read_csv("./Registros.csv", sep=";")
        for i in range(0, len(arquivo)):
            self.registers.append(arquivo.iloc[i].to_dict())

        return self.registers


App()