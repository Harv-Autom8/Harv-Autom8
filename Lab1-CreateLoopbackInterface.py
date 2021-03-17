import getpass
import telnetlib

HOST = "192.168.0.220"
user = input("Enter your username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user + "\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password + "\n")

tn.write("enable\n")
tn.write("cisco\n")
tn.write("conf t\n")
tn.write("int loop0\n")
tn.write("ip address 1.1.1.1 255.255.2555.255\n")
tn.write("end\n")
tn.write("exit\n")

print (tn.read_all)
