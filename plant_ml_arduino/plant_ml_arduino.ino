#define ENABLE 5
#define DIRA 3
#define DIRB 4
int gesture = -1;  // Variable to store the received gesture state


void setup() {
  pinMode(ENABLE, OUTPUT);
  pinMode(DIRA, OUTPUT);
  pinMode(DIRB, OUTPUT);
  Serial.begin(9600);
  // digitalWrite(ENABLE, LOW);  // ✅ Enable the motor driver
}

void loop() {
  if (Serial.available() > 0) {
    gesture = Serial.parseInt();  // Read the integer gesture from serial
    Serial.print("Received Gesture: ");
    Serial.println(gesture);

    if (gesture == 0) {
      digitalWrite(DIRA, LOW);  // 🛑 Stop the motor
      digitalWrite(ENABLE, LOW);
      Serial.println("FAN OFF");
    } 
    else if (gesture == 1) {
      
      digitalWrite(DIRA, HIGH);  // ✅ Start the motor
      digitalWrite(ENABLE, HIGH);
      
      
      Serial.println("FAN ON");
    } else if (gesture == 2) {
      digitalWrite(DIRA, LOW);  // 🛑 Stop the motor
      digitalWrite(ENABLE, LOW);
      Serial.println("FAN OFF");
    }
    delay(100);
  }
}
