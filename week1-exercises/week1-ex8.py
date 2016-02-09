import re
from ciscoconfparse import CiscoConfParse

def main():
  cisco_cfg = CiscoConfParse("cisco_ipsec.txt")

  cryptomaps = cisco_cfg.find_objects(r"^crypto map CRYPTO")
  print "\n crypto maps:"
  for entry in cryptomaps:
    print "{0}" .format(entry.text)
    for childtext in entry.children:
      print childtext.text

if __name__ == "__main__":
  main()
