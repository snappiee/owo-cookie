#made by snappiee; discord: gh0x
#importing: 
import keep_alive
import string
from colorama import init
import os
init()
from sys import *
import time
import requests
import atexit
from multiprocessing import Process, Pool
import random
import re
try:
 from inputimeout import inputimeout,TimeoutOccurred
except:
 from setup import install
 install()
finally:
 from inputimeout import inputimeout,TimeoutOccurred
if os.name == 'nt':
  import json
else:
  import simplejson as json
try:
  from discum import *
except:
  from setup import install
  install()
finally:
  from discum import *
try:
 from discord_webhook import DiscordWebhook
except:
 from setup import install
 install()
finally:
 from discord_webhook import DiscordWebhook
#starting bot:
print("""\
owo self bot.
Remade version - no updates supported.
- Edit your options in the settings.json file.
- This is for Replit hosting, make 2 secrets: 'TOKEN', 'USERID' for the main selfbot
""")
wbm=[16,18]
class client:
  token = os.getenv("TOKEN")
  webhookping = os.getenv("USERID")
  totalcmd = 0
  totaltext = 0
  stopped = False
  recentversion = "6.9.6"
  wait_time_daily = 60
  channel2 = []
  class color:
    purple = '\033[95m'
    okblue = '\033[94m'
    okcyan = '\033[96m'
    okgreen = '\033[92m'
    warning = '\033[93m'
    fail = '\033[91m'
    reset = '\033[0m'
    bold = '\033[1m'
    underline = '\033[4m'
  with open('settings.json', "r") as file:
        data = json.load(file)
        channel = data["channel"]
        gm = data["gm"]
        sm = data["sm"]
        pm = data["pm"]
        em = data["em"]
        bm = data["bm"]
        prefix = data["prefix"]
        allowedid = data["allowedid"]
        webhook = data["webhook"]
        daily = data["daily"]
        stop = data["stop"]
        change = data["change"]
        text = data["text"]
        farm = data["farm"]
  f = open('stopped.txt', 'r')
  content = f.read()
  if "True" in content:
   try:
    choice = inputimeout("Did You Solve The Captcha (y/n)?: ",timeout=10)
   except:
    raise Exception("Please Solve The Captcha")
   if choice.lower() == "y":
     f = open('stopped.txt', 'w')
     f.close()
   else:
     raise Exception("Please Solve The Captcha")
  else:
   pass
  if data["channel"] == 'nothing':
   print(f"{color.fail} !!! [ERROR] !!! {color.reset} Please enter Channel to continue")
   time.sleep(2)
   os.execl(executable, executable, *argv)
  head = {'Authorization': str(token)}
  response = requests.get('https://discordapp.com/api/v6/users/@me', headers=head)
  if response.status_code == 200:
    pass
  elif response.status_code == 429:
    print(f"{color.fail}[ERROR]{color.reset} Too Many Requests! Try Again Later.")
    time.sleep(300)
    raise SystemExit
  elif response.status_code == 404:
    print(f"{color.fail}[ERROR]{color.reset} Invalid Token")
    time.sleep(2)
    raise SystemExit
  print('=========================')
  print(f'| [1] {color.warning}Load data         {color.reset}|')
  print(f'| [2] {color.warning}Info with Help    {color.reset}|')
  print('=========================')
try:
 print("Automatically Pick Option [1] In 3 Seconds. ")
 choice = inputimeout(prompt='Enter Your Choice: ', timeout=3)
except TimeoutOccurred:
 choice = "1"
if choice == "1":
 pass
elif choice == "2":
      print(f'{client.color.purple} =========Selfbot Commands=========={client.color.reset}')
      print("{Prefix}send {Message} [Send Your Provided Message}")
      print("{Prefix}restart [Restart]")
      print("{Prefix}exit [Stop]")
      print("{Prefix}sm {on/off} [Turn On/Off Sleep mode]")
      print("{Prefix}em {on/off} [Turn On/Off Exp mode]")
      print("{Prefix}pm {on/off} [Turn On/Off Pray mode]")
      print("{Prefix}gm {on/off} [Turn On/Off Gems mode]")
      print("{Prefix}change {on/off} [Turn On/Off Change Channel mode]")
      print("{Prefix}bm {on/off} [Turn On/Off Break mode]")
      print("{Prefix}farm {on/off} [Turn On/Off Farm mode]")
      print(" ")
      print("{Prefix} == Your Prefix")
      time.sleep(15)
      raise SystemExit
