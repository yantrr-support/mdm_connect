__author__ = 'yantrr'
#
# This program is free software: you can redistribute it and/or modify 	#
# it under the terms of the GNU General Public License as published by 	#
# the Free Software Foundation, either version 3 of the License, or    	#
# at your option) any later version.                                   	#
#                                                                      	#
# This program is distributed in the hope that it will be useful,      	#
# but WITHOUT ANY WARRANTY; without even the implied warranty of       	#
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the        	#
# GNU General Public License for more details.                         	#
#                                                                      	#
# You should have received a copy of the GNU General Public License    	#
# with this program.  If not, see <http://www.gnu.org/licenses/>.      	#
#########################################################################


import serial
import sys
from contextlib import closing
import os


#gets Serial prt settings from settings.txt################################
global PORT
PORT = None
global BAUD
BAUD = None


def getSerialSettings():
	global PORT
	global BAUD

	with open("settings.txt") as f: # read the file for one time settings
	 for line in f:
	        args=line.replace('\n','').split(" ")
		if args[0].lower() == "port":
			PORT = args[1]
		elif args[0].lower() == "baud":
			BAUD = args[1]
		else:
			 pass

	if PORT==None or BAUD==None:
		print "****ERROR BAD SYNTAX -> Check \"settings.txt\" file \n\
	Syntax is:\n PORT(space)/dev/ttyUSB*(RETURN)\
	\n BAUD(space)9600(RETURN)"

	else:
		print "OPENING MODEM SERIAL  CONNECTION#######\nPort: " + PORT + "\n" "Baud: " + BAUD
		print "################################"
###########################################################################


#Check if Modem Respond to AT CMD
def heartBeat():

    resp = runATCmd('AT')
    BAD_REPLIES = ['AT','']
    resp = [r for r in resp if r not in BAD_REPLIES]
    if resp[0] == "OK":
        print "Modem replied, communications OK....."
        return True
    else:
        print "Failed to talk to Modem, is it on? Is the port free?"
        print "Check the Modem Enablement using GPIO"
        sys.exit(1)



def runATCmd(cmd,timeout=5,retries=2):
        """Returns the response of AT COMMAND"""
        eol='\r\n'
        cmd = cmd+eol

        try:
            with closing(serial.Serial(PORT,BAUD,timeout=5)) as ser:
                retries = retries - 1
                # ser.write(cmd)
                # ser.readlines()
                ser.flushOutput()
                ser.flushInput()
                ser.write(cmd)
                lines = ser.readlines()
                # clean up \r\n as pairs or singles and avoid unsolicited notifications
                resp = [r for r in [l.strip('\r\n') for l in lines
                            if not l.startswith(('^', '_'))]]
                if resp:
                    print "SENT COMMAND %s response: %s" % (cmd,resp)
                    return resp
                elif retries:
                    return runATCmd(cmd,timeout=5,retries=retries)

                else:
                    raise ValueError("Reply from modem %s was meaningless: %s"
                                    % (PORT, lines))
        except serial.SerialException,e:
            print "SERIAL FAILURE: ",e
            print "CHECK settings.txt file"


def serialOpenCheck():
    getSerialSettings()
    heartBeat()
    return True
###############################################################################

serialOpenCheck()


