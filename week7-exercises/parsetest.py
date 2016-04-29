#!/usr/bin/env python
import argparse

def main():
  parser = argparse.ArgumentParser(
  description="Idempotent addition/removal of VLAN to Arista switch")
  parser.add_argument("vlan_id", help="VLAN number to create or remove", action="store", type=int)
  parser.add_argument("--name",help="Specify VLAN name",action="store",dest="vlan_name",type=str)
  parser.add_argument("--remove", help="Remove the given VLAN ID", action="store_true")
  print parser.parse_args()

if __name__ == "__main__":
  main()