else:
 print(f'{client.color.fail} !! [ERROR] !! {client.color.reset} Wrong input!')
 time.sleep(1)
 os.execl(executable, executable, *argv)
def at():
  return f'\033[0;93m{time.strftime("%d/%m/%Y | %H+7:%M:%S", time.localtime())}\033[0;21m'
bot = discum.Client(token = client.token, log = False)
@bot.gateway.command
def on_ready(resp):
    if resp.event.ready_supplemental: #ready_supplemental is sent after ready
        user = bot.gateway.session.user
        print("Logged in as {}#{}".format(user['username'], user['discriminator']))
@bot.gateway.command
def security(resp): #webhook for captcha mode
 if client.webhook != 'None':
  if issuechecker(resp) == "captcha":
    client.stopped = True
    user = bot.gateway.session.user
    if client.webhookping != 'None':
     sentwebhook = DiscordWebhook(url=client.webhook, content='<@{}> Captcha in: <#{}>'.format(client.webhookping,client.channel))
     response = sentwebhook.execute()
     bot.gateway.close()
     atexit()
    else:
     sentwebhook = DiscordWebhook(url=client.webhook, content='<@{}> <@{}> Captcha in: <#{}>'.format(user['id'],client.allowedid,client.channel))
     response = sentwebhook.execute()
     bot.gateway.close()
     atexit()
 if client.webhook == 'None':
  if issuechecker(resp) == "captcha":
   client.stopped = True
   bot.gateway.close()
   atexit()
@bot.gateway.command
def issuechecker(resp):
 if resp.event.message:
   m = resp.parsed.auto()
   if m['channel_id'] == client.channel and client.stopped != True:
    if m['author']['id'] == '408785106942164992' or m['author']['username'] == 'gh0x' or m['author']['discriminator'] == '8456' or m['author']['public_flags'] == '65536':
     if 'captcha' in m['content'].lower():
       print(f'{at()}{client.color.warning} !! [CAPTCHA] !! {client.color.reset} CAPTCHA . ACTION REQU??RED')
       f = open("stopped.txt","w")
       f.write('True')
       return "captcha"
     if 'you are human!'  in m['content']:
       print(f'{at()}{client.color.warning} !! [CAPTCHA] !! {client.color.reset} CAPTCHA . ACTION REQU??RED')
       return "captcha"
     if '/5)' in m['content'].lower():
       print(f'{at()}{client.color.warning} !! [CAPTCHA] !! {client.color.reset} CAPTCHA . ACTION REQU??RED')
       return "captcha" #captcha detection
     
     def change_channel(): #change channel module
       if client.change.lower() == "yes":
         client.channel2 = []
         guild = bot.gateway.session.guild(m['guild_id']).channels
         channel = guild.keys()
         channel2 = random.choice(list(channel))
         try:
          if guild[channel2]['type'] == "guild_text":
            client.channel2.append(channel2)
            client.channel2.append(guild[channel2]['name'])
          else:
            change_channel()
         except RecursionError:
            client.channel2.append(channel2)
            client.channel2.append(guild[channel2]['name'])
     change_channel()
    
def levelling(resp):
    if resp.event.message:
     m = resp.parsed.auto()
     if m['channel_id'] == client.channel and client.stopped != True:
         if m['author']['id'] == '408785106942164992' or m['author']['username'] == 'OwO' or m['author']['discriminator'] == '8456' or m['author']['public_flags'] == '65536':
           if 'level' in m['content'].lower():
            print(f'{at()}{client.color.warning} Level up! {client.color.reset}')
            sentwebhook = DiscordWebhook(url=client.webhook, content='<@{}> Level up!'.format(client.webhookping))
            response = sentwebhook.execute()
def runner(): #auto-farm module
        global wbm
        time.sleep(2)
        bot.sendMessage(str(client.channel), 'owoh')
        print(f"{at()} {client.color.okgreen}[SENT]{client.color.reset} Hunt")
        time.sleep(5)
        bot.sendMessage(str(client.channel), 'owob')
        print(f"{at()} {client.color.okgreen}[SENT]{client.color.reset} Battle")
        client.totalcmd += 2
        time.sleep(random.randint(wbm[0],wbm[1]))
