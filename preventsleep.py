import ctypes
import reapy_boost as reapy

project = reapy.Project()

ES_CONTINUOUS = 0x80000000
ES_SYSTEM_REQUIRED = 0x00000001
ES_DISPLAY_REQUIRED = 0x00000002

def deferred_loop(i):
    if project.is_stopped == False: #on playing, recording and pause
        if i > 100: # count to 100 then it clicks about every 3 seconds
          i = 0
          # reset the windows standby timer
          ctypes.windll.kernel32.SetThreadExecutionState(ES_DISPLAY_REQUIRED) 
        #reapy.print(i)
    
    # loop
    reapy.defer(deferred_loop, i + 1)

deferred_loop(0)  # Start the loop
