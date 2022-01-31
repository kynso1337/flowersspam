from telethon import TelegramClient, events
import asyncio
import datetime

api_id = 18285148
api_hash = '2906865d9add7981322d52aa8631fe5b'

mychan = 'me'
channels1 = [1137499852, 1541722817, 1284298470, 1284273044, 1173194065]
channels2 = [1357404865, 1167359821]

client = TelegramClient('myGrab', api_id, api_hash)
print("GRAB - Started")

mytext1 = "Вп на сегодня или на ближайшие числа \n 👁‍🗨На глаза: 1/200 1/300 \n \n 🕐На время: 1/12 1/24 \n \n https://t.me/joinchat/thhjxaeeHm5mYjNi"
mytext2 = "Вп на сегодня или на ближайшие числа \n 👁‍🗨На глаза: 1/200 1/300 \n \n 🕐На время: 1/12 1/24"

@client.on(events.NewMessage(chats=mychan))
async def my_event_handler(event):
        print('bot started')
        await client.send_message('me', "Запустил")
        while True:
                cur = datetime.datetime.now()
                if ((cur.hour==15 or cur.hour==17 or cur.hour==19 or cur.hour==21 or cur.hour==23 or cur.hour==1) and (cur.minute==1 and cur.second==0 and cur.microsecond<50000)):
                        await client.send_message(1137499852, mytext1)
                        await client.send_message(1541722817, mytext1)
                        await client.send_message(1284298470, mytext1)
                        await client.send_message("https://t.me/joinchat/MFdDLxl2zW3yzKmkG_BsyQ", mytext1)
                        await client.send_message("https://t.me/joinchat/Re2FUdAqcidMM3T_", mytext1)
                        await client.send_message("https://t.me/joinchat/-eedVS7E_ukyZWNi", mytext2)
                        await client.send_message('me', "Сообщения по 6 чатам разосланы")
client.start()
client.run_until_disconnected()
