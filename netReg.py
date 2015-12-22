__author__ = 'root'
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
import YTR_SER
import re

def process_netreg_status(info):
        """Processes get_netreg_status callback and reacts accordingly"""
        BAD_REPLIES = ['AT+CREG?', 'OK', '']
        resp = [r for r in info if r not in BAD_REPLIES]
        p_resp=re.split(':|,|"',resp[0])
        # Sample respose:p_resp : ['+CREG', ' 2', '1', '791D', '0FB7', '0']
        p_resp=filter(None,p_resp) # remove all empty strings from that so indexing would be normal.
        return p_resp
        # Returns list of the process result, develop logic based on this.


cmd='AT+CREG=2'
res = YTR_SER.runATCmd(cmd)
cmd ='AT+CREG?'
try:
    res = YTR_SER.runATCmd(cmd)
    reg_status = process_netreg_status(res)
except:
    print "Some Exception"




