
from copy import copy
import xml.etree.cElementTree as ET

def get_root(xml_file):
    with open(xml_file, mode='rb') as file:
        xml_data = file.read().decode('utf-8')
        xml_data = ''.join(xml_data.split('\n'))
        xml_data = ''.join(xml_data.split('\t'))
    root = ET.fromstring(xml_data)
    # root = tree.getroot()
    return root

def to_dict(r, root=True):
    if root:
        return {r.tag : to_dict(r, False)}
    d = copy(r.attrib)
    for x in r.findall('./*'):
        if x.tag not in d:
            d[x.tag] = to_dict(x, False)
        if x.text:
            d[x.tag] = x.text
    return d

if __name__=="__main__":
    testfile = 'data.xml'
    root = get_root(testfile)
    result = to_dict(root)
    print(result)