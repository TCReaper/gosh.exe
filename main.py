
# gosh bot

import os
import sys
import time
import asyncio
import discord

from keep_alive import keep_alive

creatorID = os.environ.get("CREATOR_ID")
token = os.environ.get("DISCORD_BOT_SECRET")


# CREATES INSTANCE OF CLIENT VARIABLE
client = discord.Client()
                
@client.event
async def on_message(message):
    if 'gosh' in message.content:
        msg = ('gosh.').format(message)
        await client.send_message(message.channel, msg)
        return
    return

    
async def my_background_task():
    await client.wait_until_ready()
    message = 'gosh'
    text_channel_list = []
    for server in Client.servers:
        for channel in server.channels:
            if channel.type == 'Text':
                text_channel_list.append(channel)
    while not client.is_closed:
        for i in text_channel_list:
            await client.send_message(i, gosh)
        await asyncio.sleep(60)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(discord.Game(name="with your goshes"))

keep_alive()
#client.loop.create_task(my_background_task())
client.run(token)
