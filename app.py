import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from engine.mainwindow_qt import Ui_MainWindow
from engine import fipe_client

class FipeApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.buttonBrands.clicked.connect(self.listBrands)
        self.buttonModels.clicked.connect(self.listModels)
        self.buttonYears.clicked.connect(self.listYears)
        self.buttonPrice.clicked.connect(self.listPrice)
    
    def list_att(self, title, items):
        "Limpa e adiciona novos intems"
        self.listWidget.clear()
        self.listWidget.addItem(f" --- {title} --- ")
        self.listWidget.addItems(items)
    
    def listBrands(self):
        vehicle_type = self.vehicle_brands.currentText()

        if not vehicle_type:
            QMessageBox.warning(self, "Atenção", "Escolha o tipo")
            return

        try:
            self.listWidget.clear()
            self.listWidget.addItem("Buscando tipos...")
            QApplication.processEvents()

            result = fipe_client.get_brands(vehicle_type)
                
                # nesse trecho realizo uma verificação : se o resultado é uma lista
            if isinstance(result, list) and len(result) > 0:
                list_format = [f"{i['name']} (Cod: {i['code']})" for i in result]
                self.list_att("Marcas encontradas", list_format)
            elif "error" in result:
                self.list_att("ERRO", [result['message']])
            else:
                self.list_att('Aviso', ["Nenhum resultado."])
        except Exception as e:
            QMessageBox.critical(self, 'Erro', str(e))

    def listModels(self):
        vehicle_type = self.vehicle_models.currentText()
        brand_id = self.codeBrands.text()

        if not (vehicle_type and brand_id):
            QMessageBox.warning(self, "Atenção", "Preencha os campos.")
            return
        
        try:
            self.listWidget.clear()
            self.listWidget.addItem("Buscando modelos.")
            QApplication.processEvents()

            result = fipe_client.get_models(vehicle_type, int(brand_id))

            if isinstance(result, list) and len(result) > 0:
                list_format = [f"{i['name']} (Cod: {i['code']})" for i in result]
                self.list_att("Modelos encontrados", list_format)
            elif "error" in result:
                self.list_att("ERRO", [result['message']])
            else:
                self.list_att('Aviso', ["Nenhum resultado."])
        except Exception as e:
            QMessageBox.critical(self, 'Erro', str(e))

    def listYears(self):
        vehicle_type = self.vehicle_years.currentText()

        brand_id = self.codeBrands_model.text()
        model_id = self.codeModels.text()

        if not (brand_id and model_id):
            QMessageBox.warning(self, "Atenção", "Preencha o codigo da Marca e do Modelo")
            return
        
        try:
            self.listWidget.clear()
            self.listWidget.addItem("Buscando anos...")
            QApplication.processEvents()

            result = fipe_client.get_years(vehicle_type, int(brand_id), int(model_id))

            if isinstance(result, list) and len(result) > 0:
                list_format = [f"{i['name']} (Cód: {i['code']})" for i in result]
                self.list_att("Anos encontrados", list_format)
            elif "error" in result:
                self.list_att("ERRO", [result['message']])
            else:
                self.list_att("Aviso", ["Nenhum resultado encontrado"])
            
        except Exception as e:
            QMessageBox.critical(self, "Erro", str(e))
    
    def listPrice(self):
        vehicle_type = self.vehicle_price.currentText()
        brand_id = self.codeBrands_price.text()
        model_id =  self.codeModels_price.text()
        year_id = self.codeYears.text()

        if not (brand_id and model_id and year_id):
            QMessageBox.warning(self, "Atencção", "Preencha os campos.")
            return
        
        try:
            self.listWidget.clear()
            self.listWidget.addItem("Buscando o preço.")
            QApplication.processEvents()

            data = fipe_client.get_price(vehicle_type, int(brand_id), int(model_id), year_id)

            # pequeno teste de resultado
            print("Retorno: ", data)

            if "error" in data:
                self.list_att("ERRO", [str(data)])
            else:
                details = [
                    f"Veiculo: {data.get('model')}",
                    f"Marca: {data.get('brand')}",
                    f"Ano: {data.get('modelYear')}",
                    f"Combustivel: {data.get('fuel')}",
                    f"Código Fipe: {data.get('codeFipe')}",
                    f"Mês Ref: {data.get('referenceMonth')}",
                    f"-----------------------------------",
                    f"PREÇO: {data.get('price')}"
                ]
                self.list_att('Preço Tabela Fipe', details)
        except Exception as e:
            QMessageBox.critical(self, "Erro", str(e))
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FipeApp()
    window.show()
    sys.exit(app.exec())