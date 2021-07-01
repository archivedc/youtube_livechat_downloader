from chat_downloader import ChatDownloader
import json
import sys

url = sys.argv[1]
chat = ChatDownloader().get_chat(url, message_groups=[
    'messages', 'superchat'])

chat_json = list()

for message in chat:
    chat_json.append(message)

with codecs.open(sys.argv[2], 'w', 'utf_8') as ft:
    json.dump(ft)
