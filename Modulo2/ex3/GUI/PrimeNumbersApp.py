import sys
import serial
import threading
from utils import file_to_bits, test_burst_channel, test_bsc_channel
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QInputDialog, QMessageBox

arduino_serial = serial.Serial('COM3', 9600)
recording = False

def PrimeNumbersApp():
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle('Prime Numbers App')
    window.setGeometry(100, 100, 600, 400) 

    layout = QVBoxLayout()

    text_edit = QTextEdit()
    layout.addWidget(text_edit)

    def get_positive_integer():
        while True:
            N, ok = QInputDialog.getInt(window, "Input", "Enter a positive integer (N):", min=1)
            if ok and N > 0:
                arduino_serial.write(f"{N}\n".encode())
                text_edit.append(f"Sent N = {N} to Arduino")
                break
            else:
                text_edit.append("Invalid input. Please enter a positive integer.")

    def read_serial_data():
        global recording
        with open("primes.txt", "w") as file:
            while recording:
                if arduino_serial.in_waiting > 0:
                    serial_data = arduino_serial.readline().decode().strip()
                    file.write(serial_data + "\n")
                    text_edit.append(serial_data)
                    app.processEvents() 

    def start_recording():
        global recording
        if start_button.text() == "Start Recording":
            arduino_serial.flushInput() 
            text_edit.clear()  
            start_button.setText("Stop Recording")
            start_button.setStyleSheet("""
                QPushButton {
                    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #FF5733, stop:1 #D23826);
                    border-style: outset;
                    border-radius: 10px;
                    color: white;
                    font: bold;
                    padding: 10px;
                }
                QPushButton:hover {
                    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #D23826, stop:1 #FF5733);
                }
            """) 
            text_edit.append("Recording started...")
            get_positive_integer()
            recording = True
            threading.Thread(target=read_serial_data).start()
        else:
            start_button.setText("Start Recording")
            start_button.setStyleSheet("""
                QPushButton {
                    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #4CAF50, stop:1 #45a049);
                    border-style: outset;
                    border-radius: 10px;
                    color: white;
                    font: bold;
                    padding: 10px;
                }
                QPushButton:hover {
                    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #45a049, stop:1 #4CAF50);
                }
            """) 
            text_edit.append("Recording stopped.")
            recording = False
            show_error_detection_prompt()

    def show_error_detection_prompt():
        reply = QMessageBox.question(window, 'Error Detection', 'Do you want to perform error detection using IP Checksum?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            perform_error_detection()
        text_edit.append("To try again, click the Arduino reset button.")

    def perform_error_detection():
        probability, ok = QInputDialog.getDouble(window, "Input Probability", "Enter the error probability (0-100):", min=0, max=100)
        if not ok:
            text_edit.append("Error detection aborted by user.")
            return
        
        burst_length, ok = QInputDialog.getInt(window, "Input Burst Length", "Enter the burst length:", min=1)
        if not ok:
            text_edit.append("Error detection aborted by user.")
            return
        
        probability /= 100.0 
        bits = file_to_bits("primes.txt")
        burst_test = test_burst_channel(probability, burst_length, bits)
        bsc_test = test_bsc_channel(probability, bits)

        text_edit.append(f"Burst Channel Test: {'Passed' if burst_test else 'Failed'}")
        text_edit.append(f"BSC Channel Test: {'Passed' if bsc_test else 'Failed'}")


    start_button = QPushButton('Start Recording')
    start_button.setStyleSheet("""
        QPushButton {
            background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #4CAF50, stop:1 #45a049);
            border-style: outset;
            border-radius: 10px;
            color: white;
            font: bold;
            padding: 10px;
        }
        QPushButton:hover {
            background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #45a049, stop:1 #4CAF50);
        }
    """)
    start_button.clicked.connect(start_recording)
    layout.addWidget(start_button)

    window.setLayout(layout)
    window.show()
    sys.exit(app.exec_())

PrimeNumbersApp()
arduino_serial.close()
