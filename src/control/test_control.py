from pycreate2 import Create2
import time

def main():
    bot = Create2("/dev/serial/by-path/pci-0000:00:14.0-usb-0:3:1.0-port0")
    bot.start()
    time.sleep(10)
    bot.close()
    #bot.full()
    #sensors = bot.get_sensors()
    #print(sensors)
    #bot.drive_direct(100,100)
    #time.sleep(2)
    #bot.drive_stop()
    #bot.close()

if __name__ == "__main__":
    main()
