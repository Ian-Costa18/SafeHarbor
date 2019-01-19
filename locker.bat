@echo off

set hwid=%1

runas /user:Administrator /savecred "devcon disable "USBSTOR\DISK""