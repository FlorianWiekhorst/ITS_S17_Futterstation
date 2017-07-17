import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO   # GPIO Bibliothek importieren
import time               # Modul time importieren
import base64
import subprocess
import threading
import os
try:
    import thread
except ImportError:
    import _thread as thread #Py3K changed it.

# url = "diginet.mt.haw-hamburg.de"
url = "broker.mqttdashboard.com"

topic = "haw/dmi/mt/its/petcare"

P = 5
GPIO.setmode(GPIO.BOARD)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
p = GPIO.PWM(15, 50)
p.start(2.5)

class myThread (threading.Thread):
	def __init__(self, threadID, name, counter):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.counter = counter
	def run(self):
		print ('Starting' + self.name)
		sendPic()
		print ("Exiting" + self.name)

def on_connect(client,userdata,flags,rc):
	print("Connected with result code "+str(rc))
	client.subscribe(topic)

def on_publish(client, userdata, mid):
	print("is printed")

def on_message(client,userdata,msg):

	payload = msg.payload.decode('utf-8')

	if payload == '00':
		print("Schalte Licht aus")
		try:
			p.ChangeDutyCycle(7.5)
			time.sleep(0.7)
			p.ChangeDutyCycle(2.5)
			time.sleep(0.7)
			p.ChangeDutyCycle(7.5)
			time.sleep(0.7)
			p.ChangeDutyCycle(2.5)
		except KeyboardInterrupt:
			p.stop()
			GPIO.cleanup()

	elif payload == '01':
		print("Holla is workin mahn")
		try:
			p.ChangeDutyCycle(7.5)
			time.sleep(0.7)
			p.ChangeDutyCycle(2.5)
			time.sleep(0.7)
			p.ChangeDutyCycle(7.5)
			time.sleep(0.7)
			p.ChangeDutyCycle(2.5)
			time.sleep(0.7)
			p.ChangeDutyCycle(7.5)
			time.sleep(0.7)
			p.ChangeDutyCycle(2.5)
		except KeyboardInterrupt:
			p.stop()
			GPIO.cleanup()

	elif payload == '10':
		GPIO.output(5, True)
		time.sleep(2)
		GPIO.output(5,False)


	elif payload == '11':
		GPIO.output(5, True)
		time.sleep(4)
		GPIO.output(5,False)

	else:
		print("unbekannter Befehl")


def sendPic():
	try:
		while True:
			command="fswebcam image.jpg --no-banner"
			os.system(command)
			#subprocess.Popen(command,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
			with open("image.jpg", "rb") as image_file:
				encoded_string = base64.b64encode(image_file.read())
			client.publish(topic,encoded_string,qos=2,retain=False)
			time.sleep(1)
	except KeyboardInterrupt:
		print("interrupted")




thread1 = myThread(1, "Image_Thread", 1)
thread1.daemon=True
thread1.start()

client = mqtt.Client()

client.on_connect = on_connect

client.on_message = on_message

client.on_publish = on_publish
# client.username_pw_set("haw",password="schuh+-0")
client.connect(url,1883,60)

client.loop_forever()
