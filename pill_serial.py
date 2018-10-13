import serial

def activate_slot(slot_num):
    ser.write(str(slot_num))

ser = serial.Serial("/dev/ttyACM0", 9600)
ser.flushInput()

while True:
    num = input("Slot: ")
    activate_slot(num)