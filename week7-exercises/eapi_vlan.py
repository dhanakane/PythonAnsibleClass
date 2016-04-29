import pyeapi
import argparse

# Take a VLAN ID and name and create the VLAN and name it if it does not exist on a switch, or amend the name if it exists and the name is incorrect.
def vlan_create(new_vlan_id, new_vlan_name):
  connection = pyeapi.connect_to("pynet-sw3")
  existing_vlans = connection.api("vlans")
  vlan_check = existing_vlans.get(new_vlan_id)
  if vlan_check and vlan_check['name'] != new_vlan_name:
    print('VLAN EXISTS, BUT NAME IS INCORRECT')
    existing_vlans.set_name(str(new_vlan_id), new_vlan_name)
    print("Amended VLAN {} with name {}".format(new_vlan_id, new_vlan_name))
  elif vlan_check == 'None':
    existing_vlans.create(new_vlan)
    name = new_vlan_name
    existing_vlans.set_name(str(new_vlan_id), new_vlan_name)
    print("created VLAN {} with name {}".format(new_vlan_id, new_vlan_name))
  elif vlan_check and vlan_check['name'] == new_vlan_name:
    print('VLAN EXISTS AND NAME IS CORRECT')

def vlan_delete(vlan_delete):
  connection = pyeapi.connect_to("pynet-sw3")
  vlans_api = connection.api("vlans")
  if vlans_api.get(vlan_delete):
    vlans_api.delete(vlan_delete)
    print("Deleting VLAN {}".format(vlan_delete))
  else:
    print("VLAN {} does not exist".format(vlan_delete))

def main():
  parser = argparse.ArgumentParser(description = 'enter VLAN name and ID to be added\/removed')
  
  subparsers = parser.add_subparsers(help='commands')

  create_parser = subparsers.add_parser('create', help = 'create a VLAN')
  create_parser.add_argument('vlan_name', action = 'store', help = 'VLAN name to create')
  create_parser.add_argument('vlan_id', action = 'store', type = int, help = 'VLAN id to create')

  delete_parser = subparsers.add_parser('delete', help = 'delete a VLAN')
  delete_parser.add_argument('vlan_id', action = 'store', type = int)
  delete_parser.add_argument('vlan_name', action = 'store_false')

  eapi_args = parser.parse_args()
  print eapi_args
  
  if eapi_args.vlan_name:
    vlan_create(eapi_args.vlan_id, eapi_args.vlan_name)
  elif not eapi_args.vlan_name and eapi_args.vlan_id:
    vlan_delete(eapi_args.vlan_id) 

if __name__ == "__main__":
  main()
