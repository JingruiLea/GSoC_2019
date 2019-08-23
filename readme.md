# Low-Power Interrupt-Based Drivers in Céu-Arduino - GSoC 2019

This repo describes all works I've done on GSoC 2019.

## Analog I2C

This driver can be used to communicate via TWI **as master only**, compatible with I2C.

It API is same as `Interrupt-Based I2C`.

See also:  

- [I2C README.md](./ana_i2c/readme.md)
- [I2C example](./ana_i2c/example)

## Interrupt-Based I2C

This library allows you to communicate with I2C / TWI devices. It provides basically the same function as the Arduino Wire library.

See also:  

- [I2C driver README.md](./driver-i2c/readme.md)
- [I2C example](./example/readme.md)

## EEPROM Driver

EEPROM (electrically erasable programmable read-only memory) is user-modifiable read-only memory (ROM) that can be erased and reprogrammed (written to) repeatedly through the application of higher than normal electrical voltage.

The driver of EEPROM is in the /eeprom/eeprom folder.

See also:  

- [EEPROM driver README.md](./eeprom/eeprom/readme.md)
- [EEPROM example](./eeprom/readme.md)
- [EEPROM datasheet](http://mouser.com/ds/2/268/atmel_doc0180-1065439.pdf)

## GY-30 Driver

GY-30 Digital Light Sensor Module is a carrier board for light intensity sensor BH1750FVI. The range of the board is between 0lx and 65535lx. The board communicates via I2C protocol.

The driver of GY-30 is in the /GY30/GY30 folder.

See also:  

- [GY30 README.md](./GY30/GY30/readme.md)
- [GY30 example](./GY30/readme.md)
- [BH1750 datasheet](https://littlemadoros.tistory.com/attachment/cfile28.uf@99350E4A5C4917DA01E903.pdf)

## Sample Oscilloscope by Arduino and Python

The Oscilloscope contains a sample 'Arduino Oscilloscope'.  
You can draw a line chart of pin voltage changes.

![Figure](./Oscilloscope/Figure_2.png)

## RC522 Driver (Incompleted)

Mifare RC522 is the high integrated RFID card reader.

The RC522 folder contains the basic API for interacting with the RC522 RFID reader.

See also:

- [RC522 README.md](./RC522/readme.md)
- [RC522 datasheet](https://www.nxp.com/docs/en/data-sheet/MFRC522.pdf)
