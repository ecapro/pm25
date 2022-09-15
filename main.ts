let _10UM2 = 0
let _10UM = 0
let _03UM = 0
serial.writeLine("version:" + ("" + custom.readVersion()))
smarthome.dht11Sensor(DigitalPin.P0, smarthome.DHT11_state.DHT11_temperature_C)
basic.forever(function () {
    _03UM = custom.particleNumber(MyEnum1.UM03)
    _10UM = custom.particleNumber(MyEnum1.UM10)
    _10UM2 = custom.particleNumber(MyEnum1.UM100)
    serial.writeLine("0.3UM:" + ("" + _03UM))
    serial.writeLine("1.0UM:" + ("" + _10UM))
    serial.writeLine("10UM:" + ("" + _10UM2))
    serial.writeLine("")
    basic.pause(1000)
    datalogger.log(datalogger.createCV("", 0))
    led.setBrightness(Math.trunc(_03UM))
    ESP8266_IoT.setData(
    "your_write_api_key",
    Environment.dht11value(Environment.DHT11Type.DHT11_temperature_C, DigitalPin.P15),
    gatorSoil.moisture(AnalogPin.P0, gatorSoilType.soilMoisture, DigitalPin.P0)
    )
})
