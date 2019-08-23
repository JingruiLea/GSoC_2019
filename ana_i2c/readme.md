# I2C 
This driver can be used to communicate via TWI **as master only**, compatible with I2C.

## Pins

```
#define SDA OUT_05
#define SCL OUT_04
```

## API

### Includes

```ceu
#include "ana_i2c.ceu"
```

### Code Abstractions

#### I2C_Master_Receive

Read specific length data form slave.

```ceu
code/await I2C_Master_Receive(var&[] byte buf, var byte address, var usize len) -> bool;
```
Parameters:

- `byte[] buf` : buffer of data
- `u8? address`: I2C slave address
- `usize? len` : data length wish to read, will read data length of `len` or less

#### I2C_Master_Send

Write data in `buf` to slave.

```ceu
code/await I2C_Master_Send(var&[] byte buf, var byte address) -> bool;
```

Parameters:

- `byte[] buf` : buffer of data
- `u8? address`: I2C slave address
