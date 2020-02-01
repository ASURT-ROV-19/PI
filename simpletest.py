
import time
import Adafruit_PCA9685
pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(50)
y=input("enter channel: ")
y=int(y)
while True:

    x = input("enter PWM:")
    x=int(x)
    pwm.set_pwm(y, 0, x)

#    for i in range(15):
#        pwm.set_pwm(i, 0, x)

