# GY30模块驱动

用于光强度传感器GY30的驱动器，基于I2C库。

## API

### include

```CEU
#include“GY30.ceu”
```

### 函数

#### GY30_Start

将开始信号发送到GY30模块。

```CEU
code / await GY30_Start(none) -> none;
```

#### GY30_Stop

向GY30模块发送停止信号。

```CEU
code / await GY30_Stop(none) -> none;
```

#### GY30_Mode

发送'mode`信号到GY30模块。

```CEU
code / await GY30_Mode(var byte mode) -> none;
```

参数：

1.`mode`：一种特定模式，它是下面的模式之一。

- GY30_CONTINUOUS_HIGH_1
- GY30_CONTINUOUS_HIGH_2
- GY30_CONTINUOUS_LOW
- GY30_ONCE_HIGH_1
- GY30_ONCE_HIGH_2
- GY30_ONCE_LOW

#### GY30_SetMT

设置GY30模块的测量时间。

```CEU
code / await GY30_SetMT(var byte mt) -> none;
```

参数：

1.`mt`：测量GY30的时间，另见[GY30数据表](https://www.elechouse.com/elechouse/images/product/Digital%20light%20Sensor/bh1750fvi-e.pdf)。

#### GY30_Read

从GY30读取数据。

```CEU
code / await GY30_Read(none) -> u16;
```

返回:  
从GY30读取的数据，您可以除以1.2将单位更改为“lux”。

#### GY30_Address

设置GY30地址。

```CEU
code / await GY30_Address(var byte address) -> none;
```

参数：

1.`adderss`: GY30 I2C地址，它是下面的地址之一。

- GY30_LOW_ADDRESS
- GY30_HIGH_ADDRESS
