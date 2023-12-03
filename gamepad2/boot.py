# boot.py
import usb_hid

gamepad = usb_hid.Device(
    report_descriptor=bytes((
        0x05, 0x01,  # Usage Page (Generic Desktop)
        0x09, 0x05,  # Usage (Gamepad)
        0xa1, 0x01,  # Collection (Application)
        0x85, 0x01,  # Report ID

        0xa1, 0x02,  # Collection (logical)
        0x05, 0x01,  # Usage Page (Generic Desktop)
        0x09, 0x30,  # Usage (X)
        0x09, 0x31,  # Usage (Y)
        0x09, 0x32,  # Usage (Z)
        0x09, 0x33,  # Usage (RX)
        0x15, 0x80,  # Logical Minimum (-128)
        0x25, 0x7F,  # Logical Maximum (127)
        0x75, 0x08,  # Report Size (8)
        0x95, 0x04,  # Report Count (4)
        0x81, 0x02,

        0xc0,  # End Collection
        0x85, 0x02,  # Report ID

        0xa1, 0x02,  # Collection (logical)
        0x05, 0x09,  # Usage Page (Button)
        0x19, 0x01,  # Usage Minimum (Button 1)
        0x29, 0x10,  # Usage Maximum (Button 16)
        0x15, 0x00,  # Logical Minimum (0)
        0x25, 0x01,  # Logical Maximum (1)
        0x75, 0x01,  # Report Size (1)
        0x95, 0x10,  # Report Count (16)
        0x81, 0x02,  # Input (Data, Variable, Absolute)

        0xc0,  # End Collection
        0xc0  # End Collection
    )),
    usage_page=0x01,
    usage=0x05,
    report_ids=(0x01, 0x02,),
    in_report_lengths=(4, 2,),
    out_report_lengths=(0, 0, )
)

usb_hid.enable([gamepad])
