import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
import sqlite3

class CryptoViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Visualizador de Criptomoedas")
        self.setGeometry(100, 100, 1000, 400)

        # Layout principal
        self.central_widget = QWidget()
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)

        # Criar tabela
        self.table_widget = QTableWidget()
        self.layout.addWidget(self.table_widget)

        # Carregar dados
        self.load_data()

    def load_data(self):
        conn = sqlite3.connect("cryptos.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM cryptos")
        data = cursor.fetchall()
        columns = [description[0] for description in cursor.description]
        conn.close()

        # Configurar tabela
        self.table_widget.setRowCount(len(data))
        self.table_widget.setColumnCount(len(columns))
        self.table_widget.setHorizontalHeaderLabels(columns)

        # Preencher tabela
        for i, row in enumerate(data):
            for j, value in enumerate(row):
                self.table_widget.setItem(i, j, QTableWidgetItem(str(value)))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CryptoViewer()
    window.show()
    sys.exit(app.exec())
