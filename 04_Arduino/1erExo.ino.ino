#include <SoftwareSerial.h>

SoftwareSerial BT(10, 11); // RX, TX du HC-05

int lampe1 = 7; 
int lampe2 = 8;
char commande;

void setup() {
  pinMode(lampe1, OUTPUT);
  pinMode(lampe2, OUTPUT);
  digitalWrite(lampe1, LOW);
  digitalWrite(lampe2, LOW);
  
  BT.begin(9600);
  Serial.begin(9600);
  Serial.println("Systeme pret");
}

void loop() {
  if (BT.available()) {
    commande = BT.read();
    Serial.print("Commande recue: ");
    Serial.println(commande);
    
    if (commande == '1') {
      digitalWrite(lampe1, HIGH); 
      BT.println("Lampe 1 ON");
    }
    if (commande == '2') {
      digitalWrite(lampe2, HIGH); 
      BT.println("Lampe 2 ON");
    }
    if (commande == '0') {
      digitalWrite(lampe1, LOW);
      digitalWrite(lampe2, LOW);
      BT.println("Tout OFF");
    }
  }
}