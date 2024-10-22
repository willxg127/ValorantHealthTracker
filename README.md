# Valorant Health Tracker

A unique hardware-software integration project that tracks player health in Valorant and provides physical feedback through Arduino-controlled hardware. The system uses optical character recognition (OCR) to monitor in-game health status in real-time and triggers a servo motor response when health changes are detected.

## Features

- Real-time health monitoring in Valorant
- OCR-based screen capture and text recognition
- Bluetooth communication between Python and Arduino
- Physical feedback through servo motor movement
- Automatic health status tracking and reset

## Hardware Requirements

- Arduino board (Uno or similar)
- Servo motor
- HC-06 Bluetooth module
- Jumper wires
- Power supply for Arduino

## Software Requirements

- Python 3.x
- OpenCV
- PyTesseract
- PyAutoGUI
- Pygame
- PySerial
- Arduino IDE

## Installation

1. **Install Required Python Packages:**
```bash
pip install opencv-python
pip install pytesseract
pip install pyautogui
pip install pygame
pip install pyserial
```

2. **Install Tesseract OCR:**
   - Download and install Tesseract OCR from the [official GitHub repository](https://github.com/UB-Mannheim/tesseract/wiki)
   - Add Tesseract to your system PATH or update the path in the code:
```python
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
```

3. **Set up Arduino:**
   - Install the Arduino IDE
   - Connect the hardware components:
     - Connect servo motor to pin 7
     - Connect HC-06 Bluetooth module to pins 10 (RX) and 11 (TX)
     - Connect power pin to pin 3
   - Upload the Arduino code to your board

## Hardware Setup

```
Arduino Connections:
- Servo Motor → Pin 7
- HC-06 (RX) → Pin 10
- HC-06 (TX) → Pin 11
- Power Pin → Pin 3
```

## Usage

1. Ensure your Bluetooth module is paired with your computer
2. Update the COM port in `ocr.py` to match your system:
```python
port = "COM5"  # Change this to your COM port
```
3. Start Valorant and ensure the health display is visible
4. Run the Python script:
```bash
python ocr.py
```
5. The program will now monitor your in-game health and trigger the servo when health drops

## How It Works

1. The Python script continuously captures a specific region of your screen where the health value is displayed
2. PyTesseract performs OCR on the captured image to extract the health value
3. When a health drop is detected, the script sends a signal via Bluetooth to the Arduino
4. The Arduino receives the signal and triggers the servo motor movement
5. The system automatically resets when health returns to 100

## Troubleshooting

- Ensure Tesseract OCR is properly installed and the path is correctly set
- Check that the COM port matches your Bluetooth module's port
- Verify the screen capture region matches your game's health display location
- Make sure all hardware connections are secure
- Check that the Bluetooth module is properly paired with your computer

## Contributing

Feel free to fork this project and submit pull requests for any improvements you make. Some areas for potential enhancement:
- Support for different game resolutions
- Customizable screen capture regions
- Additional physical feedback mechanisms
- Improved OCR accuracy

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) for text recognition
- The Valorant community for inspiration
