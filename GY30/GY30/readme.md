# GY30 Driver

Driver for Light intensity Sensor GY30, based on I2C library.

## API

### Includes

```ceu
#include "GY30.ceu"
```

### Functions

#### GY30_Start

Send start signal to GY30 moudle.

```ceu
code/await GY30_Start(none) -> none;
```

#### GY30_Stop

Send stop signal to GY30 moudle.

```ceu
code/await GY30_Stop(none) -> none;
```

#### GY30_Mode

Send `mode` signal to GY30 moudle.

```ceu
code/await GY30_Mode(var byte mode) -> none;
```

Parameters:

1. `mode`: a specific mode, it's one of belows.  

- GY30_CONTINUOUS_HIGH_1
- GY30_CONTINUOUS_HIGH_2
- GY30_CONTINUOUS_LOW
- GY30_ONCE_HIGH_1
- GY30_ONCE_HIGH_2
- GY30_ONCE_LOW

#### GY30_SetMT

Set measure time of GY30 moudle.

```ceu
code/await GY30_SetMT(var byte mt) -> none;
```

Parameters:  

1. `mt`: measure time of GY30, see also [GY30 datasheet](https://www.elechouse.com/elechouse/images/product/Digital%20light%20Sensor/bh1750fvi-e.pdf).

#### GY30_Read

Read data from GY30.

```ceu
code/await GY30_Read(none) -> u16;
```

return:  
The data read from GY30, you can change the unit to `lux` by divide 1.2.

#### GY30_Address

Set GY30 address.

```ceu
code/await GY30_Address(var byte address) -> none;
```

Parameters:

1. `adderss`: GY30 I2C address, it's one of belows.  

- GY30_LOW_ADDRESS
- GY30_HIGH_ADDRESS
