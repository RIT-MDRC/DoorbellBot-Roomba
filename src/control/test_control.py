from pycreate2 import Create2
import time


def ascii_out(bot):
    while True:
        try:
            bot.full()
            bot.digit_led_ascii("1234")
        except KeyboardInterrupt:
            return

def motor_fwd(bot, pwr):
    while True:
        try:
            bot.full()
            bot.drive_direct(pwr, pwr)
            print(bot.get_sensors())
        except KeyboardInterrupt:
            return

def read_sensors(bot):
    while True:
        try:
            # bot.full()
            sensors = bot.get_sensors()
            print(sensors)
        except KeyboardInterrupt:
            return
        except Exception as e:
            print(e)

def main():
    bot = Create2("/dev/serial/by-id/usb-Belkin_USB_PDA_Adapter_0109_963902-if00-port0")
    bot.start()
    bot.full()
    # ascii_out(bot)
    # read_sensors(bot)
    motor_fwd(bot, 100)

if __name__ == "__main__":
    main()
