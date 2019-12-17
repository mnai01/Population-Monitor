#!/usr/bin/python3
import xml.etree.ElementTree as ET

class Parse():
    def __init__(self):
        self.hostsUP = 0
        self.listofMAC = []
        self.listofIP = []
        self.listofVendor = []

    # @staticmethod
    def ParseXML(self, xmlfile):

        # EXAMBLE XML ELEMENT
        # <address addr='192.0.0.0' addrtype='ipv4' vendor='Apple'/>
        # address is the Element type name
        # addrtype is the Attribute name, 'ipv4' is the Attribute Value
        # vendor is an Attribute name, 'Apple' is the Attribute value

        # create element tree object
        tree = ET.parse(xmlfile)
        # get root element
        root = tree.getroot()

        # iterates through file and looks for 'address' element name
        for node_1 in tree.iter('address'):
            # Looks for Attribute name called 'addrtype'
            # that holds an Attribute value of 'ipv4'
            # Prints only ipv4 address, will work wihtout sudo
            if node_1.attrib.get('addrtype') == 'ipv4':
                addr = node_1.attrib.get('addr')
                # each time a new item is found it is added to the array
                str(self.listofIP.append(addr))
                print('IP Address: ', addr)

            # Print only mac address HAS TO RUN IN SUDO TO WORK
            # Looks for Attribute name called 'addrtype'
            # that holds an Attribute value of 'mac''
            if node_1.attrib.get('addrtype') == 'mac':
                addr = node_1.attrib.get('addr')
                # each time a new item is found it is added to the array
                str(self.listofMAC.append(addr))
                print('MAC Address: ', addr)
                # If a vendor Attribute name vendor is found in the mac address
                # store that vendor in the array, else store unknows in the array
                if node_1.attrib.get('vendor'):
                    vendor = node_1.attrib.get('vendor')
                    # each time a new item is found it is added to the array
                    str(self.listofVendor.append(vendor))
                    print('Vendor: ', vendor, '\n')
                else:
                    vendor = 'Unkown'
                    str(self.listofVendor.append(vendor))
                    print('Vendor: ', vendor, '\n')

        # iterates through file and looks for 'hosts' element name
        for node_1 in tree.iter('hosts'):
            # Looks for Attribute name called 'up'
            # Prints only number of hostUp, MIGHT HAVE TO RUN IN SUDO TO WORK
            if node_1.attrib.get('up'):
                self.hostsUP = node_1.attrib.get('up')
        # Since the hosted machine doesnt have a MAC or Vendor
        # You must append it at the end so all the arrays are the same length
        # The last IP added is the local machine so appending it at the end
        # places it in the correct spot based off that
        # its important to have all arrays length the same
        # when inserting into database
        # Checkout SQLServer.py to see why
        hs = int(self.hostsUP)
        self.listofMAC.append("HOST MACHINE")
        self.listofVendor.append("HOST MACHINE")
        print('MAC Address: ', self.listofMAC[hs-1])
        print('Vendor: ', self.listofVendor[hs-1])
        print('\n', 'Number of people on the network are: ' + self.hostsUP)
