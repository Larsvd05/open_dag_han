#!/usr/bin/python
import time
import serial # pip install pyserial

# sudo dmesg om de usb poort te vinden (direct nadat deze ingeplugged is).
# Voer deze Python code gewoon uit in de terminal en dan komt het goed.
# Als hij niet reageert, baud rate aanpassen (knop van BAUD), ingedrukt houden, als hij gaat knipperen dan kan je het aanpassen. LEDje A en B moeten aan staan voor de juiste!!
# Credits naar Bram voor de code en uitleg.

# Originele sequences
#               T     0     1     2     3     4     5    6
#sequences = ((1000,  900, 1600, 1500, 1500,  900, 900, 1000), (2000, 1500, 1200, 1200, 1900,  900, 1400, 2000), (5000, 2100, 1300,  900, 1700, 1800, 2100, 1000), (600, 1500, 1200, 1400, 1500, 1800, 1500, 2000))

# Open dag sequenties die leuk zijn :)
# 
sequences = ((1000,  900, 1600, 1500, 1500,  900, 900, 1000), (2000, 1500, 1200, 1200, 1900,  900, 1400, 2000), (5000, 2100, 1300,  900, 1700, 2500, 2100, 1000), (3000, 2100, 1300,  900, 1700, 500, 2100, 2500), (600, 1500, 1200, 1400, 1500, 1800, 1500, 2000))


# Test sequences
# T mag niet lager dan 600, want dan trekt hij alles mee.
#sequences = ((2000, 1000, 1000, 1000, 1800, 1000, 1000), (2000, 2100, 2100, 2100, 2100, 2100, 2100))

# Test sequence voor
#sequences = ((2000, 1000, 1400, 1000, 1600, 2600, 1900), (5000, 1600, 1000 , 800, 1800, 1400, 1915))

# Oppak sequence
#sequences = ((3000, 1600, 900, 800, 600, 1400, 1000), (3000, 1600, 900, 800, 600, 1400, 2250),(1000, 1600, 1500, 800, 600, 1400, 2250))

# Object zijwaarts gooien sequences
#sequences = ((3000, 1600, 1500, 800, 600, 1400, 1000), (3000, 1600, 900, 800, 600, 1400, 1000),(1000, 1600, 900, 800, 600, 1400, 2250), (300, 1000, 1400, 1000, 1600, 2600, 1900))

# Object zijwaarts gooien maar dan traag
#sequences = ((3000, 1600, 1500, 800, 600, 1400, 1000), (3000, 1600, 900, 800, 600, 1400, 1000),(3000, 1600, 900, 800, 600, 1400, 2250), (3000, 1000, 1400, 1400, 1000, 1600, 2600, 1900))


# Zijwaarts met aanloop
#sequences = ((3000, 1600, 1500, 800, 600, 1400, 1000), (3000, 1600, 900, 800, 600, 1400, 1000),(1000, 1600, 900, 800, 600, 1400, 2250), (300, 1000, 1400, 1000, 1600, 2600, 1900))

# Object recht gooien sequences
#sequences = ((50, 1600, 1800, 800, 1800, 1400, 1986), (3000, 1600, 1000, 800, 1000, 1400, 1000), (1000, 1600, 1000, 800, 1000, 1400, 2250))
#sequences = ((3000, 1600, 1500, 800, 600, 1400, 1000), (3000, 1600, #900, 800, 600, 1400, 1000), (3000, 1600, 900, 800, 600, 1400, 2150), #(50, 1600, 1800, 800, 1800, 1400, 1985))


#port_name = 'COM8'       # WINDOWS; zie device manager / apparaatbeheer
port_name = '/dev/ttyUSB0'  # LINUX;  run in terminal 'dmesg | grep tty'

robotarm_port = serial.Serial(port=port_name, baudrate=115200)
print(robotarm_port.name)

cmd = "#5 P1700 T2000\r"
robotarm_port.write(cmd.encode())

while True:
    for sequence in sequences:
        full_command = ""
        (t, commands) = sequence[0], sequence[1:]
        servo = 0
        for cmd in commands:
            full_command += "#" + str(servo) + " P" + str(cmd)
            servo += 1
        full_command += " T" + str(t) + " \r"
        print(full_command)
        robotarm_port.write(full_command.encode())
        time.sleep((t/1000) + 1)
