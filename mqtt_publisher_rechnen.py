#-*- coding:utf-8 -*-
import paho.mqtt.publish as publish

MQTT_SERVER = "localhost"
MQTT_PATH = "test_channel"


dauer=1
while dauer==1:

    g=input("Wollen Sie das Programm beenden?")
    ab=str(g)
    

    if ab in ['j','y','ja','yes','ye','Ja']:
        break
        dauer=0
    else:
        m=input("Eingabe des Wertes 1 der Rechnung:")

        try:
            wert1=int(m)
        except:
            print("Der Eingegebene Wert ist falsch1")
            continue
        
        y=input("Eingabe des Wertes 2 der Rechnung:")

        try:
            wert2=int(y)
        except:
            print("Der Eingegebene Wert ist falsch!")
            continue

        z=input("Eingabe des Rechenzeichens (1=+, 2=-, 3=*, 4=/):")

        try:
            rechen=int(z)
        except:
            print("Bitte beachten Sie die Bedeutung der Zaheln für die Rechenzahlen!")
            continue


        if rechen==1:
                ergebnis= wert1 + wert2
                print(ergebnis)
                publish.single(MQTT_PATH,ergebnis,hostname=MQTT_SERVER)
        elif rechen==2:
                ergebnis=wert1-wert2
                print(ergebnis)
                publish.single(MQTT_PATH,ergebnis,hostname=MQTT_SERVER)
        elif rechen==3:
                ergebnis= wert1*wert2
                print(ergebnis)
                publish.single(MQTT_PATH,ergebnis,hostname=MQTT_SERVER)
        elif rechen==4:
                ergebnis=wert1/wert2
                print(ergebnis)        
                publish.single(MQTT_PATH,ergebnis,hostname=MQTT_SERVER)
        else:
                print("Eingabe ungültig. Bitte wiederholen")
            

