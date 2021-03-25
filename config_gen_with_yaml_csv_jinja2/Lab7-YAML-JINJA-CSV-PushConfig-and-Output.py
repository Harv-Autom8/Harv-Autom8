import yaml
import netmiko
from netmiko import ConnectHandler
import jinja2
import time
import threading
import csv
from jinja2 import Template



with open("hosts.yaml") as f:
    hosts = f.read()
print(hosts)
yaml_dict = yaml.safe_load(hosts)




x = input("Enter your Station Name: ")
site_code = yaml_dict["GWAN"][x]['code']
if yaml_dict["GWAN"][x]['code'] is None:
    raise KeyError('Site {} is not specified in inventory YAML file'.format(site_code))
print(site_code)

ipaddr = "192.168.0."+str(site_code)
print(ipaddr)

interface_template_file = "switchport-interface-template.j2"

# print multiple configs place holder
interface_configs = ""


#opens Jinja2 Template file
with open(interface_template_file) as f:
    interface_template = Template(f.read(), keep_trailing_newline=True)

source_file = "switch-ports.csv"

with open(source_file) as f:
    reader = csv.DictReader(f)
    for row in reader:
        interface_config = interface_template.render(
            interface = row["Interface"],
            vlan = row["VLAN"],
            server = row["Server"],
            link = row["Link"],
            purpose = row["Purpose"]
        )
        interface_configs += interface_config

with open("interface_configs.txt", "w") as f:
    f.write(interface_configs)


net_connect = ConnectHandler(device_type="cisco_ios", ip=ipaddr, username="harv", password="cisco")
config_set = interface_configs.split("\n")
print(config_set)

output = net_connect.send_config_set(config_set)
print(output)