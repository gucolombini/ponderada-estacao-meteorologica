float temp = 550;
float umid = 24;

void setup() {
Serial.begin(9600);
}

void updatestats() {
  temp += random(-10, 11);

  if (temp < 550) temp = 550;
  if (temp > 600) temp = 600;

  umid += random(-1, 2);

  if (umid < 24) umid = 24;
  if (umid > 28) umid = 28;
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