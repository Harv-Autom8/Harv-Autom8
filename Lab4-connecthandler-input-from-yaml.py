import yaml
import netmiko
from netmiko import ConnectHandler

with open("hosts.yaml") as f:
    hosts = f.read()
print(hosts)
yaml_dict = yaml.safe_load(hosts)


def station_input():

    x = input("Enter your Station Name: ")
    site_code = yaml_dict["GWAN"][x]['code']
    if yaml_dict["GWAN"][x]['code'] is None:
        raise KeyError('Site {} is not specified in inventory YAML file'.format(site_code))
    print(site_code)

    ipaddr = "192.168.0."+str(site_code)
    print(ipaddr)
    connection_to_devices(ipaddr)


def connection_to_devices(ipaddr):

    net_connect = ConnectHandler(device_type="cisco_ios", ip=ipaddr, username="harv", password="cisco")
    output = net_connect.send_command('show ip int brief')
    print(output)

def main():
    station_input()
    station_input()
    print("You have reached the end of the script")


if __name__ == '__main__':
    main()














