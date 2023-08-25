import requests
import json

webhook_url = "https://discord.com/api/webhooks/1144729027391803492/kU8WgZgUQQopE5tjhe_Q5GtL0LOPL0_f5FqtLZqd7yKkkyXX8wwd13Jv5-fbgmK6bQXq"
username = "HaZaRd"
avatar_url = "https://cdn.discordapp.com/attachments/1144660953498136666/1144729844530282557/artworks-43CHzgWVauWOMRp8-q43XYA-t500x500.jpg"
message = "Hello _ Im HaZaRd"

payload = {
    "content":message,
    "username": username,
    "avatar_url": avatar_url
}

response = requests.post(webhook_url,json=payload)

if response.status_code == 204:
    print("Message Sent SuccessFully!")
else:
    print("Failed to Send message.", response.status_code)