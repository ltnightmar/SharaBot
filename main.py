import discord
import os
import random
import json
import asyncio
from discord.ext import commands
from webserver import keep_alive
from utils.save import vodka

intents = discord.Intents.all()
client = commands.Bot(intents=intents)

@client.event
async def on_guild_channel_delete(channel):
	with open('./databases/global_chat.json', 'r') as file:
		global_chat_data = json.load(file)
		for channel_id in list(global_chat_data.values()):
			if channel.guild.id == channel_id:
				global_chat_data.pop(str(channel.guild.id))
				with open('./databases/global_chat.json', 'w') as update_global_chat_file:
					json.dump(global_chat_data, update_global_chat_file, indent=4)
				
@client.event
async def on_guild_remove(guild):
	with open('./databases/global_chat.json', 'r') as file:
		global_chat_data = json.load(file)
		for guild_id in list(global_chat_data.values()):
			if guild.id == guild_id:
				global_chat_data.pop(str(guild.id))
				with open('./databases/global_chat.json', 'w') as update_global_chat_file:
					json.dump(global_chat_data, update_global_chat_file, indent=4)

@client.event
async def on_ready():
	print(f'{client.user} online!')
async def ch_pr():
	await client.wait_until_ready()
	statuses = [
     'Minha criadora é a Queen of Darkness#1471', 
     f'Estou online em {len(client.guilds)} servidores com {len(client.users)} membros',
     'Meu prefixo é /', 'Ative o chat global no seu servidor!']
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
 
