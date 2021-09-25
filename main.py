import discord
import os
import random
import asyncio
from discord.ext import commands
from webserver import keep_alive
from utils.save import vodka

intents = discord.Intents.all()
client = commands.Bot(intents=intents)

@client.event
async def on_ready():
	print(f'{client.user} online!')
async def ch_pr():
	await client.wait_until_ready()
	statuses = [
	    f'Online em {len(client.guilds)} servidores',
	    'Minha criadora: Queen of Darkness#1471',
        f'Cuidando de {len(client.users)} membros']
	while not client.is_closed():
		status = random.choice(statuses)
		await client.change_presence(activity=discord.Game(name=status))
		await asyncio.sleep(3)
client.loop.create_task(ch_pr())

@client.event
async def on_message(message):
    if not message.author.bot:
        msg = message.content.lower()
        if 'vodka' in msg:
            await message.reply(f'Pegue essa {vodka} vodka para você!')
        elif 'bolo' in msg:
            await message.reply(f'Pegue esse :cake: bolo para você!')
        else:
            pass
    else:
        pass
    
for filename in os.listdir('comandos'):
	if filename.endswith('.py'):
		client.load_extension(f'comandos.{filename[:-3]}')

keep_alive()
TOKEN = os.environ['TOKEN']
client.run(TOKEN)
 
