import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO   # GPIO Bibliothek importieren
import time               # Modul time importieren


url = "broker.mqttdashboard.com"

topic = "haw/dmi/mt/its/petcare"

P = 5
GPIO.setmode(GPIO.BOARD)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
p = GPIO.PWM(15, 50)
p.start(2.5)

def on_connect(client,userdata,flags,rc):

	print("Connected with result code "+str(rc))

	client.subscribe(topic)



def on_message(client,userdata,msg):

	payload = msg.payload.decode('utf-8')

	if payload == '0':
		print("Schalte Licht aus")

	elif payload == '1':
		print("Holla is workin mahn")
		GPIO.output(5, False)	
		
	elif payload == '2':
		GPIO.output(5, True)
		
	elif payload == '4':
		try:
			while True:
				p.ChangeDutyCycle(5)
				time.sleep(0.1)
				p.ChangeDutyCycle(7.5)
				time.sleep(0.1)
				p.ChangeDutyCycle(10)
				time.sleep(0.1)
				p.ChangeDutyCycle(12.5)
				time.sleep(0.1)
				p.ChangeDutyCycle(10)
				time.sleep(0.1)
				p.ChangeDutyCycle(7.5)
				time.sleep(0.1)
				p.ChangeDutyCycle(5)
				time.sleep(0.1)
				p.ChangeDutyCycle(2.5)
				time.sleep(0.1)
		except KeyboardInterrupt:
			p.stop()
			GPIO.cleanup()
		
	else:
		print("unbekannter Befehl")




client = mqtt.Client()

client.on_connect = on_connect

client.on_message = on_message



client.connect(url,1883,60)

client.loop_forever()      