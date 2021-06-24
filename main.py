import os
import asyncio
import random
import discord
import datetime
from discord.ext import commands
from webserver import keep_alive

intents = discord.Intents(messages=True, guilds=True)
intents.members = True
intents.change_presence = True
client = discord.Client(command_prefix='>', intents=intents)
client.remove_command('help')
client.launch_time = datetime.datetime.utcnow()

@client.event
async def on_ready():

    await client.change_presence(activity=discord.Game(name=f"Online em {len(client.guilds)} servidores"))
    await client.change_presence(activity=discord.Game(name=f"Escreva #help para mais comandos"))
    await client.change_presence(activity=discord.Game(name=f"Entre no meu servidor: https://discord.gg/ntm"))
    await client.change_presence(activity=discord.Game(name=f"Minha criadora: Lilithⁿᵗᵐ#0666"))

    print('A mãe tá on')


async def change_presence():
    await client.wait_until_ready()

    statuses = [f"Cuidando de {len(client.guilds)} servidores", f"Escreva #help para mais comandos",
                f"Entre no meu servidor: https://discord.gg/ntm", "Minha criadora: Lilithⁿᵗᵐ#0666"]

    while not client.is_closed():

        status = random.choice(statuses)

        await client.change_presence(activity=discord.Game(name=status))

        await asyncio.sleep(2)

    client.loop.create_task(change_presence())


for filename in os.listdir('comandos'):
    if filename.endswith('.py'):
        client.load_extension(f'comandos.{filename[:-3]}')

keep_alive()
TOKEN = os.environ['TOKEN']
client.run(TOKEN)
