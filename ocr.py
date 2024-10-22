import serial
import cv2
import pytesseract
import pyautogui
import numpy
import time
import pygame
import os   

pygame.init()

sound = pygame.mixer.Sound("airsoft shots.mp3")

port = "COM5"
baud_rate = 9600
ser = serial.Serial(port, baud_rate)
command = 'on'
    
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
healthValues = []
lowestHealth = 100

while True:
    if len(healthValues) == 0:
        pass
    else:
        lowestHealth = min(healthValues)
    
    #select region of screen
    image = pyautogui.screenshot(region=(575,1000,75,50))
    image = cv2.cvtColor(numpy.array(image), cv2.COLOR_RGB2BGR)

    #convert image to grey scale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    #apply otsu thresholding
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    #run OCR using pytesseract
    text = pytesseract.image_to_string(thresh, lang = 'eng', 
    config='--psm 11')
    text = text.replace("\n", " ")

    #test for health drop
    try:
        if int(text) <= 100 and int(text) > 0:
            healthValues.append(int(text))
        print(healthValues[-1])
        if min(healthValues) < lowestHealth:
            ser.write("ON".encode())
            time.sleep(2)
            #sound.play()
        if healthValues[-1] == 100 and healthValues[-2] == 100 and healthValues[-3] == 100:
            healthValues.clear()
    except:
        pass

                
    cv2.imshow("Screenshot",image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print(healthValues)
        break

# Release camera and close window
cv2.destroyAllWindows()