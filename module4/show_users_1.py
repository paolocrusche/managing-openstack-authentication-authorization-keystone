import openstack
import json
import pprint

conn = openstack.connect(cloud="james.page")


def list_users(conn):
    print("List of Users:")

    for user in conn.identity.users():
        print(json.dumps(user, indent=2))


list_users(conn)
