#https://stackoverflow.com/questions/52124027/python-evdev-reading-axes-x-and-y-of-a-gamepad-simultaneously
from evdev import InputDevice, categorize, ecodes, KeyEvent 
gamepad = InputDevice('/dev/input/event0') 
last = {
    "ABS_RZ": 128,
    "ABS_Z": 128,
    "ABS_HAT0Y": 128,
    "ABS_HAT0X": 128
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

        if last["ABS_RZ"] > 128: 
            print 'r_down' 
            print last["ABS_RZ"] 
        elif last["ABS_RZ"] < 127: 
            print 'r_up' 
            print last["ABS_RZ"] 

        if last["ABS_Z"] > 128 : 
            print 'r_right' 
            print last["ABS_Z"] 
        elif last["ABS_Z"] < 127: 
            print 'r_left' 
            print last["ABS_Z"]

#        if last["ABS_HAT0Y"] > 128: 
#            print 'l_down' 
#            print last["HAT0Y"] 
#        elif last["ABS_HAT0Y"] < 127: 
#            print 'l_up' 
#            print last["ABS_HAT0Y"] 
#
#        if last["ABS_HAT0X"] > 128 : 
#            print 'l_right' 
#            print last["ABS_HAT0X"] 
#        elif last["ABS_HAT0X"] < 127: 
#            print 'l_left' 
#            print last["ABS_HAT0X"]
