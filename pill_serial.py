import serial

def activate_slot(slot_num):
    ser.write(str.encode(slot_num))

ser = serial.Serial("/dev/ttyACM0", 9600)
ser.flushInput()

if __name__ == "__main__":
    while True:
        num = input("Slot: ")
        activate_slot(num)