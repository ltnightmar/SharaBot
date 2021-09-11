import os
import json
import discord
import random
import asyncio
import datetime
from discord.ext import commands
from webserver import keep_alive


def get_prefix(client=None, message=None):
	with open('./databases/prefixes.json', 'r') as f: 
		prefixes = json.load(f) 
	try: 
		return prefixes[str(message.guild.id)] 
	except AttributeError: 
		return ['#']


intents = discord.Intents.all()
client = commands.Bot(command_prefix=get_prefix, intents=intents)
client.remove_command('help')
client.launch_time = datetime.datetime.utcnow()

@client.event
async def on_guild_join(guild):
    with open ("./databases/prefixes.json", "r") as f:
        prefixes = json.load(f)
        prefixes[str(guild.id)] = "#"
    with open ("./databases/prefixes.json", "w") as f:
        json.dump(prefixes, f, indent=4)

@client.event
async def on_guild_channel_delete(channel):
	with open('./databases/global_chat.json', 'r') as file:
		global_chat_data = json.load(file)
		channel_data = global_chat_data[str(channel.guild.id)]
		for channel_id in list(global_chat_data.values()):
			if channel_data == channel_id:
				global_chat_data.pop(str(channel.guild.id))
				with open('./databases/global_chat.json', 'w') as update_global_chat_file:
					json.dump(global_chat_data, update_global_chat_file, indent=4)
				

@client.event
async def on_guild_remove(guild):
	try: 
		with open('./databases/prefixes.json', 'r') as f: 
			prefixes = json.load(f)
		prefixes.pop(str(guild.id)) 
		with open('./databases/prefixes.json', 'w') as f: 
			json.dump(prefixes, f, indent=4)

		with open('./databases/global_chat.json', 'r') as file:
			global_chat_data = json.load(file)
			channel_data = global_chat_data[str(guild.id)]
			for channel_id in list(global_chat_data.values()):
				if channel_data == channel_id:
					global_chat_data.pop(str(guild.id))
					with open('./databases/global_chat.json', 'w') as update_global_chat_file:
						json.dump(global_chat_data, update_global_chat_file, indent=4)
	except KeyError: 
		return


@client.event
async def on_ready():
	print('Sim, to online de novo')

async def ch_pr():
	await client.wait_until_ready()
	statuses = [
	    f'Online em {len(client.guilds)} servidores',
	    'Minha criadora: Queen of Darkness#1471',
	    'Entre no meu servidor: https://discord.gg/5a87Afucne',
        f'Cuidando de {len(client.users)} membros']

	while not client.is_closed():
		status = random.choice(statuses)
		await client.change_presence(activity=discord.Game(name=status))
		await asyncio.sleep(3)

client.loop.create_task(ch_pr())


for filename in os.listdir('comandos'):
	if filename.endswith('.py'):
		client.load_extension(f'comandos.{filename[:-3]}')


keep_alive()
TOKEN = os.environ['TOKEN']
client.run(TOKEN)