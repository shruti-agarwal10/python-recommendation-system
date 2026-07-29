import json

def clean_data(data):
    data["users"] = [user for user in data["users"] if user["name"].strip()]
    
    for user in data["users"]:
        user['friends'] = list(set(user['friends']))
        
    data["users"] = [user for user in data['users'] if user['friends'] or user['liked_pages']]
    
    unique_pages = {}
    for page in data['pages']:
        unique_pages[page['id']] = page
    data['pages'] = list(unique_pages.values())
        
    return data

data = json.load(open("data2.json"))
data = clean_data(data)
json.dump(data, open("cleaned_data.json", "w"), indent=4)
print("Data has been cleaned.") 