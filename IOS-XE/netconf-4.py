from ncclient import manager
from pprint import pprint
import xmltodict
import xml.dom.minidom

netconf_filter = """
 <filter>
   <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
     <interface>
       <name>GigabitEthernet1</name>
     </interface>
   </interfaces>
   <interfaces-state xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
     <interface>
       <name>GigabitEthernet1</name>
     </interface>
   </interfaces-state>
 </filter>
"""
with manager.connect(host="ios-xe-mgmt-latest.cisco.com", port=10000, username="developer", password="C1sco12345", hostkey_verify=False) as m:
    for capability in m.server_capabilities:
        print('*' * 50)
        print(capability)
        
    interface_netconf = m.get(netconf_filter)
    print("getting running config")
    
    #xmlDom = xml.dom.minidom.parseString(str(interface_netconf))
    #print(xmlDom.toprettyxml(indent=" "))
    #print('*' * 25 + 'Break' * 50)
    
    # XMLDICT for converting xml output to python dictionary
    interface_python = xmltodict.parse(interface_netconf.xml)[
        "rpc-reply"]["data"]
    pprint(interface_python)
    name = interface_python['interfaces']['interface']['name']['#text']
    print(name)
    
    config = interface_python['interfaces']['interface']
    op_state = interface_python['interfaces-state']['interface']
    
    print("Start")
    print(f"Name: {config['name']['#text']}")
    print(f"Description: {config['description']}")
    print(f"Packets In: {op_state['statistics']['in-unicast-pkts']}")
    print("End")
    