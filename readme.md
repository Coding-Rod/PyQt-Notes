# PyQt5

## Install

~~~bash
sudo apt-get install python3-pyqt5
sudo apt-get install qtcreator pyqt5-dev-tools
sudo apt-get install qttools5-dev-tools
~~~

## Convert to python

~~~bash
python -m PyQt5.uic.pyuic -x [FILENAME].ui -o [FILENAME].py
~~~

## Steps

1. Convert to construct
2. Modificar UI
3. Position components
4. Add css to attributes
5. QMessageBox
6. Read Css File

## QMessageBox

~~~python3
from PyQt5.QtWidgets import QMessageBox

msg = QMessageBox()
msg.setIcon(QMessageBox.Information)
msg.setText(f"Text: {self.lineEdit.text()}\n"+f"Checkbox: {self.checkBox.isChecked()}")
# msg.setInformativeText('More information')
msg.setWindowTitle("Información")
msg.exec_()
~~~
