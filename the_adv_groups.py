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
print("""
sdSS_SSSSSSbs    sSSSSs   .S_SSSs     .S       S.   sdSS_SSSSSSbs    sSSs_sSSs      sSSs    sSSs   .S_sSSs     .S_sSSs    
YSSS~S%SSSSSP   d%%%%SP  .SS~SSSSS   .SS       SS.  YSSS~S%SSSSSP   d%%SP~YS%%b    d%%SP   d%%SP  .SS~YS%%b   .SS~YS%%b   
     S%S       d%S'      S%S   SSSS  S%S       S%S       S%S       d%S'     `S%b  d%S'    d%S'    S%S   `S%b  S%S   `S%b  
     S%S       S%S       S%S    S%S  S%S       S%S       S%S       S%S       S%S  S%|     S%S     S%S    S%S  S%S    S%S  
     S&S       S&S       S%S SSSS%S  S&S       S&S       S&S       S&S       S&S  S&S     S&S     S%S    S&S  S%S    S&S  
     S&S       S&S       S&S  SSS%S  S&S       S&S       S&S       S&S       S&S  Y&Ss    S&S_Ss  S&S    S&S  S&S    S&S  
     S&S       S&S       S&S    S&S  S&S       S&S       S&S       S&S       S&S  `S&&S   S&S~SP  S&S    S&S  S&S    S&S  
     S&S       S&S sSSs  S&S    S&S  S&S       S&S       S&S       S&S       S&S    `S*S  S&S     S&S    S&S  S&S    S&S  
     S*S       S*b `S%%  S*S    S&S  S*b       d*S       S*S       S*b       d*S     l*S  S*b     S*S    S*S  S*S    d*S  
     S*S       S*S   S%  S*S    S*S  S*S.     .S*S       S*S       S*S.     .S*S    .S*P  S*S.    S*S    S*S  S*S   .S*S  
     S*S        SS_sSSS  S*S    S*S   SSSbs_sdSSS        S*S        SSSbs_sdSSS   sSS*S    SSSbs  S*S    S*S  S*S_sdSSS   
     S*S         Y~YSSY  SSS    S*S    YSSP~YSSY         S*S         YSSP~YSSY    YSS'      YSSP  S*S    SSS  SSS~YSSY    
     SP                         SP                       SP                                       SP                      
     Y                          Y                        Y                                        Y                       
                                                                                                                          
created by : bijita syanz
      telegram : @soufianshope
      github   : @bijita-syanz
""")

while True:
   loop = asyncio.get_event_loop()
   loop.run_until_complete(send_message())
   time.sleep(300)

