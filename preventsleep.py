import ctypes               # import to make  dll calls and another bunch of system stuff
from reaper_python import * # import reaper python api

# https://learn.microsoft.com/en-us/windows/win32/api/winbase/nf-winbase-setthreadexecutionstate
#ES_CONTINUOUS = 0x80000000 # a continuous flag, not needed here
#ES_SYSTEM_REQUIRED = 0x00000001 # reset standby timer
ES_DISPLAY_REQUIRED = 0x00000002 # reset display timeout timer (and standby timer)

def deferred_loop(i):
    if RPR_GetPlayState()!= 0: # 0 = stopped; aka on playing, recording and pause
        if i == 100: # count to 100 then it clicks about every 4 to 5 seconds
          i = 0
          ctypes.windll.kernel32.SetThreadExecutionState(ES_DISPLAY_REQUIRED) # reset the windows standby timer
          #RPR_ShowConsoleMsg("prevent")
        RPR_defer("deferred_loop("+str(i+1)+")") # i+1
    
    else:    # if stopped lets do nothing. 
        RPR_defer("deferred_loop(0)")
        
    #RPR_ShowConsoleMsg(i)
deferred_loop(0)  # Start the loop
