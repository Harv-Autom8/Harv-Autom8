import getpass
import telnetlib

HOST = "192.168.0.220"   ##inside quotes = string###
user = input("Enter your Username: ")
pwd = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if pwd:
    tn.read_until(b"Password: ")
    tn.write(pwd.encode('ascii') + b"\n")

tn.write(b"show ip access-list CSD_ACL\n")
tn.read_until(b'CSD_ACL')
tn.write(user.encode('ascii') + b"\n")

tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))