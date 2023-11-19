# boot.py
import usb_hid

gamepad = usb_hid.Device(
    report_descriptor=bytes((
        0x05, 0x01, # Usage Page (Generic Desktop)
        0x09, 0x05, # Usage (Gamepad)
        0xa1, 0x01, # Collection (Application)
        0x85, 0x02, # Report ID
        # 16 buttons, value 0=off, 1=on (2 bytes)
        0x05, 0x09, # Usage Page (Button)
        0x19, 0x01, # Usage Minimum (Button 1)
        0x29, 0x10, # Usage Maximum (Button 16)
        0x15, 0x00, # Logical Minimum (0)
        0x25, 0x01, # Logical Maximum (1)
        0x75, 0x01, # Report Size (1)
        0x95, 0x10, # Report Count (16)
        0x81, 0x02, # Input (Data, Variable, Absolute)
        0x05, 0x01, # Usage Page (Generic Desktop)
        0x09, 0x30, # Usage (X)
        0x09, 0x31, # Usage (Y)
        0x09, 0x32, # Usage (Z)
        0x09, 0x35, # Usage (RZ)
        0x15, 0x81, # Logical Minimum (-127)
        0x25, 0x7F, # Logical Maximum (127)
        0x75, 0x08, # Report Size (8)
        0x95, 0x04, # Report Count (4)
        0x81, 0x02, # Input (Data,Var,Abs,No Wrap,Linear,Preferred State,No Null Position)
        0xc0 # End Collection
    )),
    usage_page=0x01,
    usage=0x05,
    report_ids=(0x02,),
    in_report_lengths=(6,),
    out_report_lengths=(0,)
)

usb_hid.enable([gamepad])
