import RPi.GPIO as GPIO
#IN1=20
#IN2=21
#ENA=16
ENA_PWM=0

#forPulley
IN1=26
IN2=19
ENA=13


GPIO.cleanup()

GPIO.setmode(GPIO.BCM)

GPIO.setup(IN1,GPIO.OUT)
GPIO.setup(IN2,GPIO.OUT)
GPIO.setup(ENA,GPIO.OUT)

while True:
            x = input("X:")
            x = int(x)
            if x == 1:
                GPIO.output(ENA, 1)
                GPIO.output(IN1, 1)
                GPIO.output(IN2, 0)
#                self.ENA_PWM = 1

            elif x == 0:
                GPIO.output(ENA, 0)
                GPIO.output(IN1, 0)
                GPIO.output(IN2, 0)
#                self.ENA_PWM = 0

            elif x == -1:
                GPIO.output(ENA, 1)
                GPIO.output(IN1, 0)
                GPIO.output(IN2, 1)