def owoexp(): #auto exp module
  if client.em.lower() == "yes":
    time.sleep(3)
    bot.sendMessage(str(client.channel), "owo")
    print(f"{at()} {client.color.okgreen}[SENT]{client.color.reset} owo")
    time.sleep(2)
def autoexp():
  if client.text.lower() == "yes":
   ran = ''.join(random.choices(string.ascii_letters + string.digits, k = 100))    
   time.sleep(2)
   bot.sendMessage(str(client.channel), ran)
   print(f"{at()} {client.color.okgreen}[SENT]{client.color.reset} Random string")
   time.sleep(2)
def owopray(): #pray module
  if client.pm.lower() == "yes":
   if client.stopped != True:
    bot.sendMessage(str(client.channel), "owopray")
    print(f"{at()} {client.color.okgreen}[SENT]{client.color.reset} Pray")
    client.totalcmd += 1
    time.sleep(random.randint(13,18))
@bot.gateway.command
def gems2(resp): #gem using status
   if client.gm.lower() == "yes":
    if resp.event.message:
      m = resp.parsed.auto()
      if m['channel_id'] == client.channel and client.stopped != True:
       if m['author']['id'] == '408785106942164992' or m['author']['username'] == 'OwO' or m['author']['discriminator'] == '8456' or m['author']['public_flags'] == '65536':
        if m['content'] != "" and m['embeds'] == [] and "hunt" in m['content']:
         if not "empowered" in m['content']:
           gems1()
         else:
            if '[0/' in m['content']:
             time.sleep(13)
             bot.sendMessage(str(client.channel), "owoh")
             gems1()
            elif not "gem1" in m['content'] or not "gem4" in m['content'] or not "gem3" in m['content']:
             gems1()
def gems1(): #gem using
    time.sleep(3)
    bot.sendMessage(str(client.channel), "owoinv")
    print(f"{at()} {client.color.okgreen}[SENT]{client.color.reset} Check inventory")
    client.totalcmd += 1
    time.sleep(4)
    msgs=bot.getMessages(str(client.channel), num=5)
    msgs=json.loads(msgs.text)
    inv = 0
    length = len(msgs)
    i = 0
    while i < length:
     if msgs[i]['author']['id']=='408785106942164992' and 'Inventory' in msgs[i]['content']:
        inv=re.findall(r'`(.*?)`', msgs[i]['content'])
        i = length
     else:
        i += 1
    if not inv:
       time.sleep(5)
       client.totalcmd -= 1
       gems1()
    else:
      if '050' in inv:
        bot.sendMessage(str(client.channel), "owolb all")
        print(f"{at()} {client.color.okgreen}[SENT]{client.color.reset} owolb all")
        time.sleep(13)
        gems1()
      if '100' in inv:
        bot.sendMessage(str(client.channel), "owowc all")
        print(f"{at()} {client.color.okgreen}[SENT]{client.color.reset} owowc all")
        time.sleep(2)
      for item in inv:
        try:
          if int(item) > 100:
            inv.pop(inv.index(item)) #weapons
        except: #backgrounds etc
          inv.pop(inv.index(item))
      tier = [[],[],[]]
      print(f"{at()} {client.color.okblue}[INFO]{client.color.reset} Found {len(inv)} gems in the inventory")
      for gem in inv:
        gem = re.sub(r"[^a-zA-Z0-9]", "", gem)
        gem = int(float(gem))
        if 50 < gem < 58:
          tier[0].append(gem)
        elif 64 < gem < 72:
          tier[1].append(gem)
        elif 71 < gem <  79:
          tier[2].append(gem)
      for level in range(0,3):
        if not len(tier[level]) == 0:
          time.sleep(5)
          bot.sendMessage(str(client.channel), "owouse "+str(max(tier[level])))
          print(f"{at()} {client.color.okgreen}[SENT]{client.color.reset} owouse {str(max(tier[level]))}")
