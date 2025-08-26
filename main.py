import sys
from PySide6.QtWidgets import QApplication, QLabel, QWidget
from PySide6.QtGui import QIcon


def main():
    app = QApplication(sys.argv)  # 创建应用实例
    window = QWidget()           # 创建主窗口
    window.setWindowTitle("剪映小助手")
    window.resize(800, 600)

    # 设置窗口图标
    icon = QIcon("res/logo.png")  # 图标放在项目根目录
    window.setWindowIcon(icon)

    label = QLabel("欢迎使用剪映小助手！", window)
    label.setGeometry(50, 50, 200, 30)  # 设置标签位置和大小

    window.show()               # 显示窗口
    sys.exit(app.exec())        # 启动事件循环

if __name__ == "__main__":
    main()