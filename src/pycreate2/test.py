import usb.core
import time
import sys

dev = usb.core.find(idVendor=0x050d, idProduct=0x0109)

if dev is None:
    raise ValueError('Device not found')

cfg = dev.get_active_configuration()
intf = cfg[(0,0)]

ep = usb.util.find_descriptor(
    intf,
    # match the first OUT endpoint
    custom_match = \
    lambda e: \
        usb.util.endpoint_direction(e.bEndpointAddress) == \
        usb.util.ENDPOINT_OUT)

assert ep is not None

if dev.is_kernel_driver_active(intf.bInterfaceNumber):
    try:
        dev.detach_kernel_driver(intf.bInterfaceNumber)
    except usb.core.USBError as e:
        sys.exit("Could not detatch kernel driver from interface({0}): {1}".format(i, str(e)))


while True:
    time.sleep(0.1)
    try:
        ep.write("test\n\r")
        break
    except usb.core.USBError as e:
        print(e)
    sys.stdout.flush()
usb.util.dispose_resources(dev)
print(r)

