import openstack
import json

conn = openstack.connect(cloud="application_rev01")


def list_users(conn):
    print("List of Users:")

    for user in conn.identity.users():
        if user['name'] == "james.page":
		print(json.dumps(user, indent=2))

list_users(conn)

