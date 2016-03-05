#!/usr/bin/env python
import pyeapi

def main():
  connection = pyeapi.connect_to("pynet-sw3")
  existing_vlans = connection.api("vlans")
  my_vlans = range(100,999,50)
  for curr_vlan in my_vlans:
    if existing_vlans.get(curr_vlan):
      print("VLAN {} already exists".format(curr_vlan))
    else:      
      existing_vlans.create(curr_vlan)
      name = "TEST_VLAN_" + str(curr_vlan)
      existing_vlans.set_name(str(curr_vlan), name)

if __name__ == "__main__":
  main()
