import serial.tools.list_ports
import serial
ports = serial.tools.list_ports.comports(include_links=False)
for port in ports :
    if port.description=="u-blox GNSS receiver":
        print(port.device)
        print(port.description)
        print(port.manufacturer)