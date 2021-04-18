from ncclient import manager

iosxe_host = "10.99.15.226"
netconf_port = "830"
username = ""
password = ""

def get_capabilities():
    """
    Method that prints NETCONF capabilities of the remote device
    """
    with manager.connect(
        host=iosxe_host,
        port=netconf_port,
        username=username,
        password=password,
        hostkey_verify=False
    ) as device:

    print('\n***NETCONF Capabilities for device {}***\n'.format(iosxe_host))
    for capability in device.server_capabilities:
        print(capability)

if __name__ == '__main__':
    get_capabilities()