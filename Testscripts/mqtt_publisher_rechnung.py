import paho.mqtt.publish as publish
 
MQTT_SERVER = "localhost"
MQTT_PATH = "test_channel"
 
dauer=1
while dauer==1:
	d=input("Bei weiter bitte 1 eingeben.Bei abbruch nach der Runde bitte 2 eingeben:")
	b=int(d)
	dauer=b

	m=input("Eingabe des Wertes 1 der Rechnung:")
	wert1=int(m)

	y=input("Eingabe des Wertes 2 der Rechnung:")
	wert2=int(y)

	z=input("Eingabe des Rechenzeichens (1=+, 2=-, 3=*, 4=/):")
	rechen=int(z)


	if rechen==1:
        	ergebnis= wert1 + wert2 
            print("Der Broker hat das Ergebnis erhalten")
        	publish.single(MQTT_PATH,ergebnis,hostname=MQTT_SERVER)
            
	elif rechen==2:
        	ergebnis=wert1-wert2
            print("Der Broker hat das Ergebnis erhalten")
        	publish.single(MQTT_PATH,ergebnis,hostname=MQTT_SERVER)
            
	elif rechen==3:
        	ergebnis= wert1*wert2
            print("Der Broker hat das Ergebnis erhalten")
        	publish.single(MQTT_PATH,ergebnis,hostname=MQTT_SERVER)
            
	elif rechen==4:
        	ergebnis=wert1/wert2
            print("Der Broker hat das Ergebnis erhalten")
        	publish.single(MQTT_PATH,ergebnis,hostname=MQTT_SERVER)
            
	else:
        	print("Eingabe ungueltig. Bitte wiederholen")
        




