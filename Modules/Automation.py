from playwright.sync_api import sync_playwright
from datetime import datetime

class Automation:
    def __init__(self, registers):
        self.browser= sync_playwright().start().chromium.launch(headless=False)
        self.mainPage= self.browser.new_page()
        self.mainPage.goto("https://gstechdeveloper.github.io/CadastroFuncionarios/#/")
        
        for reg in registers:
            self.fillFuncName(reg["Nome"])
            self.fillFuncEmail(reg["Email"])
            self.fillFuncDtNasc(reg["Data Nascimento"])
            self.fillFuncSex(reg["Sexo"])
            self.fillFuncDef(reg["Deficiencia"])
            self.submitForm()

        input("Preenchimento finalizado. Pressione qualquer tecla para fechar...")

    def fillFuncName(self, name):
        self.FuncName= self.mainPage.get_by_placeholder("Nome do Funcionário")
        self.FuncName.fill(name)
    def fillFuncEmail(self, email):
        self.FuncEmail= self.mainPage.get_by_placeholder("E-mail do Funcionário")
        self.FuncEmail.fill(email)
    def fillFuncDtNasc(self, data_br):
        data_iso = datetime.strptime(data_br, "%d/%m/%Y").strftime("%Y-%m-%d")
        self.FuncDtNasc= self.mainPage.locator("input[type='date']")
        self.FuncDtNasc.fill(data_iso)
    def fillFuncSex(self, sexo):
        self.FuncSex= self.mainPage.locator("select")
        self.FuncSex.select_option(sexo)
    def fillFuncDef(self, deficiencia):
        deficiencia= bool(deficiencia)
        self.FuncDef= self.mainPage.locator("input[type='checkbox']")
        if(deficiencia and not(self.FuncDef.is_checked())):
            self.FuncDef.check()
    def submitForm(self):
        self.mainPage.locator("button").click()
        self.FuncName.clear()
        self.FuncEmail.clear()
        self.FuncDtNasc.clear()
        self.FuncSex.select_option(index=0)
        if(self.FuncDef.is_checked()):
            self.FuncDef.uncheck()