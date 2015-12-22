# mdm_connect
Simple Routine to configure PPP connection on embedded linux running on VIBE platform

These python routine are simple routine to get started with modem PPP connection on VIBE and VAYU Platform.

##Pre-requisite 
* wvdial package for debian, apt-get install wvdial
* python 2.6 or later 

## Usage 
* Enable the modem on the IoT platform based on wiki (http://www.yantrr.com/wiki/Main_Page )
* Each modem has different CMD and Data USB port, once modem is successfully enabled using the GPIO as explained in wiki, the system would populate /dev/ttyUSB*, kindly make a note of it
* Download the repository and edit following: 
* * setting.txt --> change the AT CMD port number, dont put the ttyUSBx which corresponds to data connect, example port in setting.txt is ttyUSB2
* * wad.conf file, this is the wvdial.conf file for your network
* run YTR_SER.py to check modem communication to AT COMMAND (AT = OK)
* run wvdial.py to connect to the network provided you have correct wvdial command line working

## Developing your own AT COMMAND sequence 

Since modem can be controlled in runtime  solely based on AT COMMAND port, YTR_SER.py gives module to communicate with modem using AT COMMAND, for any command sequence say 'AT+CREG?' to test the registration.

Simply import YTR_SER  and run the command sequence, see netReg.py for an example. One need to write the AT response processing using regular expressions 

=== Output of netReg.py ===
OPENING MODEM SERIAL  CONNECTION#######
Port: /dev/ttyUSB2
Baud: 115200
################################
SENT COMMAND AT
 response: ['AT', 'OK']
Modem replied, communications OK.....
SENT COMMAND AT+CREG=2
 response: ['AT+CREG=2', 'OK']
SENT COMMAND AT+CREG?
 response: ['AT+CREG?', '+CREG: 2,1, 9D68, 8FEDAB7', '', 'OK']





