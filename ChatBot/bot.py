import os
from dotenv import load_dotenv
import discord
import sys

# Other Files
sys.path.insert(0, "AI Logic\\")
import main



load_dotenv('ChatBot\.env')

BOT_TOKEN = os.environ['TOKEN']

client = discord.Client()


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content
    # msgs = str(msg.lower()).split("$trixy")[1]
    y = main.chat("".join(msg))
    print(y)
    await message.channel.send(y)

client.run(BOT_TOKEN)     
