from setuptools import Command
from nxosapi import *
from inventory import *
from cmdset import generic_show
from reporting import *

############################

# define required logic:
# - list of cmds;
# - limit to device types;
# - select user.

############################

# function to import inventory.csv and create list of objects

# def inventory_import(csv)
# def inventory_create()

############################

# function to post data to devices in inventory

if __name__ == '__main__':
    username = chris_obj.name
    password = chris_obj.pwd
    for ip in deviceIPs:
        url = 'https://' + ip + '/ins'
        nxapi_post(url, {'content-type': 'application/json'}, generic_show("show version"), username, password)

#        for port in value['interfaces']:
#            nxapi_post(url, {'content-type': 'application/json-rpc'}, ospf_interface(port, "UNDERLAY"), username, password)

