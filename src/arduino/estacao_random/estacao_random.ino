float temp = 300;
float umid = 30;

void setup() {
Serial.begin(9600);
}

void updatestats() {
  temp += random(-10, 11);

  if (temp < 100) temp = 100;
  if (temp > 400) temp = 400;

  umid += random(-1, 2);

  if (umid < 20) umid = 20;
  if (umid > 80) umid = 80;
}

void loop() {
updatestats();
if (!isnan(temp) && !isnan(umid)) {
Serial.print("{");
Serial.print("\"temperatura\":"); Serial.print(temp/10);
Serial.print(",\"umidade\":"); Serial.print(umid);
Serial.println("}");
}
delay(1000);
}