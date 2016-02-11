import telnetlib
import time
import socket
import sys
import getpass

TELNET_PORT = 23
TELNET_TIMEOUT = 6


class TelnetShow:
  def __init__(self, ip_addr, username, password):
    #TELNET_PORT = 23
    #TELNET_TIMEOUT = 6

    self.ip_addr = ip_addr
    self.username = username
    self.password = password

    try:
      self.remote_conn = telnetlib.Telnet(self.ip_addr, TELNET_PORT, TELNET_TIMEOUT)
    except socket.timeout:
      sys.exit('connection timed out')

  def login(self):
    output = self.remote_conn.read_until('sername:', TELNET_TIMEOUT)
    self.remote_conn.write(self.username + '\n')
    output += self.remote_conn.read_until('assword:')
    self.remote_conn.write(self.password + '\n')
    output += self.remote_conn.read_until('#')
    print output

  def send_command(self, command):
    self.command = command.rstrip()
    self.remote_conn.write(self.command + '\n')
    time.sleep(1)
    return self.remote_conn.read_very_eager()

  def disable_paging(self, paging_cmd = 'terminal length 0'):
    return self.send_command(paging_cmd)

def main():
  ip_address = raw_input("IP Address: ")
  ip_address = ip_address.strip()
  username = 'pyclass'
  password = getpass.getpass()
  x = TelnetShow(ip_address, username, password)
  #print x.ip_addr
  #print x.username
  #print x.password
  x.login()
  x.disable_paging()
  output = x.send_command('show ip int brief')
  print output
  output = x.send_command('show run')
  #print output
  #x.send_command('show ip int brief')

if __name__ == '__main__':
  main()
