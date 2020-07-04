from ncclient import manager
import xml.dom.minidom

netconf_filter = """
<filter>
 <


with manager.connect(host="ios-xe-mgmt-latest.cisco.com", port=10000, username="developer", password="C1sco12345", hostkey_verify=False) as m:
    for capability in m.server_capabilities:
        print('*' * 50)
        print(capability)
    m.close_session()