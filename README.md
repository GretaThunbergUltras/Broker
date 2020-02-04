# MQTT-Pi-Project
## Netzwerk zur Datenerhebung/-speicherung/-verwaltung

### Beschreibung:
Fahrende Robocars sollen ihre aufgenommenen Bilder nicht lokal speichern, sondern über eine MQTT-Verbindung an den Broker schicken welcher diese auf einem externen Speichermedium ablegt. Die gesammelten Daten sollen einer späteren KI zum "lernen" dienen (Objekterkennung/mechinal learning).

### Programmablaufplan:
![Programmablaufplan](https://i.ibb.co/w605N3B/Broker.png)
(Bild einfügen)
## HowTo:

#### Festplatte:
- Festplatte einbinden:  `sudo mount -t exfat -o utf8,uid=pi,pid=pi,noatime /dev/sda1 /media/extern`

#### botlib:
- ggf. botlib klonen:  `git clone https://github.com/GretaThunbergUltras/botlib.git`
- Branch wechseln:  `git checkout origin/witling-design`
- Branch aktualisieren: `git pull origin witling-desing`
- botlib installieren:  `sudo ./install`

#### send and recive file:
- recive_file auf Broker starten: `sudo python3 recive_file.py`
- send_file auf Client (Gruppe11) starten:  `sudo python3 send_file.py`

### Links:
- [Funkkommunikation zwischen Raspberry Pi’s mittels MQTT Broker/Client](https://tutorials-raspberrypi.de/datenaustausch-raspberry-pi-mqtt-broker-client/)

### Ideen für die Zukunft:
- [Webinterface zu Statusabfrage](https://github.com/fabaff/mqtt-panel)


## Autoren:
* __[Mercedes Doert](https://github.com/CEDY20)__
* __[Kris Myslowski](https://github.com/Nutzernam3)__

## Großes Danke an:
* __[Laurin Kirbach](https://github.com/witling)__
für die Botlib und die Rettung vor der Depression.
* __[Elias Hörner](https://github.com/eliaspr)__
für die Bereitschaft zum Testen und Fehlerbehebung.







