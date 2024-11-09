from telethon import TelegramClient
import asyncio
import arrays
import random , time

api_id = ''
api_hash = ''
phone_number = ''
groups = arrays.adv_groups

def print_colored(text, color):
    colors = {
        'red': '\033[31m',
        'green': '\033[32m',
        'reset': '\033[0m'
    }
    color_code = colors.get(color, colors['reset'])
    print(f"{color_code}{text}{colors['reset']}")

def generate_messag():
    reflink = "https://t.me/GmailFarmerBot?start=1299531144"
    ranint = random.randint(0,len(arrays.adsgmail)-1)
    message_content = arrays.adsgmail[ranint]
    message = f"{message_content} link : {reflink} "
    return message
client = TelegramClient('anon', api_id, api_hash)

async def send_message():
    await client.start(phone_number)
    count = 0
    msesages_num = 1
    for group in groups:
        
        try:
            time.sleep(1+random.randint(0,2))
            entity = await client.get_entity(group)
            await client.send_message(entity, generate_messag())
            print_colored(f"Message n:[{str(msesages_num)}] sent to {group}" , "green")
            msesages_num += 1
        except Exception as e:
            print_colored(f"Failed to send message to {group}: {e}" , "red")
            count += 1
    if count == 0 :
        print_colored("All messages sent!", "green")
    else :
        pass


while True:
   loop = asyncio.get_event_loop()
   loop.run_until_complete(send_message())
   time.sleep(300)

