import pigpio
import time

SERVO_PIN = 18

pi = pigpio.pi() # Servo Init

def servo_set_angle(angle):
    width = float(angle) * 100.0 / 9.0 + 500 # Convert angle (degrees) to pulse width
    pi.set_servo_pulsewidth(SERVO_PIN, width)

while True:
    servo_set_angle(0)
    time.sleep(2)
    servo_set_angle(90)
    time.sleep(2)
