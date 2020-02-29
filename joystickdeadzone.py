#https://stackoverflow.com/questions/52124027/python-evdev-reading-axes-x-and-y-of-a-gamepad-simultaneously
from evdev import InputDevice, categorize, ecodes, KeyEvent 
gamepad = InputDevice('/dev/input/event0') 
# Set sensitivity
deadl = 123
deadr = 132
deadup = 123
deaddn = 132

last = {
    "ABS_RZ": 128,
    "ABS_Z": 128,
    "ABS_HAT0Y": 128,
    "ABS_HAT0X": 128,
    "ABS_Y": 128,
    "ABS_X": 128
}
for event in gamepad.read_loop(): 
    if event.type == ecodes.EV_ABS: 
        absevent = categorize(event) 
        if ecodes.bytype[absevent.event.type][absevent.event.code] == 'ABS_RZ':
            last["ABS_RZ"] = absevent.event.value

        if ecodes.bytype[absevent.event.type][absevent.event.code] == 'ABS_Z': 
            last["ABS_Z"] = absevent.event.value

        if ecodes.bytype[absevent.event.type][absevent.event.code] == 'ABS_HAT0Y':
            last["ABS_HAT0Y"] = absevent.event.value

        if ecodes.bytype[absevent.event.type][absevent.event.code] == 'ABS_HAT0X': 
            last["ABS_HAT0X"] = absevent.event.value

        if ecodes.bytype[absevent.event.type][absevent.event.code] == 'ABS_Y':
            last["ABS_Y"] = absevent.event.value

        if ecodes.bytype[absevent.event.type][absevent.event.code] == 'ABS_X': 
            last["ABS_X"] = absevent.event.value

        if last["ABS_RZ"] > deaddn: 
            print 'r_down' 
            print last["ABS_RZ"] 
        elif last["ABS_RZ"] < deadup: 
            print 'r_up' 
            print last["ABS_RZ"] 

        if last["ABS_Z"] > deadr : 
            print 'r_right' 
            print last["ABS_Z"] 
        elif last["ABS_Z"] < deadl: 
            print 'r_left' 
            print last["ABS_Z"]

        if last["ABS_HAT0Y"] > deaddn: 
            print 'l_down' 
            print last["ABS_HAT0Y"] 
        elif last["ABS_HAT0Y"] < deadup: 
            print 'l_up' 
            print last["ABS_HAT0Y"] 

        if last["ABS_HAT0X"] > deadr : 
            print 'l_right' 
            print last["ABS_HAT0X"] 
        elif last["ABS_HAT0X"] < deadl: 
            print 'l_left' 
            print last["ABS_HAT0X"]

        if last["ABS_Y"] > deaddn: 
            print 'l_down' 
            print last["ABS_Y"] 
        elif last["ABS_Y"] < deadup: 
            print 'l_up' 
            print last["ABS_Y"] 

        if last["ABS_X"] > deadr : 
            print 'l_right' 
            print last["ABS_X"] 
        elif last["ABS_X"] < deadl: 
            print 'l_left' 
            print last["ABS_X"]
