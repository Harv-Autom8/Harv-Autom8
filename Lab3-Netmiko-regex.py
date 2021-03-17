import netmiko
import re
from netmiko import ConnectHandler

iosv_l2_s1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.0.220',
    'username': 'harv',
    'password': 'cisco',
}

net_connect = ConnectHandler(**iosv_l2_s1)
output = net_connect.send_command('show ip access-list CSD_ACL')
regexoutput = re.search('20\..', output)
print(regexoutput.group(0))
