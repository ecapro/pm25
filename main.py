_10UM2 = 0
_10UM = 0
_03UM = 0
serial.write_line("version:" + ("" + str(custom.read_version())))
smarthome.dht11_sensor(DigitalPin.P0, smarthome.DHT11_state.DHT11_TEMPERATURE_C)

def on_forever():
    global _03UM, _10UM, _10UM2
    _03UM = custom.particle_number(MyEnum1.UM03)
    _10UM = custom.particle_number(MyEnum1.UM10)
    _10UM2 = custom.particle_number(MyEnum1.UM100)
    serial.write_line("0.3UM:" + ("" + str(_03UM)))
    serial.write_line("1.0UM:" + ("" + str(_10UM)))
    serial.write_line("10UM:" + ("" + str(_10UM2)))
    serial.write_line("")
    basic.pause(1000)
    datalogger.log(datalogger.create_cv("", 0))
    led.set_brightness(int(_03UM))
    ESP8266_IoT.set_data("your_write_api_key",
        Environment.dht11value(Environment.DHT11Type.DHT11_TEMPERATURE_C, DigitalPin.P15),
        gatorSoil.moisture(AnalogPin.P0, gatorSoilType.SOIL_MOISTURE, DigitalPin.P0))
basic.forever(on_forever)
