import time
import json
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QLineEdit
from PyQt6.QtCore import QTimer


class Timer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pomodoro Timer")
        self.setGeometry(100, 100, 400, 500)
        self.start = QPushButton("Start")
        self.pause = QPushButton("Pause")
        self.reset = QPushButton("Reset")
        self.time = QLabel("25:00")
        self.work_or_break = QLabel("")
        self.sessions_label = QLabel("Sessions: 0")
        try:
            with open("pomodoro_sessions.txt", "r") as file:
                self.sessions_count = int(file.read())
                self.sessions_label.setText(f"Sessions: {self.sessions_count}")
        except:
            self.sessions_count = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.tick)
        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()



        vbox.addWidget(self.work_or_break)
        vbox.addWidget(self.time)
        vbox.addWidget(self.sessions_label)
        vbox.addWidget(self.start)
        vbox.addWidget(self.pause)
        vbox.addWidget(self.reset)
        self.setLayout(vbox)

        self.work_or_break.setText("Work")

        self.start.setObjectName("Start")
        self.pause.setObjectName("Pause")
        self.reset.setObjectName("Reset")

        self.setStyleSheet("""
            QLabel{
                background-color: rgb(200, 200, 200);
                font-size: 100px
            }
            QPushButton{
                font-size: 40px;
                font-family: Arial;
                padding: 15px 75px;
                margin: 25px;
                border: 3px solid;
                border-radius: 15px;
            }
            QPushButton#Start{
                background-color: rgb(111, 196, 87)
            }
            QPushButton#Pause{
                background-color: rgb(80,199,199)
            }
            QPushButton#Reset{
                background-color: rgb(179, 12, 4)
            }
            QLabel{
                font-family: Iosevka Charon Mono
            }
            QLineEdit{
                font-size: 30px;
            }
            """)

        self.start.clicked.connect(self.start1)
        self.pause.clicked.connect(self.pause1)
        self.reset.clicked.connect(self.reset1)

    def start1(self):
        self.time_left = 25 * 60
        self.is_work = True
        self.timer.start(1000)

    def reset1(self):
        self.timer.stop()
        self.time_left = 25 * 60
        self.is_work = True
        self.work_or_break.setText("Work")
        self.time.setText("25:00")

    def pause1(self):
        self.timer.stop()

    def tick(self):
        self.time_left -= 1
        minutes = self.time_left // 60
        seconds = self.time_left % 60
        time_string = f"{minutes:02d}:{seconds:02d}"
        self.time.setText(time_string)
        if self.time_left < 0:
            if self.is_work:
                self.is_work = False
                self.work_or_break.setText("Break")
                self.time_left = 5 * 60
            else:
                self.is_work = True
                self.work_or_break.setText("Work")
                self.time_left = 25 * 60
                self.sessions_count += 1
                self.sessions_label.setText(f"Sessions: {self.sessions_count}")

                with open("pomodoro_sessions.txt", "w") as file:
                    file.write(str(self.sessions_count))

            return

if __name__ == "__main__":
    app = QApplication(sys.argv)
    timer = Timer()
    timer.show()
    sys.exit(app.exec())