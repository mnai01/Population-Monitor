#!/usr/bin/python3
import nmap
import os.path

def NmapScan(filename):
    nm = nmap.PortScanner()
    # Scans local host
    # -sP This options tell snmap to do a port scan after host discovery.
    # It will only print out available hosts that respond to the host discovery probes.
    # This is often known as 'Ping Scan'
    nm.scan(hosts='raspberrypi.local/24', arguments='-sP')
    nm.command_line()

    # Returns Current directory of file
    currentDirectory = os.getcwd()

    # Using os.path.join to create/overwrite nmapScan.xml in specified directory
    # (Path Name, File Name)
    nmapfile = os.path.join(currentDirectory, filename)

    # return file object in write mode '-w'
    # this is opening nmapScan.xml
    file = open(nmapfile, 'w')

    # writes the output of nm.get_nmap_last_output() to nmapScan.xml
    file.write(nm.get_nmap_last_output())

    # closes the opened file
    file.close()

    # prints xml data for testing
    print(nm.get_nmap_last_output())
