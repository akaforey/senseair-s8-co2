import serial
import time
from datetime import date


def record(data):
    today = date.today()
    filename = f"co2_captures/{today}_co2.csv"

    with open(filename, 'a') as file:
        file.write(','.join([str(x) for x in data]) + "\n")


def main_loop():
    ser = serial.Serial("/dev/ttyS0", baudrate =9600, timeout=.5)
    print(" AN-168: Raspberry Pi3 to S8 Via UART\n")
    ser.flushInput()
    time.sleep(1)
#     for i in range(0,12*6): # At 5 minute intervals, 12 readings per hour for 6 hours
    while True:
        try:
            ser.flushInput()
            ser.write(b'\xFE\x44\x00\x08\x02\x9F\x25')
            time.sleep(1)
            resp = ser.read(7)
            high = resp[3]
            low = resp[4]
            co2 = (high*256) + low
            print(f"CO2 = {co2}")
            record([time.time(), co2])
        except Exception as e:
            print(e)
        time.sleep(5*60-1)


if __name__ == "__main__":
    main_loop()
