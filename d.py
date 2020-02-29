#https://stackoverflow.com/questions/52124027/python-evdev-reading-axes-x-and-y-of-a-gamepad-simultaneously
from evdev import InputDevice, categorize, ecodes, KeyEvent 
gamepad = InputDevice('/dev/input/event0') 
last = {
    "ABS_RZ": 128,
    "ABS_Z": 128
}
for event in gamepad.read_loop(): 
    if event.type == ecodes.EV_ABS: 
        absevent = categorize(event) 
        if ecodes.bytype[absevent.event.type][absevent.event.code] == 'ABS_RZ':
            last["ABS_RZ"] = absevent.event.value

        if ecodes.bytype[absevent.event.type][absevent.event.code] == 'ABS_Z': 
            last["ABS_Z"] = absevent.event.value

        if last["ABS_RZ"] > 128: 
            print 'reverse' 
            print last["ABS_RZ"] 
        elif last["ABS_RZ"] < 127: 
            print 'forward' 
            print last["ABS_RZ"] 

        if last["ABS_Z"] > 128 : 
            print 'right' 
            print last["ABS_Z"] 
        elif last["ABS_Z"] < 127: 
            print 'left' 
            print last["ABS_Z"]

        if last["ABS_RZ"] > 128: 
            print 'reverse' 
            print last["ABS_RZ"] 
        elif last["ABS_RZ"] < 127: 
            print 'forward' 
            print last["ABS_RZ"] 

        if last["ABS_Z"] > 128 : 
            print 'right' 
            print last["ABS_Z"] 
        elif last["ABS_Z"] < 127: 
            print 'left' 
            print last["ABS_Z"]
