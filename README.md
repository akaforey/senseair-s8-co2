# senseair-s8-co2
Capture and display CO2 data from the Senseair s8 sensor connected to a Raspberry Pi.

This repository contains the code necessary to capture CO2 readings every 5 minutes and record those values.
Records can be accessed and displayed in a graph to show trends over time and to indicate when CO2 readings exceed a safe limit.

This project was written for the purpose of detecting leaks from a CO2 tank with a hose that comes undone easily.

### TODO
- [x] Write a an application to serve the data over the network
- [ ] Improve the server and graph generation to be faster
- [ ] Make an interactive display to control what time frame is being displayed
- [x] Capture data and save it for future viewing

### Acknowledgement
This repo uses the schematic shown in [this document](http://co2meters.com/Documentation/AppNotes/AN168-S8-raspberry-pi-uart.pdf) to connect the sensor to the pi. The code included is useful for getting started with the s8 sensor.
