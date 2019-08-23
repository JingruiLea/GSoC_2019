# GY30 Driver

Driver for RC522, based on SPI library.

## Files

### rc522_base

RC522 basic API

```ceu
code/await PCD_WriteRegister(var byte reg, var byte value) -> none;
```

```ceu
code/await PCD_Reset(none) -> none;
```

```ceu
code/await PCD_WriteRegister2(var byte reg, var usize count, var&[] byte tx) -> none;
```

```ceu
code/await PCD_ReadRegister(var byte reg) -> byte;
```

```ceu
code/await PCD_ReadRegister2(var byte reg, var usize len, var&[] byte buf, var usize offset) -> byte;
```

```ceu
code/await PCD_CalculateCRC(var&[] byte dat, var usize len, var&[] byte res) -> byte;
```

```ceu
code/await PCD_AntennaOn(none) -> none;
```

```ceu
code/await PCD_Init(none)-> none;
```

```ceu
code/await PCD_ClearRegisterBitMask(var byte reg, var byte mask) -> none;
```

```ceu
code/await PCD_SetRegisterBitMask(var byte reg, var byte mask)-> none;
```

### rc522_comm

RC522 common API

```Ceu
code/await PCD_CommunicateWithPICC(var byte command,		
                                   var byte waitIRq,		
                                   var&[] byte sendData,		
                                   var usize sendLen,		
                                   var&[] byte backData,		
                                   var usize backLen,		
                                   var usize validBits,	
                                   var usize rxAlign,		
                                   var bool checkCRC) -> byte；
```
```Ceu
code/await PCD_TransceiveData(var&[] byte sendData, 
                              var usize sendLen,
                              var&[] byte backData, 
                              var usize backlen,
                              var usize validBits,
                              var usize rxAlign,
                              var bool checkCRC 
                             ) -> byte;
```
## API
//TODO