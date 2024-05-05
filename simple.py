import json
import random
from instagrapi import Client

def load_random_bio(json_file_path):
    with open(json_file_path, 'r') as file:
        bios = json.load(file)['bios']
    return random.choice(bios)

def update_instagram_bio(username, password, new_bio):
    cl = Client()
    cl.login(username, password)
    cl.account_edit(biography=new_bio)

if __name__ == "__main__":
    username = 'your_instagram_username'
    password = 'your_instagram_password'
    json_file_path = '/workspaces/instagram-bio-auto_update/bios.json'
    
    new_bio = load_random_bio(json_file_path)
    update_instagram_bio(username, password, new_bio)
    print(f"Updated bio: {new_bio}")