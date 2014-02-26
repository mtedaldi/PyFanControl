PyFanControl
============

A set of python scripts to control the fan speed inside a 
cooling cabinet according to temperature

fan-control.py will control the speed of the fan of the heat 
exchanger inside a cooling rack.

The original system by rittal has a fan with constant speed. 
We've added an inverter (Siemens SINAMICS G110 0.25kW) and 
configured it for an output frequency of 30-55Hz (depending on 
the voltage on the linear voltage input).

This Setup is controled by a Raspberry Pi
Connected to the RaspberryPi i2c are a temperature sensor 
MCP9808 and a DAC MCP4725

The software in the Pi will set the output voltage acording to 
the measured temperature and also send warnings by email in
case of over temperature.

There is also a module for munin-node[1] so the temperature of
the sensor can be tracked on a munin-server via web browser.


[1]http://munin-monitoring.org/
