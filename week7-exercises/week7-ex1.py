#!/usr/bin/env python
#from __future__ import unicode_literals
import pyeapi

def main():
  #pynet_sw3_raw = pyeapi.connect(transport='https', host='50.76.53.27', username='admin1', password='99saturday', port=8443, timeout=60, return_node=False)
  pynet_sw3 = pyeapi.connect_to("pynet-sw3")
  show_interfaces = pynet_sw3.enable("show interfaces")
  response_list = show_interfaces[0]
  #print response_list.keys()
  #print response_list['result'].keys()
  #for dict in response_list['result']
  for interface in response_list['result'][u'interfaces']:
    if u'interfaceCounters' in response_list['result'][u'interfaces'][interface].keys():
      print("{} InOctets: {}".format(interface, response_list['result'][u'interfaces'][interface][u'interfaceCounters'][u'inOctets']))
      print("{} OutOctets: {}".format(interface, response_list['result'][u'interfaces'][interface][u'interfaceCounters'][u'outOctets']))
  #config = pynet_sw3.get_config()
  #print config
  
if __name__ == "__main__":
  main()

