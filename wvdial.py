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
import YTR_SER
bin_path = '/usr/bin/wvdial'
conf_path = 'wad.conf'
import subprocess

print "starting Wvdial connect"
proc = subprocess.Popen([bin_path, '-C', conf_path, 'connect'],bufsize=2,
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        )

with proc.stderr:
    for line in iter(proc.stderr.readline, b''):#iter() is used to read lines as soon
        print line,
proc.wait() # wait for the subprocess to exit

