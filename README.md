# pyESPEC
A simple API for controlling [ESPEC] temperature/climate chambers. It is built on top of a previous library, [pyUART], which manages the protocol layer by wrapping [ftd2xx]. As the latter statement implies, this solution is dependent on use with a FTDI-UART Bridge IC such as the [FT232R]. Additionally, a transceiver chip is needed to convert the low-voltage, single-ended CMOS I/O (3.3V) to differential levels compliant with EIA-422/485. 

**NOTE:** Cables and adapters with the bridge and transceiver ICs already integrated can be easily procured [online].  The key aspect is to ensure that the selected product is using the FT232R (or similar) and supports full duplex mode (i.e. ESPEC chambers require a 4-wire communication interface).         

**NOTE:** pyUART and ft2dxx are requirements to use this module. The former expects the dll to be placed in `C:\Python27\Lib\site-packages\`. Please update as necessary should it be stored elsewhere.   

**NOTE:** Tested with Python 2.7 on Windows 7 with the SH-241 temperature/humidity chamber. 

## References
[SH Series Temperature Chambers]

[USB-RS422-WE-5000-BT Datasheet]

[RS485 Reference Guide]

[RS485 Transceiver ICs]

[ESPEC]: http://www.espec.co.jp/english/products/env-test/sh/
[pyUART]: https://github.com/jmbattle/pyUART
[ftd2xx]: http://www.ftdichip.com/Drivers/D2XX.htm
[FT232R]: http://www.ftdichip.com/Support/Documents/DataSheets/ICs/DS_FT232R.pdf
[online]: http://www.aliexpress.com/wholesale?catId=0&initiative_id=SB_20160620034650&SearchText=usb+to+RS-485
[SH Series Temperature Chambers]: http://www.espec.co.jp/english/inquiry/catalog/sh.pdf
[USB-RS422-WE-5000-BT Datasheet]: http://www.ftdichip.com/Support/Documents/DataSheets/Cables/DS_USB_RS422_CABLES.pdf
[RS485 Reference Guide]: http://www.ti.com/lit/sg/slyt484a/slyt484a.pdf
[RS485 Transceiver ICs]: http://www.ti.com/lsds/ti/interface/rs-485-products.page#p305nom=5&p1065=Full

