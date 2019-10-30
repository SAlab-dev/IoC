// BH1750FVI - Version: 1.1.1
#include <BH1750FVI.h>
#include <Wire.h>

float noise;
float gas;
int movement;

BH1750FVI LightSensor(BH1750FVI::k_DevModeContLowRes);


void setup() {

  Serial.begin(9600);
  pinMode(2, INPUT);
  LightSensor.begin();
  Serial.print("Running...");

}

void loop() {

  uint16_t lux = LightSensor.GetLightIntensity();

  noise = analogRead(A2);
  gas = analogRead(A1);
  movement = digitalRead(2);

  String NoiseDataOne = "Noise sensor value: ";
  String NoiseData = NoiseDataOne + noise;
  Serial.println(NoiseData);
  delay(1000);
  
  String GasDataOne = "Gas sensor value: ";
  String GasData = GasDataOne + gas;
  Serial.println(GasData);
  delay(1000);
  
  String MovementDataOne = "Movement sensor value: ";
  String MovementDataNobody = "Nobody...";
  String MovementDataDetected = "Movement detected!";
  String MovementDataTwo = MovementDataOne + MovementDataNobody;
  String MovementDataThree = MovementDataOne + MovementDataDetected;
  
  if (movement == 0) {
    Serial.println(MovementDataTwo); 
  }
  else {
    Serial.println(MovementDataThree);
  }
  delay(1000);
  
  String LightDataOne = "Light sensor value: ";
  String LightDataTwo = " lux";
  String LightData = LightDataOne + lux + LightDataTwo;
  Serial.println(LightData);
  

  delay(1000);
  
}
