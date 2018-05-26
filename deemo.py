import asyncio
import discord

client = discord.Client()

token = "NDQ5NDI0MzE2NzE5ODI0ODk3.DekfVA.SBdHjXbsSVySV5hzBPwYYfSq9Ak"

@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    print("=======")

    await client.change_presence(game=discord.Game(name="CodeAligo :D",type=1))

@client.event
async def on_message(message):
    if message.authon.bot:
        return None

id = message.author.id
channel = message.channel 

if message.content.startswith('!커맨드'):
    aait clien.send_message(channel, '커맨드')
else:

    await client.send_message(channel, "<@"+id+">님이 \""+message.content+"\"라고 말하였습니다.")

client.run(token)