def daily(): #claim daily mode
 if client.daily.lower() == "yes" and client.stopped != True:
    time.sleep(1)
    bot.sendMessage(str(client.channel), "owodaily")
    print(f"{at()} {client.color.okgreen}[SENT]{client.color.reset} Claiming daily")
    client.totalcmd += 1
    time.sleep(3)
    print(f"{at()} {client.color.okblue}[INFO]{client.color.reset} Claimed Daily Rewards")
    bot.sendMessage(str(client.channel), "owoclaim")
    time.sleep(5)
    bot.sendMessage(str(client.channel), "owoq")
    client.daily = "no"
@bot.gateway.command
def othercommands(resp):
 prefix = client.prefix
 if resp.event.message:
   m = resp.parsed.auto()
   if m['author']['id'] == bot.gateway.session.user['id'] or m['channel_id'] == client.channel and m['author']['id'] == client.allowedid:
    if prefix == "None":
     bot.gateway.removeCommand(othercommands)
     return
    if "{}send".format(prefix) in m['content'].lower():
     message = m['content'][6::]
     bot.sendMessage(str(m['channel_id']), message)
     print(f"{at()}{client.color.okgreen} [SENT] {client.color.reset} {message}")
    if "{}restart".format(prefix) in m['content'].lower(): #restarting
     bot.sendMessage(str(m['channel_id']), "Restarting...")
     print(f"{at()}{client.color.okcyan}[INFO] Restarting...  {client.color.reset}")
     time.sleep(1)
     os.execl(executable, executable, *argv)
    if "{}exit".format(prefix) in m['content'].lower(): #exit
     bot.sendMessage(str(m['channel_id']), "Exiting...")
     print(f"{at()}{client.color.okcyan}[INFO] Exiting...  {client.color.reset}")
     bot.gateway.close()
    if "{}gm".format(prefix) in m['content'].lower(): #gems mode
     if "on" in m['content'].lower():
      client.gm = "YES"
      bot.sendMessage(str(m['channel_id']), "Turn on Gems mode")
      print(f"{at()}{client.color.okcyan}[INFO] Turn on Gems mode{client.color.okcyan}")
     if "off" in m['content'].lower():
      client.gm = "NO"
      bot.sendMessage(str(m['channel_id']), "Turn off Gems mode")
      print(f"{at()}{client.color.okcyan}[INFO] Turn off Gems mode{client.color.okcyan}")
    if "{}pm".format(prefix) in m['content'].lower(): #pray mode
      if "on" in m['content'].lower():
       client.pm = "YES"
       bot.sendMessage(str(m['channel_id']), "Turn on Pray mode")
       print(f"{at()}{client.color.okcyan}[INFO] Turn on Pray mode{client.color.reset}")
      if "off" in m['content'].lower():
       client.pm = "NO"
       bot.sendMessage(str(m['channel_id']), "Turn off Pray mode")
       print(f"{at()}{client.color.okcyan}[INFO] Turn off Pray mode{client.color.reset}")
    if "{}sm".format(prefix) in m['content'].lower(): #sleep mode
      if "on" in m['content'].lower():
       client.sm = "yes"
       bot.sendMessage(str(m['channel_id']), "Turn on Sleep mode")
       print(f"{at()}{client.color.okcyan}[INFO] Turn on Sleep mode{client.color.reset}")
      if "off" in m['content'].lower():
       client.sm = "NO"
       bot.sendMessage(str(m['channel_id']), "Turn off Sleep mode")
       print(f"{at()}{client.color.okcyan}[INFO] Turn off Sleep mode{client.color.reset}")
    if "{}bm".format(prefix) in m['content'].lower(): #break mode
      if "on" in m['content'].lower():
       client.bm = "yes"
       bot.sendMessage(str(m['channel_id']), "Turn on Break mode")
       print(f"{at()}{client.color.okcyan}[INFO] Turn on Break mode{client.color.reset}")
      if "off" in m['content'].lower():
       client.bm = "NO"
       bot.sendMessage(str(m['channel_id']), "Turn off Break mode")
       print(f"{at()}{client.color.okcyan}[INFO] Turn off Break mode{client.color.reset}")
    if "{}farm".format(prefix) in m['content'].lower(): #farming mode
      if "on" in m['content'].lower():
       client.farm = "yes"
       bot.sendMessage(str(m['channel_id']), "Turn on Farm mode")
       print(f"{at()}{client.color.okcyan}[INFO] Turn on Farm mode{client.color.reset}")
      if "off" in m['content'].lower():
       client.farm = "NO"
       bot.sendMessage(str(m['channel_id']), "Turn off Farm mode")
       print(f"{at()}{client.color.okcyan}[INFO] Turn off Farm mode{client.color.reset}")
    if "{}em".format(prefix) in m['content'].lower(): #exp mode
      if "on" in m['content'].lower():
       client.em = "YES"
       bot.sendMessage(str(m['channel_id']), "Turn on Exp mode")
       print(f"{at()}{client.color.okcyan}[INFO] Turn on Exp mode{client.color.reset}")
      if "off" in m['content'].lower():
       client.em = "NO"
       bot.sendMessage(str(m['channel_id']), "Turn off Exp mode")
       print(f"{at()}{client.color.okcyan}[INFO] Turn off Exp mode{client.color.reset}")
    if "{}gems".format(prefix) in m['content'].lower():
       gems1()
    if "{}change".format(prefix) in m['content'].lower(): #change
      if "on" in m['content'].lower():
       client.change = "yes"
       bot.sendMessage(str(m['channel_id']), "Turn on Change Channel mode")
       print(f"{at()}{client.color.okcyan}[INFO] Turn on Change Channel mode{client.color.reset}")
      if "off" in m['content'].lower():
       client.change = "no"
       bot.sendMessage(str(m['channel_id']), "Turn off Change Channel mode")
       print(f"{at()}{client.color.okcyan}[INFO] Turn off Change Channel mode{client.color.reset}")
