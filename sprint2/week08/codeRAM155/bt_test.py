''' Test code for piRover Bluetooth
'''
import time
from piRover_Bluetooth import Bluetooth, Action

bt = Bluetooth()
while(True):
    action = bt.next_action()
    print(action.name)
    if action == Action.LED_OFF:
        break
    time.sleep(.1)
print("Done")

