int pot = A0; //potenciometro

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);  
}

int valor;
void loop() {
  // put your main code here, to run repeatedly:
  valor = analogRead(pot); //0-1023

  Serial.println(valor);  
  delay(100); //ms

}
