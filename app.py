# import requests

# API_link = "https://api.telegram.org/bot5556875821:AAFW74WSAcNSF1ATvLE16HySso_qpelO4kE"

# updates = requests.get(API_link + "/getUpdates?offset=-1").json()

# print (updates)

# message = updates["result"][0]["message"]

# chat_id = message["from"]["id"]
# text = message["text"]
# sent_messeage = requests.get(API_link + f"sendMessage?chat_id={chat_id}&text=dkdo{text}")
# # sent_message = requests.get(API_link + f"/sendMessage?chat_id={chat_id}&text = Салом сиз хозир {text} ёздингиз")

# import aiogram