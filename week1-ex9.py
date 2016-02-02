import re
from ciscoconfparse import CiscoConfParse

def main():
  cisco_cfg = CiscoConfParse("cisco_ipsec.txt")

  cryptomaps = cisco_cfg.find_objects_w_child(parentspec = r"crypto map CRYPTO", childspec = r"pfs group2")
  print "\n crypto maps using PFS group2:"
  for entry in cryptomaps:
    print "  {0}" .format(entry.text)

if __name__ == "__main__":
  main()
