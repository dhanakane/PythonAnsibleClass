#!/usr/bin/env python

import pyeapi
from eapi_vlan import vlan_create, vlan_delete
from ansible.module_utils.basic import *

def main():

  module = AnsibleModule(
    argument_spec = dict(
    vlan_id = dict(required=True),
    vlan_name = dict(required=False)
    )
  )

if __name__ == "__main__":
  main()
