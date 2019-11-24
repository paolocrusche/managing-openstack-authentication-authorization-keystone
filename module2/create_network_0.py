import openstack
import json

conn = openstack.connect(cloud="application_rev01")

def create_network(conn):
    print("Create Network:")

    example_network = conn.network.create_network(name='pluralsight-network-example')

    example_subnet = conn.network.create_subnet(
        name='pluralsight-subnet-example',
        network_id=example_network.id,
        ip_version='4',
        cidr='10.0.2.0/24',
        gateway_ip='10.0.2.1')

    print json.dumps(example_subnet, indent=2)
 
create_network(conn)
