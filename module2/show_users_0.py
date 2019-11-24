import openstack

conn = openstack.connect(cloud="openstack")


def list_users(conn):
    print("List of Users:")

    for user in conn.identity.users():
        print user

list_users(conn)
