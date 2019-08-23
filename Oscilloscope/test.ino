
void setup() {
  pinMode(A1, INPUT);
  pinMode(A2, INPUT);
  Serial.begin(9600);
}

void loop() {
  int a1 = analogRead(A1);
  int a2 = analogRead(A2);

  byte data = Serial.read();
  if (data == 'x')
  {
    Serial.print(a1);
    Serial.print(",");
    Serial.print(a2);
    Serial.println();
    delay(5);        // delay in between reads for stability
  }
}

