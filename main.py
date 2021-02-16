import discord
import random
import os

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

client = commands.Bot(command_prefix='!')

def choose_quote(file_name):
    with open(file_name, encoding="utf8") as file:
        lines = file.readlines()
        random_line = random.choice(lines)
    return random_line

@client.command(name = 'motivation', help = 'Provide a motivational message from her')
async def motivation(ctx):
    response = choose_quote('motivation.txt')
    await ctx.send(response)

@client.command(name = 'drunk', help = 'Some messages to wake you up')
async def drunk(ctx):
    response = choose_quote('drunk.txt')
    await ctx.send(response)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    yes_no = [
        '😊',
        '*seen*',
    ]
    if 'em có nên nhắn cho cô không?' in message.content.lower():
        response = random.choice(yes_no)
        await message.channel.send(response)
    if 'có phải do mày mà cô không thèm rep tao hong' in message.content.lower():
        response = random.choice(yes_no)
        await message.channel.send(response)
    await client.process_commands(message)
client.run(TOKEN)