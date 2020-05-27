
from twilio.rest import Client
import json
import sys
import yaml
import random
from sklearn.utils import shuffle

# TODO 1 : Register a twilio account and update the following informaiton. 
# DANGER! This is insecure. See http://twil.io/secure
account_sid = '<enter your sid here>'
auth_token = '<enter your auth token here>'


# TODO 2: Add your players name and phone numbers, you can copy them from Sandbox.
players={
        "contacts": 
        [
            {"name" : "John", "phone" : "6667778888"},
            {"name" : "George", "phone" : "6667778888"},
            {"name" : "Nikki", "phone" : "6667778888"},
            {"name" : "Ramen", "phone" : "6667778888"},
            {"name" : "Ben", "phone" : "6667778888"},
            {"name" : "Tiff", "phone" : "6667778888"},
            {"name" : "Meghan", "phone" : "6667778888"},
            {"name" : "James", "phone" : "6667778888"}
        ]
    }

def my_shuffle(array):
    random.shuffle(array)
    return array      

# TODO 3: Enter the number of werewolve's and seer here. Change it to Mafia, Doctor if required.
nos_werewolf = 2
nos_seer = 1

nos_villagers = len(players['contacts']) - (nos_werewolf + nos_seer)
roles = ['WereWolf']*nos_werewolf+ ['Seer']*nos_seer + ['Villager']*nos_villagers
roles = my_shuffle(roles)

# TODO 4: (Optional) you can also shuffle the users to accomplish a better shuffle.
# If you want to make someone a mafia/werewolf, who haven't got the chance so far. Add additional code hardcoding manually. 
players_json_str = json.dumps(players)
roles_json_str = json.dumps(roles)

players_resp = yaml.safe_load(players_json_str)
roles_resp = yaml.safe_load(roles_json_str)

client = Client(account_sid, auth_token)

count = 0
for role in roles_resp:
        print('------------------------')
        print(players_resp['contacts'][count]["name"])
        print(players_resp['contacts'][count]["phone"])
        print(role)
        # message = client.messages.create(
        #                             from_='whatsapp:+14155238886', #Twilio's default sandbox from phone number, change it if twilio changes it.
        #                             body='Hello, ' + players_resp['contacts'][count]["name"] +'! You are a: ' + role,
        #                             to='whatsapp:+1' + players_resp['contacts'][count]["phone"]
        #                         )
        count = count + 1
        print('------------------------')

  
