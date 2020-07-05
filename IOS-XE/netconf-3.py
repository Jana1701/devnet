from ncclient import manager
import xml.dom.minidom

netconf_filter = """
 <filter>
   <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
     <interface>
       <name>GigabitEthernet3</name>
     </interface>
   </interfaces>
   <interfaces-state xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
     <interface>
       <name>GigabitEthernet3</name>
     </interface>
   </interfaces-state>
 </filter>
"""
with manager.connect(host="ios-xe-mgmt-latest.cisco.com", port=10000, username="developer", password="C1sco12345", hostkey_verify=False) as m:
    for capability in m.server_capabilities:
        print('*' * 50)
        print(capability)
        
    interface_netconf = m.get(netconf_filter)
    xmlDom = xml.dom.minidom.parseString(str(interface_netconf))
    print(xmlDom.toprettyxml(indent=" "))
    print('*' * 25 + 'Break' * 50)
    m.close_session()