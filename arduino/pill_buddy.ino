#include <Servo.h>

Servo slot1;
Servo slot2;
Servo slot3;

int incomingByte = 0;

void setup() {
  Serial.begin(9600);
  
  slot1.attach(13);
  slot2.attach(12);
  slot3.attach(11);

  set_all(180);

//  dispense(slot1);
//  delay(1000);
//  dispense(slot2);
//  delay(1000);
//  dispense(slot3);
}

void set_all(int pos) {
  slot1.write(pos);
  slot2.write(pos);
  slot3.write(pos);
}

void dispense(Servo &slot) {
  for(int i = 180; i >= 0; i--) {
    slot.write(i);
    delay(1);
  }
  delay(2000);
  for(int i = 0; i <= 180; i++) {
    slot.write(i);
    delay(1);
  }
}

void check_serial() {
  if (Serial.available() > 0) {
    incomingByte = Serial.read();
    // say what you got:
    Serial.print("I received: ");
    Serial.println(incomingByte, DEC);
    if (incomingByte == 49) {
      dispense(slot1);
    } else if (incomingByte == 50) {
      dispense(slot2);
    } else if (incomingByte == 51) {
      dispense(slot3);
    }
  }
}

void loop() {
  check_serial();

}

