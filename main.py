from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtGui import QIcon
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Logshine (В РАЗРАБОТКЕ)")
                
        self.setWindowIcon(QIcon("icon.png"))
        
        self.setGeometry(300, 300, 400, 300)

        self.setCentralWidget(QLabel("Привет, мир!", parent=self.window))


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())