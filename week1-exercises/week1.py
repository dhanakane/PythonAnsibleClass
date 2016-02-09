# print('Hello World')
import yaml
import json
from pprint import pprint

def niceprint(input_list, filetype):
  print '\n\n\n'
  print '###'
  print '###' + filetype + '###'
  print '###'
  pprint(input_list)

def main():

  testlist = range(8)
  testlist.append('something')
  testdict1 = {'ip1' : '10.1.1.1', 'ip2' : '20.1.1.1'}
  testlist.append(testdict1)
  testlist[-1]['attribs'] = range(99,109)

#print testlist
#print yaml.dump(testlist, default_flow_style = False)

  with open("week1.yml",'w') as f:
    f.write(yaml.dump(testlist, default_flow_style = False))
  with open('week1.json','w') as f:
    json.dump(testlist,f)

  with open("week1.yml") as f:
    yamllist = yaml.load(f)
  #pp(yamllist)

  with open("week1.json") as f:
    jsonlist = json.load(f)
  #pp(jsonlist)

  niceprint(yamllist, 'YAML')
  niceprint(jsonlist, 'JSON')

if __name__ == "__main__":
  main()
