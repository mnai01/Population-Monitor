from NmapScanner import NmapScan
#from Parse import ParseXML
#from Parse import *
from SQLServer import *

# The file name that will be created from nmap and parsed
filename = 'nmapScan.xml'
NmapScan(filename)
#x = ParseXML(filename)
SendToServer()
