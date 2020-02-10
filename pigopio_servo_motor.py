import pigpio
import time

# refer to http://blawat2015.no-ip.com/~mieki256/diary/201607201.html
#
# how to use pigpio
#  $ sudo pigpiod
#
# how to use pigpio on startup
#  $ sudo systemctl enable pigpiod.service
#  $ sudo systemctl restart pigpiod.service

SERVO_PIN = 12    #GPIO
START_V = 500   #us
END_V = 2400    #us

def get_pulsewidth(angle):
    angle += 90.0
    if angle < 0.0:
        angle = 0.0
    if angle > 180.0:
        angle= 180.0
    
    pw = (END_V - START_V) * (float(angle) / 180.0) + START_V
    return pw

pig = pigpio.pi()

try:
    for angle in [0,-90,0,90,0,-90,-45,0,45,90,45,0]:
        pw = get_pulsewidth(angle)
        pig.set_servo_pulsewidth(SERVO_PIN ,pw)
        time.sleep(0.5)
        pig.set_servo_pulsewidth(SERVO_PIN , 0)
        time.sleep(2.5)

except KeyboardInterrupt:
    pass

pig.stop()

