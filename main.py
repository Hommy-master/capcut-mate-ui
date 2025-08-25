#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
跨平台最小 PyQt5 窗口示例
支持 Windows / Linux / macOS
运行：
    python main.py
"""
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget, QPushButton


class SimpleWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 跨平台示例")
        self.resize(360, 240)

        # 主布局
        layout = QVBoxLayout(self)

        # 标签
        self.label = QLabel("你好，PyQt5！", self)
        self.label.setAlignment(Qt.AlignCenter)

        # 按钮
        self.button = QPushButton("点我", self)
        self.button.clicked.connect(self.on_click)

        layout.addWidget(self.label)
        layout.addWidget(self.button)

    def on_click(self):
        self.label.setText("按钮被点了！")


if __name__ == "__main__":
    # 适配高清屏（可选）
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)

    app = QApplication(sys.argv)
    w = SimpleWindow()
    w.show()
    sys.exit(app.exec_())
