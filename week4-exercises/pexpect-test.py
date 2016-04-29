from getpass import getpass
import pexpect
import sys
import re
import time
import paramiko

def main():
  ip_addr = '50.76.53.27'
  username = 'pyclass'
  #password = getpass()
  password = '88newclass'
  port = 8022

  #hostname = re.compile(r'^pynet-rtr.*[1-2]#$', re.MULTILINE)

  # Spawns a command
  ssh_conn = pexpect.spawn('ssh -l {} {} -p {}'.format(username, ip_addr, port))

  #ssh_conn.expect('(yes/no)? ')
  #ssh_conn.sendline('yes')
  ssh_conn.timeout = 3
  ssh_conn.expect('ssword:')
  ssh_conn.sendline(password)
  ssh_conn.expect('#')

  ssh_conn.sendline('show ip int brief')
  ssh_conn.expect('#')
  print ssh_conn.before
  print ssh_conn.after

  ssh_conn.sendline('terminal length 0')
  ssh_conn.expect('#')
  ssh_conn.sendline('show version')
  ssh_conn.expect('pynet-rtr2#')
  print ssh_conn.before
  print ssh_conn.after

  ssh_conn.sendline('configure terminal')
  ssh_conn.expect('#')
  #ssh_conn.sendline('\n')
  #ssh_conn.expect('#')
  #time.sleep(1)
  print ssh_conn.before
  print ssh_conn.after

  ssh_conn.sendline('logging buffered 4096')
  ssh_conn.expect('#')
  print ssh_conn.before
  print ssh_conn.after

  ssh_conn.sendline('exit')
  ssh_conn.expect('#')
  print ssh_conn.before
  print ssh_conn.after
  
  ssh_conn.sendline('show logging')
  ssh_conn.expect('#')  
  #time.sleep(1)
  print ssh_conn.before
  print ssh_conn.after
  
  #ssh_conn.logfile = sys.stdout 
  #for line in  ssh_conn.logfile:
   # print line
if __name__ == "__main__":
  main()
