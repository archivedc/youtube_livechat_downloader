import json
import csv
import sys
import codecs

with codecs.open(sys.argv[1], 'r', 'utf_8') as ff:
    json = json.load(ff)
    with codecs.open(sys.argv[2], 'w', 'utf_8') as ft:
        w = csv.writer(ft)
        w.writerow(
            ['unixtime', 'seconds', 'author_channel_id', 'author', 'type', 'message_or_sticker', 'price', 'currency'])
        for message in json:
            message_type = message['message_type']
            try:
                towrite = None
                if (message_type == 'text_message'):
                    towrite = [message['timestamp'], message['time_in_seconds'],
                               message['author']['id'], message['author']['name'], message_type, message['message']]
                elif (message_type == 'paid_message'):
                    towrite = [message['timestamp'], message['time_in_seconds'],
                               message['author']['id'], message['author']['name'], message_type, message.get(
                                   'message', ''),
                               message['money']['amount'], message['money']['currency']]
                elif (message_type == 'membership_item'):
                    towrite = [message['timestamp'], message['time_in_seconds'],
                               message['author']['id'], message['author']['name'], message_type, message['message']]
                elif (message_type == 'paid_sticker'):
                    towrite = [message['timestamp'], message['time_in_seconds'],
                               message['author']['id'], message['author']['name'], message_type, message['sticker_images'][0]['url'],
                               message['money']['amount'], message['money']['currency']]
                w.writerow(towrite)
            except:
                print(message)
                break
