
# EEPROM Driver

Driver for EEPROM memory(AT24C02), based on I2C library.

## API

### Includes

```ceu
#include "eeprom.ceu"
```

### Functions

#### EEPROM_Write

Write bytes to EEPROM.

```ceu
code/await EEPROM_Write(var byte chip_addr, var&[] byte tx_buf) -> bool
```

Parameters:

- `byte chip_addr` : EEPROM inner address
- `byte[] tx_buf`: bytes data for writing


#### EEPROM_Read

Read bytes form EEPROM.

```ceu
code/await EEPROM_Read(var&[] byte rx_buf, var byte chip_addr, var usize len) -> bool
```

Parameters:

- `byte[] rx_buf`: array where data save
- `byte chip_addr` : EEPROM inner address
- `usize len` : read data length
