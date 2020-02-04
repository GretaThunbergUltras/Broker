# MQTT-Pi-Project
## Netzwerk zur Datenerhebung/-speicherung/-verwaltung

### Beschreibung:
Fahrende Robocars sollen ihre aufgenommenen Bilder nicht lokal speichern, sondern über eine MQTT-Verbindung an den Broker schicken welcher diese auf einem externen Speichermedium ablegt. Die gesammelten Daten sollen einer späteren KI zum "lernen" dienen (Objekterkennung/mechinal learning).

### Programmablauf:
(Bild einfügen)

## HowTo:

#### Festplatte:
- Festplatte einbinden:  `sudo mount -t exfat -o utf8,uid=pi,pid=pi,noatime /dev/sda1 /media/extern`

#### botlib:
- ggf. botlib klonen:  `git clone https://github.com/GretaThunbergUltras/botlib.git`
- Branch wechseln:  `git checkout origin/witling-design`
- Branch aktualisieren: `git pull origin witling-desing`
- botlib installieren:  `sudo ./install`

#### send end recive file
- Subscriber Script starten: `sudo python3 recive_file.py`
- Publisher Script ausführen:  `sudo python3 send_file.py`

### Links:
- [Funkkommunikation zwischen Raspberry Pi’s mittels MQTT Broker/Client](https://tutorials-raspberrypi.de/datenaustausch-raspberry-pi-mqtt-broker-client/)

### Ideen für die Zukunft:
- [Webinterface zu Statusabfrage](https://github.com/fabaff/mqtt-panel)


