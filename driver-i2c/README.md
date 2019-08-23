# I2C (TWI)
This driver can be used to communicate via TWI between microcontrollers, compatible with I2C.

## Pins

```
Board	              I2C / TWI pins
Uno, Ethernet	      A4 (SDA), A5 (SCL)
Mega2560	      20 (SDA), 21 (SCL)
Leonardo	      2 (SDA), 3 (SCL)
Due	              20 (SDA), 21 (SCL), SDA1, SCL1
```

## API

### Includes

```ceu
#include "i2c.ceu"
```

### Events
```Ceu
output (on/off,u8?) I2C;  
input none I2C_SLAVE_RECEIVE_REQUESTED;  
input none I2C_SLAVE_SEND_REQUESTED;  
```

#### I2C

Emit the I2C to on to begin the Two Wire Interface. It has a second optional parameter for address which is necessary for a slave and optional for a master.

```
emit I2C(on,_);
```
Set address of the device by emitting I2C with the desired address as the second parameter.

```
emit I2C(on,8);
```

To stop using I2C communication you can turn it off by emitting the I2C to off

```
emit I2C(off,_);
```

#### I2C_SLAVE_RECEIVE_REQUESTED

When master send data to slave. This input is emitted on slave.

#### I2C_SLAVE_SEND_REQUESTED

When master requests slave send data. This input is emitted on slave.

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

#### I2C_Slave_Send

```ceu
code/await I2C_Slave_Send(var&[] byte buf) -> bool;
```
Parameters:

- `byte[] buf` : buffer of data
- `u8? address`: I2C slave address
- `usize? len` : data length wish to read, will read data length of `len` or less

#### I2C_Slave_Receive

```ceu
code/await I2C_Slave_Receive(var&[] byte buf) -> bool;
```

Parameters:

- `byte[] buf` : buffer of data
- `u8? address`: I2C slave address

#### I2C_Set_Clock

Set twi bit rate
```ceu
code/call I2C_Set_Clock (var u32 clock) -> none;
```
Parameters:

- `u32 clock` : Clock Frequency
