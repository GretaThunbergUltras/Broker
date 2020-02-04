# MQTT-Pi-Project
## Netzwerk zur Datenerhebung/-speicherung/-verwaltung

![Programmablaufplan](https://i.ibb.co/HzTDQ8t/Programmablaufplan.png)


### HowTo:

#### Festplatte:
- Festplatte einbinden:  `sudo mount -t exfat -o utf8,uid=pi,pid=pi,noatime /dev/sda1 /media/exter`

#### botlib:
- ggf. botlib klonen:  `git clone https://github.com/GretaThunbergUltras/botlib.git`
- Branch wechseln:  `git branch origin/witling-design`
- botlib installieren: `sudo ./install`

#### send end recive file
- Subscriber Script starten: `sudo python mqtt_subscriber.py`
- Publisher Script ausführen:  `sudo python mqtt_publisher.py`

### Links:
- [Funkkommunikation zwischen Raspberry Pi’s mittels MQTT Broker/Client](https://tutorials-raspberrypi.de/datenaustausch-raspberry-pi-mqtt-broker-client/)

