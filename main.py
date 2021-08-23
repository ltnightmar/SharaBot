import os
import json
import discord
import random
import asyncio
import datetime
from discord.ext import commands
from webserver import keep_alive


def get_prefix(client, message):
	if not message.guild:
		return commands.when_mentioned_or('#')(client, message)
	with open('./databases/prefixes.json', 'r') as f:
		prefixes = json.load(f)
	if str(message.guild.id) not in prefixes:
		return commands.when_mentioned_or('#')(client, message)

	prefix = prefixes[str(message.guild.id)]
	return commands.when_mentioned_or(prefix)(client, message)


intents = discord.Intents.all()
client = commands.Bot(command_prefix=get_prefix, intents=intents)
client.remove_command('help')
client.launch_time = datetime.datetime.utcnow()


@client.event
async def on_ready():

	print('Sim, to online de novo')

async def ch_pr():

	await client.wait_until_ready()

	statuses = [
	    f'Online em {len(client.guilds)} servidores | #help',
	    'Minha criadora: Lilithⁿᵗᵐ#0666 | #help',
	    'Entre no meu servidor: https://discord.gg/nnightmare | #help',
        f'Cuidando de {len(client.users)} membros']

	while not client.is_closed():

		status = random.choice(statuses)

		await client.change_presence(activity=discord.Game(name=status))

		await asyncio.sleep(3)


client.loop.create_task(ch_pr())

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return await ctx.send(f'<:nao:850020125927276641> {ctx.author.mention}| Comando inexistente! Use o comando help para saber meus comandos!')

for filename in os.listdir('comandos'):
	if filename.endswith('.py'):
		client.load_extension(f'comandos.{filename[:-3]}')

keep_alive()
TOKEN = os.environ['TOKEN']
client.run(TOKEN)
