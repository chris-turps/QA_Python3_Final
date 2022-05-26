class Device:
    def __init__(self
        , hostname_txt
        , ip_txt
    ):
        self.hostname = hostname_txt
        self.ip = ip_txt

ls1a_5a5_diva_obj = Device("ls1a-5a5-diva", "1.1.1.1")
ls1b_5a5_diva_obj = Device("ls1b-5a5-diva", "1.1.1.2")
 
deviceList = [ls1a_5a5_diva_obj, ls1b_5a5_diva_obj]
# print(deviceList)
deviceTypes = [device.hostname for device in deviceList]
deviceIPs = [device.ip for device in deviceList]
print(deviceTypes)
print(ls1a_5a5_diva_obj.ip)
print(deviceIPs)

#    n9kvs = {
#                'n9kv-s1':
#                    {
#                        'mgmt': '10.1.10.11',
#                        'router-id': '10.10.10.11',
#                        'interfaces': ['1/1', '1/2']
#                    },
#                'n9kv-l1':
#                    {
#                        'mgmt': '10.1.10.21',
#                        'router-id': '10.10.10.21',
#                        'interfaces': ['1/1']
#                    },
#                'n9kv-l2':
#                    {
#                        'mgmt': '10.1.10.22',
#                        'router-id': '10.10.10.22',
#                        'interfaces': ['1/1']
#                    },
#            }

