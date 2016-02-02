import re
from ciscoconfparse import CiscoConfParse

def main():
  cisco_cfg = CiscoConfParse("cisco_ipsec.txt")

  cryptomaps = cisco_cfg.find_objects_wo_child(parentspec = r"crypto map CRYPTO", childspec = r"AES")
  print "\ncrypto maps not using AES:"
  for entry in cryptomaps:
    print "{0}" .format(entry.text)
    for text in entry.children:
      if 'transform-set' in text.text: 
        print re.sub('set transform-set ','',text.text)

if __name__ == "__main__":
  main()