@bot.gateway.command
def loopie(resp): #timer module
 if resp.event.ready:
  pray = 0
  owo = pray
  daily_time = pray
  main = time.time()
  stop = main
  change = main
  while True:
    if client.stopped == True:
       break
    if client.stopped != True:
      if client.farm.lower() == "yes":
        runner()
      if time.time() - pray > random.randint(300, 600) and client.stopped != True:
        owopray()
        pray=time.time()
      if time.time() - owo > random.randint(20, 30) and client.stopped != True:
        owoexp()
        time.sleep(5)
        autoexp()
        owo=time.time()
      if client.sm.lower() == "yes":
       if time.time() - main > random.randint(4000, 4500) and client.stopped != True:
        main=time.time()
        print(f"{at()} {client.color.okblue}[INFO]{client.color.reset} Sleeping")
        time.sleep(random.randint(1600, 1900))
      if client.bm.lower() == "yes":
       if time.time() - main > random.randint(300, 400) and client.stopped != True:
        main=time.time()
        print(f"{at()} {client.color.okblue}[INFO]{client.color.reset} Taking a break")
        time.sleep(random.randint(80, 150))
      if time.time() - daily_time > int(client.wait_time_daily) and client.stopped != True:
        daily()
        daily_time = time.time()
      if client.stop.lower() == "yes" and client.stopped != True:
       if time.time() - stop > int(client.stop):
         bot.gateway.close()
      if client.change.lower() == "yes" and client.stopped != True:
        if time.time() - change > random.randint(3600, 4000):
         print(f"{at()}{client.color.okcyan}[INFO] Restarting...  {client.color.reset}")
         time.sleep(1)
         os.execl(executable, executable, *argv)
        if time.time() - change > random.randint(600, 900):
         change=time.time()
         print(f"{at()} {client.color.okblue}[INFO]{client.color.reset} Changed Channel To: {client.channel2[1]}")
         client.channel = client.channel2[0]
         sentwebhook = DiscordWebhook(url=client.webhook, content='<@{}> Changed channel: <#{}>'.format(client.webhookping,client.channel))
         response = sentwebhook.execute()
      
def defination1(): #cpu calculation with bot
  global once
  if not once:
    once=True
    if __name__ == '__main__':
      lol2 = Pool(os.cpu_count() - 1)
      lol2.map(loopie)
      lol = Process(target=loopie)
      lol.run()
keep_alive.keep_alive()
bot.gateway.run(auto_reconnect=True)
@atexit.register
def atexit():
 print(f"{client.color.okgreen}Total Commands: {client.totalcmd}{client.color.reset}")
 print(f"{client.color.okgreen}Total Random Text Sent: {client.totaltext}{client.color.reset}")
 print("Answer Your Captcha First Before Restarting!")
 time.sleep(9999999)
 
