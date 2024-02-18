import ctypes
from reaper_python import *

ES_CONTINUOUS = 0x80000000
ES_SYSTEM_REQUIRED = 0x00000001
ES_DISPLAY_REQUIRED = 0x00000002

def deferred_loop(i):
    if RPR_GetPlayState()!= 0: # 0 = stopped; aka on playing, recording and pause
        if i == 100: # count to 100 then it clicks about every 4 to 5 seconds
          i = 0
          ctypes.windll.kernel32.SetThreadExecutionState(ES_DISPLAY_REQUIRED) # reset the standby timer
          #RPR_ShowConsoleMsg("prevent")
        RPR_defer("deferred_loop("+str(i+1)+")") # i+1
    
    else:    # lets not count up to huge numbers please. 
        RPR_defer("deferred_loop("+str(i)+")") # i
        
    #RPR_ShowConsoleMsg(i)
deferred_loop(0)  # Start the loop
