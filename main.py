#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os

####Protokoll####

#Schaue welche Prozesse gecheckt werden sollen
protocolFile = open("protocol.conf")
protocol = []

#lese Protokolle aus
for line in protocolFile:
    protocol.append(line.rstrip())

protocolFile.close()

#Temporäre Protokoll Variable
swapProtoValue = []
spindown = False;

#Teile Protokoll Parameter
for i in range (len(protocol)):
   #Teile sobald ein : kommt
   swapProtoValue = protocol[i].split(":")

   # Protokoll/Prozessname
   proto = swapProtoValue[0]
   #Manuell gegebener Schwellwert
   value = swapProtoValue[1]
   
   #Erstelle configurationsfile für Protokoll/Prozess
   setPgrepFile = proto + ".conf"
   if os.path.exists(setPgrepFile):
       os.system('rm -r ' + setPgrepFile)

   #Lese Prozess mit pgrep aus und schreibe wert in das Konfigurationsfile
   os.system('pgrep -c ' + proto + '>> ' + setPgrepFile)
   pgrep = open(setPgrepFile, "r")


   for line in pgrep:
       pgrep1 = line.rstrip()

   pgrep.close()
    
   #Konviertiere Werte von String zu integer
   pgrepInt = int(pgrep1)
   valueInt = int(value)

   print "-" * 25
   print "Protokoll: %s" %proto
   print "Spindown Wert:     %i" %valueInt
   print "Tatsächlicher Wert: %i" %pgrepInt

   if pgrepInt > valueInt:
       print "Kein Spindown"

   else:
       spindown = True

if spindown == False:
    print "-" * 25
    print "Es wird kein Spindown ausgeführt!"
    exit(0)

else:
    print "-" * 25
    print ("Bereite Spindown vor")

####DEVICES####

    deviceFile = open("devices.conf")
    devices = []

    print "Initialisiere Geräte..."
    for line in deviceFile:
        devices.append(line.rstrip())
    deviceFile.close()
    
    print"-" * 25
    print"Folgende Geräte wurden initialisiert:"
    for i in range(len(devices)):
        print"Gerät %i: %s" %(i+1,devices[i])

 #Geräte werden mit sdparm synchronisiert
    print"-" * 25   
    print"Synchronisiere Geräte"
    print"-" * 25
    for i in range (len(devices)):
        os.system('sdparm --command=sync ' + devices[i])

#Geräte werden mit sdparm gestoppt

    print"-" * 25
    print"Stoppe Geräte"
    print"-" * 25
    for i in range (len(devices)):
        os.system('sdparm --command=stop ' + devices[i])
    
    print"-" * 25
    print"Fertig!"

#END OF FILE















