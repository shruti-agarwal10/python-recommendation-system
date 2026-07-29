import json

def load_data(filename):
    with open(filename, "r") as f:
        data = json.load(f)
    return data

data = load_data("data.json")
print(data)
print(type(data))

def display_user(data):
    print("\nUser and their connections:\n")
    for user in data['users']:
        print(f"Id: {user['id']} - {user['name']} and their friends: {user['friends']} with liked pages: {user['liked_pages']}")
    print("\nPage Information:\n")
    for page in data['pages']:
        print(f"{page['id']}: {page['name']}")

display_user(data)