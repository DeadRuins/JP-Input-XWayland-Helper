import sys
import threading
import keyboard

from PyQt6.QtWidgets import QApplication, QLabel, QLineEdit, QVBoxLayout, QWidget, QPushButton
from PyQt6.QtCore import Qt

class LineEditDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # ラベル
        label_top = QLabel("Welcome to XWayland JP Input Helper!")


        self.text_input = QLineEdit()
        self.text_input.setPlaceholderText("ここに入力...")
        self.text_input.returnPressed.connect(self.copy_to_clipboard)

        # 入力値を表示するためのラベル
        self.result_label_top = QLabel("入力した内容がここに表示されます")


        # コピー用ボタン
        copy_button = QPushButton("コピー")
        copy_button.clicked.connect(self.copy_to_clipboard)

        # レイアウト
        layout = QVBoxLayout()
        layout.addWidget(label_top)
        layout.addWidget(self.text_input)
        layout.addWidget(copy_button)
        layout.addWidget(self.result_label_top)

        self.setLayout(layout)
        self.setWindowTitle("XWayland JP Input Helper (Prototype)") # ウィンドウのタイトル
        self.setFixedSize(600,150) # ウィンドウの位置と大きさ

        #常にウィンドウ上部に表示させる。
        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint)


    def keyPressEvent(self, event):
        # Detect Shift + Tilde (~), which is Shift + ` (backquote)
        if (event.key() == Qt.Key.Key_AsciiTilde or event.key() == Qt.Key.Key_QuoteLeft) and \
           event.modifiers() & Qt.KeyboardModifier.ShiftModifier:
            self.toggle_visibility()

    def toggle_visibility(self):
        if self.isVisible():
            self.hide()
        else:
            self.show()

    def copy_to_clipboard(self):
        text = self.text_input.text()
        QApplication.clipboard().setText(text)
        self.result_label_top.setText(f"クリップボードにコピーしました: {text}")
        self.text_input.clear()


if __name__ == "__main__":
    app = QApplication([])
    demo = LineEditDemo()
    demo.show()
    app.exec()
