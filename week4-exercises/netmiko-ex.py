from netmiko import ConnectHandler
from getpass import getpass

password = getpass()
#username = getpass.getuser()

pynet1 = {
           'device_type' : 'cisco_ios',
           'ip' : '50.76.53.27',
           'username' : 'pyclass',
           'password' : password,
}

pynet2 = {
           'device_type' : 'cisco_ios',
           'ip' : '50.76.53.27',
           'username' : 'pyclass',
           'password' : password,
           'port' : 8022,
}

juniper_srx = {
           'device_type' : 'juniper',
           'ip' : '50.76.53.27',
           'username' : 'pyclass',
           'password' : password,
           'secret' : '',
           'port' : 9822,
}

def arp_print(device_list):
  for device in device_list:
    print("connecting to {0}".format(device))
    device_connection = ConnectHandler(**device)
    if device['device_type'] == 'cisco_ios':
      print("device type is {0}".format(device['device_type']))
      output = device_connection.send_command('show ip arp')
      print output
    elif 'juniper' in device['device_type']:
      print("device type is {0}".format(device['device_type']))
      output = device_connection.send_command('show arp')
      print output

def main():
  '''
  pynet_rtr1 = ConnectHandler(**pynet1)
  output = pynet_rtr1.config_mode()
  print pynet_rtr1.check_config_mode()
  pynet_rtr1.exit_config_mode()
  output = pynet_rtr1.send_command('show ip arp')
  print output
  '''
  device_list = [pynet1, pynet2, juniper_srx]
  arp_print(device_list)

if __name__ == "__main__":
  main()
