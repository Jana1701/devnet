from ncclient import manager
#change1
with manager.connect(host="ios-xe-mgmt-latest.cisco.com", port=10000, username="developer", password="C1sco12345", hostkey_verify=False) as m:
    m.close_session()