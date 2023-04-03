#include <Arduino.h>
#include <WMHead.h>
#include <WMBoard.h>

WMRGBLed rgbLED(0,4);
WMMatrixLed matrixLed(5);
WMDCMotor motor1(7);
WMDCMotor motor2(8);

void setup() {
    matrixLed.setColorIndex(1);
    //brightness is from 0-8
    matrixLed.setBrightness(6);
    rgbLED.setColor(0,0,0);
    rgbLED.show();
    matrixLed.drawStr(0,0+8,"Hi");

    motor1.run(-50);
    motor2.run(-50);
    delay(1000);
    motor1.stop();
    motor2.stop();
}

