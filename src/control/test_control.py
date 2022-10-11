from ../pycreate2/create2api import Create2
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

def drive_motor_pwm(bot, pwr):
    try:
        bot.full()
        bot.motor_pwm(-pwr,-pwr)
        input()
        bot.motor_pwm(pwr, pwr)
        input()
    except KeyboardInterrupt:
        return
def drive_direct_pwm(bot, speed):
	try:
		bot.full()
		bot.drive_pwm(-speed, -speed)
		input()
		bot.drive_pwm(speed, speed)
		input()
	except KeyboardInterrupt:
		return

def drive(bot, speed):
    try:
		bot.full()
		bot.drive_direct(-speed, -speed)
		input()
		bot.drive_direct(speed, speed)
		input()
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
    # motor_fwd(bot, 100)
    # drive(bot, 500)
    drive_pwm(bot, 255)

if __name__ == "__main__":
    main()
