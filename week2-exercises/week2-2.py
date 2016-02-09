import telnetlib

def show_int(ip_address,username,password,timeout):
  tn = telnetlib.Telnet(ip_address, 23, 6)
  tn.read_until('Username:', timeout)
  tn.write(username + '\n')
  tn.read_until('Password:', timeout)
  tn.write(password + '\n')
  tn.read_until('pynet-rtr1#', timeout)
  tn.write('show ip int brief' + '\n')
  output = tn.read_until('pynet-rtr1#', timeout)
  tn.close()
  return output

def main():
  test = show_int('50.76.53.27','pyclass','88newclass',1)
  print test
  
if __name__ == '__main__':
  main()
