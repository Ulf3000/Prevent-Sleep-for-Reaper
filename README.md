# Prevent-Sleep-for-Reaper

prevents the pc and connected displays to go into standby by repeatedly calling SetThreadExecutionState(ES_DISPLAY_REQUIRED)
when reaper is in:

-Playback
-Pause 
-Recording

This is, as far as i understand, the same way mediaplayers and browsers do it when the pc shouldnt go to sleep.  

# Installation is a bit hacky: 

- first you need to install reapy-boost https://github.com/Levitanus/reapy-boost into the python you use for reaper.
  
  We need reapy-boost to run a python loop outside of reaper's main thread
  

- now activate reapy-boost by calling reapy-boost.configure_reaper() from inside reaper (just use a dummy .py file and import as action)
  this only needs to be done once per installation and never again after that
  

- you also need to install SWS extension for reaper from here:
  https://www.sws-extension.org/
  SWS extension can run scripts on reaper startup
  

- finally save my script to a .py file and import it with reapers action list as a new action.
- copy the command/action ID and paste it into SWS -> startup actions -> global startup actions
- the script should now run on reaper startup


