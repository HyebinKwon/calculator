# ch 5.2.1 main.py

import os
import sys
from ui import View
from ctrl import Control
from PyQt5.QtWidgets import QApplication

# PyQt5의 Qt 플랫폼 플러그인 경로를 지정합니다.
qt_plugin_path = r'C:\calculator\platforms'  # Qt 플랫폼 플러그인 경로
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = qt_plugin_path

def main():
    calc= QApplication(sys.argv)
    app=QApplication(sys.argv)
    view=View()
    Control(view=view)
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
