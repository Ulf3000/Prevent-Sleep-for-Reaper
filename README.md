# Prevent-Sleep-for-Reaper

prevents the pc and connected displays to go into standby by repeatedly calling SetThreadExecutionState(ES_DISPLAY_REQUIRED)
when reaper is NOT stopped aka in:

-Playback

-Pause 

-Recording

-Recording pre-roll

This is, as far as i understand, the same way mediaplayers and browsers do it when they are playing a video and the pc and displays shouldnt go to sleep.
The script counts to 100 which is about every 4 to 5 seconds.

# Installation: 

- First you need to install SWS extension for reaper from https://www.sws-extension.org/

  SWS extension can run a global startup script on reaper startup
  
- save the script to a .py file and import it with reapers action list as a new action.

- copy the command/action ID and paste it into SWS -> startup actions -> global startup actions

![grafik](https://github.com/Ulf3000/Prevent-Sleep-for-Reaper/assets/10765339/fc4f8050-6894-4a8c-aae7-54928cba024c)


- the script should now run on reaper startup

# Linux an MacOS
for linux and macos similar apis should exist. Please replace the line:

ctypes.windll.kernel32.SetThreadExecutionState(ES_DISPLAY_REQUIRED)

with whatever your system api call or a simple mousemove or shiftclick (something which prevents the system and displays go to standby/sleep)

# Setup Python 

- this script is a python script so you need to setup python for use with reaper 

  ![grafik](https://github.com/Ulf3000/Prevent-Sleep-for-Reaper/assets/10765339/3355743e-f9aa-4a70-9702-16b6764d64b5)

  python is just a folder with s pecific subfolder structure , theres no need to install , set env or whatever.
  just unpack a python folder anywhere and set the dll in the reaper setting




