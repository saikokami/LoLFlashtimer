#Failed project to fetch current timer in a game

import os
import cv2
import pytesseract
import pyscreenshot as ImageGrab
from datetime import datetime

pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

def addToClipBoard(text):
    command = 'echo ' + text.strip() + '| clip'
    os.system(command)

lane="top"

while True:
    #Wait untill keypress
    input("waiting for keypress....")
   
    #Get png to get time in game
    im=ImageGrab.grab(bbox=(1855,3,1905,25))
    im.show()
    im.save('screen.png')

    #Convert img to text
    img = cv2.imread('screen.png')
    date = pytesseract.image_to_string(img)
    print(date)
    #Convert string to datetime
    date_time=datetime.strptime(date,'%MM:%SS')
    print ("The date is", date_time)
        
    addToClipBoard(lane+ " has flash in minutes")







