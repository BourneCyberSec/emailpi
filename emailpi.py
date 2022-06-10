##Declare Modules for sending emails, detecting on pir on gpio and sending images over emails
import picamera
from time import sleep
from gpiozero import MotionSensor
import numpy as np
from datetime import datetime
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

##Config PiCamera as camera
camera = picamera.PiCamera()
pir = MotionSensor(4)

##Config email information
gmail_user = "raspberrypi@gmail.com"
gmail_pwd = "raspberrpipassword"
recipient = "st1075213@craven-college.ac.uk"
subject = "Security Alert"
text = "Movement Detected"

##Defing what to do if motion is detectedd
def Detection_System()
    gmail_user = "raspberrypi@gmail.com"
    gmail_pwd = "raspberrpipassword"
    to = "st1075213@craven-college.ac.uk"
    subject = "Security Alert"
    text = "Movement Detected"
    image = "home/pi/capture-1.img"


##Detect movement
while True:
    if pir.motion_detected:
        camera.resolution = (1024, 768)
        camera.brightness = 50
        print("Motion Detected")
        camera.capture("/home/pi/capture-%.img" %1)

##Set email arguments
        msg = MIMEMultipart()
        msg['From'] = gmail_user
        msg['To'] = recipient
        msg['Subject'] = subject
        msg.attach(MIMEText(text))

        stage = MIMEBase('application, 'octet-stream')
        filename = os.path.basename(capture)
        attachment = open(capture, "rb")
        staged01 = MIMEBase('application', octet-stream)
        staged01.set_payload((attachment).read())
        encoders.encode_base64(staged01)
        staged01.add_header('Content-Disposition', 'attatchment', filename = os.path.basename(capture))
        msg.attach(staged01)

##Configure email server host and port
        with smtplib.SMTP_SSL('smtp.gmail.com', '465') as email:
            email.set_debuglevel(False)
            email.login(gmail_user, gmail_pwd)

##Send email to recipient
            text = msg.as_string()
            print(to)
            email.sendmail(gmail_user, gmail_pwd)
            text = msg.as_string()
            print(to)
            email.sendmail(gmail_user, to, text)
            email.quit()
            print("Message Sent")

##Start listening on Pir Sensor
while True:
    Detection_System()