Bitte beachten Sie, dass pgrep und sdparm und python installiert sein muss.

Benutzung des Skripts:

###devices.conf####

In der Datei devices.conf werden die Geräte eingetragen, die in den Standby versetzt werden wollen.

Bsp:


/dev/sda
/dev/sdb
/dev/sdc


###protocol.conf###

In der Datei protocol.conf werden die Prozesse eingetragen werden die überprüft werden sollen. 
Wird der manuell gesetzte Schwellwert überschritten, wird der Spindown abgebrochen.
Der Prozess smb hat beispielsweise 2 Prozesse laufen wenn keiner über die Samba-Freigabe zugreift. 
Man schreibt also folgendes in die protocol.conf:

smb:2

Wird also der Wert 2 überschritten, wird kein Spindown eingeleitet.
Es können beliebig viele Prozesse in die protocol.conf eingetragen werden

Bsp:

smb:2
rsync:0
php5-fpm:3

usw.
