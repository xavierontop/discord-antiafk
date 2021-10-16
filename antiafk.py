import os, discord
from discord.ext import commands
 
input("press enter to continue")
os.system('cls')
token = input("enter token: ")
client = commands.Bot(command_prefix=commands.when_mentioned_or("$"))
os.system('cls')
os.system(f'title [pressure bot by xavier]')
os.system(f'mode 60,20')
 


 
@client.event
async def on_ready():
  print(f""" \u001b[31m
                   _  __ _         _   
 __ ____ ___ ___| |/ _| |__  ___| |_ 
 \ \ / _(_-</ -_) |  _| '_ \/ _ \  _|
 /_\_\__/__/\___|_|_| |_.__/\___/\__|
------------------------------
bot by xavier
type "OK" to pressure
type "@opp afk check" to afk check
!to stop any of those loops close this window!
------------------------------
""")
 
@client.event
async def on_message(message):
    channel = message.channel
    if message.content.endswith('OK'):

        await message.channel.send ('NIGGA')
        await message.channel.send ('YOU')
        await message.channel.send ('SUCK')
        await message.channel.send ('U')
        await message.channel.send ('CANT')
        await message.channel.send ('PACK')
        await message.channel.send ('DUMBASS')
        await message.channel.send ('BITCH')
        await message.channel.send ('TWINK LOOKIN ASS NIGGA')
        await message.channel.send ('U CANT PRESSURE ME')
        await message.channel.send ('SLOW')
        await message.channel.send ('ASS')
        await message.channel.send ('NIGGA')
        await message.channel.send ('LO')
        await message.channel.send ('L')
        await message.channel.send ('LOOLLOL')
        await message.channel.send ('LOLL')
        await message.channel.send ('TYPE')
        await message.channel.send ('FASTER')
        await message.channel.send ('RETARDED')
        await message.channel.send ('ASS')
        await message.channel.send ('BITCH')
        await message.channel.send ('LOO')
        await message.channel.send ('LLOL')
        await message.channel.send ('LO')
        await message.channel.send ('COME')
        await message.channel.send ('LETS')
        await message.channel.send ('PACK')
        await message.channel.send ('RETARD')
        await message.channel.send ('U WONT')
        await message.channel.send ('BITCH ASS')
        await message.channel.send ('TYPE')
        await message.channel.send ('FASTER')
        await message.channel.send ('DUMB')
        await message.channel.send ('ASS')
        await message.channel.send ('BITCH')
        await message.channel.send ('LOLO')
        await message.channel.send ('LOOL')
        await message.channel.send ('OLOL')
        await message.channel.send ('LOLO')
        await message.channel.send ('DONT STOP')
        await message.channel.send ('SPAMMING')
        await message.channel.send ('WEAK ASS BITCH')
        await message.channel.send ('LO')
        await message.channel.send ('LOOL')
        await message.channel.send ('LOLO')
        await message.channel.send ('LO')
        await message.channel.send ('LO')
        await message.channel.send ('OK')
        await message.channel.send ('XAVIER LOL WAS HERE SON')
        channel = message.channel
    if message.content.endswith('check'):
      for i in range(1, 10001):
        await message.channel.send(i)




 
client.run(token, bot=False)