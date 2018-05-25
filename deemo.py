import asyncio
import discord

client = discord.Client()

token = "NDQ5NDI0MzE2NzE5ODI0ODk3.DekfVA.SBdHjXbsSVySV5hzBPwYYfSq9Ak"

@client.event
async def on_ready():
    print("디스코드 로그인 완료!")
    print(client.user.name)
    print(client.user.id)
    print("=======")

    await client.change_presence(game=discord.Game(name="CodeAligo :d",type=1))

client.run(token)
