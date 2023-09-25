from asyncio import sleep
import pyautogui
import openpyxl
import time
import clipboard
import pandas as pd
import time
from datetime import datetime
import shlex
import re
import io


class Automator:

    def __init__(self):
        self.inicio = None
        self.fin = None

    def log_in(self):
        pyautogui.press('winleft')
        pyautogui.sleep(2)
        pyautogui.write('mapex bp10')
        pyautogui.sleep(2)
        pyautogui.click(x=237, y=477)
        pyautogui.sleep(2)
        pyautogui.press('enter')
        while True:
            location = pyautogui.locateOnScreen(
                "transaction_load_comprobation/load_app.PNG", confidence=0.9)
            if location is not None:
                print("Transaction complete detected!")
                break
            print("Waiting for transaction to complete...")
            time.sleep(1)

        pyautogui.click(x=866, y=559)
        pyautogui.sleep(2)
        pyautogui.write('Aciturri', interval=0.05)
        pyautogui.hotkey('ctrl', 'alt', '2')
        pyautogui.write('2024_', interval=0.05)
        pyautogui.sleep(2)
        pyautogui.press('enter')

        while True:
            location = pyautogui.locateOnScreen(
                'transaction_load_comprobation/load_log_in.PNG', confidence=0.9)
            if location is not None:
                print("Transaction complete detected!")
                break
            print("Waiting for transaction to complete...")
            time.sleep(2)

    def select_range(self):
        self.inicio, self.fin = input("Escriba la fecha de inicio en formato dd/mm/yyyy :"), input(
            "Escriba la fecha de inicio en formato dd/mm/yyyy :")

        if not self.check_date(self.inicio) or not self.check_date(self.fin):
            print("Una o ambas fechas ingresadas no son válidas. Por favor, asegúrese de que el formato es correcto y la fecha introducida es válida e intentelo de nuevo .")
        else:
            return self.inicio, self.fin

    def check_date(self, date):
        if len(date) != 10:
            return False
        day, month, year = date.split("/")

        if not (day.isdigit() and month.isdigit() and year.isdigit()):
            return False

        day, month, year = int(day), int(month), int(year)

        if not (1 <= day <= 31):
            return False
        if not (1 <= month <= 12):
            return False
        if not (1000 <= year <= 9999):
            return False
        return True

    def insert_date(self):
        day, month, year = self.inicio.split("/")
        day_1, month_1, year_1 = self.fin.split("/")

        pyautogui.click(x=67, y=133)
        pyautogui.write(day)
        pyautogui.press('right')
        pyautogui.write(month)
        pyautogui.press('right')
        pyautogui.write(year)

        pyautogui.click(x=229, y=133)
        pyautogui.write(day_1)
        pyautogui.press('right')
        pyautogui.write(month_1)
        pyautogui.press('right')
        pyautogui.write(year_1)

    def get_valores_and_hora(self):
        pyautogui.click(x=124, y=14)
        pyautogui.sleep(2)
        pyautogui.click(x=124, y=75)
        pyautogui.sleep(1)
        self.select_range()
        self.insert_date()
        pyautogui.click(x=706, y=130)
        pyautogui.sleep(2)
        pyautogui.click(x=572, y=205)
        pyautogui.sleep(2)
        # Botón de refrescar
        pyautogui.click(x=1870, y=87)  # este es el botón de cargar
        while True:
            location = pyautogui.locateOnScreen(
                'transaction_load_comprobation/load_transaction_1.png', confidence=0.85)
            if location is not None:
                print("Transaction complete detected!")
                break
            print("Waiting for transaction to complete...")
            time.sleep(1)

    # Seleccion DMG
        pyautogui.click(x=1828, y=129)
        pyautogui.sleep(2)
        pyautogui.click(x=1798, y=204)
        while True:
            location = pyautogui.locateOnScreen(
                'transaction_load_comprobation/load_transaction_2.png', confidence=0.95)
            if location is not None:
                print("Transaction complete detected!")
                break
            print("Waiting for transaction to complete...")
            time.sleep(1)

        pyautogui.sleep(2)
        self.copia_pegar()
        self.data_valor_hora = self.copied_data

    def get_htas(self):
        pyautogui.click(x=1774, y=134)
        pyautogui.sleep(2)
        pyautogui.click(x=1773, y=251)
        pyautogui.sleep(2)
        pyautogui.click(x=1867, y=75)
        pyautogui.sleep(2)
        while True:
            location = pyautogui.locateOnScreen(
                'transaction_load_comprobation/load_transaction_3.png', confidence=0.85)
            if location is not None:
                print("Transaction comppñete detected")
                break
            print("waiting for transaction to complete...")

        self.copia_pegar()
        self.data_htas = self.copied_data

    def get_ofs(self):
        pyautogui.moveTo(x=54, y=16)
        pyautogui.sleep(2)
        pyautogui.click(x=54, y=16)
        pyautogui.sleep(2)
        pyautogui.click(x=130, y=56)
        pyautogui.sleep(2)
        pyautogui.click(x=272, y=59)
        pyautogui.sleep(2)
        self.insert_date()
        pyautogui.sleep(4)
        pyautogui.click(x=471, y=127)
        pyautogui.sleep(2)
        pyautogui.click(x=442, y=173)
        pyautogui.sleep(2)
        pyautogui.click(x=1869, y=89)
        pyautogui.sleep(2)
        pyautogui.click(x=1875, y=121)
        pyautogui.sleep(2)
        pyautogui.click(x=1815, y=206)
        pyautogui.sleep(4)

        self.copia_pegar()
        self.data_ofs = self.copied_data

    def copia_pegar(self):
        pyautogui.rightClick(981, 333)
        pyautogui.sleep(2)
        pyautogui.click(x=981, y=719)
        pyautogui.sleep(5)
        clipboard.copy('')
        pyautogui.click(x=200, y=319)
        pyautogui.sleep(2)
        pyautogui.rightClick(981, 333)
        pyautogui.sleep(2)
        pyautogui.click(x=981, y=719)
        pyautogui.sleep(5)
        pyautogui.rightClick(444, 312)
        pyautogui.sleep(5)
        pyautogui.click(x=464, y=561)
        time.sleep(5)
        self.copied_data = str(clipboard.paste())

    def valor_y_hora_to_df(self):
        # reemplazamos las comas que van seguidas de tres dígiutos por un punto y esos mismos tres dígitos
        cleaned_data = re.sub(r',(\d{3})', r'.\1', self.data_valor_hora)
        # creamos un objeto que representa un archivo de memoria
        buffer = io.StringIO(cleaned_data)
        df = pd.read_csv(buffer, delimiter='\t', header=None)
        df.columns = ['Process', 'Type', 'Load', 'Date',
                      'Value1', 'Value2', 'Value3', 'Value4']
        cols_to_replace = ['Value2', 'Value3']
        df[cols_to_replace] = df[cols_to_replace].apply(
            lambda x: x.str.replace(',', '.').astype(float))
        df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y %H:%M:%S')
        self.data_valor_hora = df[['Date', 'Value1']]
        #self.data_valor_hora.to_csv('valor_hora_grande.csv', index =False)

    def hora_y_hta_to_df(self):
        cleaned_data = self.data_htas.replace('\n', '').replace('\t', ',')
        buffer = io.StringIO(cleaned_data)
        df = pd.read_csv(buffer, header=None)
        # estamos cogiendo todas las filas de las columnas 3 y 8
        self.data_htas = df.iloc[:, [3, 8]]
        # damos nombre a las columnas
        self.data_htas.columns = ['Date', 'Herramienta']
        self.data_htas['Herramienta'] = self.data_htas['Herramienta'].str.extract(
            r'-toolIdent (\w+)')
        #self.data_htas.to_csv('htas_grande.csv', index= False)

    def of_to_df(self):
        col_names = ['Día Productivo', 'Turno', 'Máquina', 'OF', 'Cod.Operación', 'cod_producto', 'desc_producto','operación','inicio', 'Fin', 'Num OFs', 'Tiempo Plan.', 'Tiempo Plan.Proceso', 'Tiempo Real', 'Sub Área']
        self.data_ofs = pd.read_csv(io.StringIO(self.data_ofs.replace('\r', '\n')), delimiter='\t', header=None, names = col_names, index_col=0)
        #self.data_ofs.to_csv('ofs_grande.csv', index= False)

    def run(self):
        self.log_in()
        self.get_valores_and_hora()
        self.valor_y_hora_to_df()
        self.get_htas()
        self.hora_y_hta_to_df()
        self.get_ofs()
        self.of_to_df()
