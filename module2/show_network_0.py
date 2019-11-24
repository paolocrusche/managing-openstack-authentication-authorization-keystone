import openstack
import json

conn = openstack.connect(cloud="application")


def list_networks(conn):
    print("List Networks:")

    for network in conn.network.networks():
        print json.dumps(network, indent=2)

list_networks(conn)
