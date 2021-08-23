import discord
import asyncio
import datetime
import json
from discord.ext import commands

class Help(commands.Cog):

    def __init__(self, client):
        self.author = None
        self.client = client

    @commands.command(aliases=['ajuda'])
    async def help(self, ctx):
        with open('./databases/prefixes.json', 'r') as f:
            prefixes = json.load(f)
        pre = prefixes[str(ctx.guild.id)]
        embed = discord.Embed(title='✉️ Menu de Ajuda', description=f'✨ Olá **{ctx.author.name}**, meu nome é Shara. Prazer em conhecer! O meu prefixo nesse servidor é: {pre}', colour=0x030058, timestamp=ctx.message.created_at)
        embed.add_field(name='📚 Comandos', value=f'`{pre}comandos` : Acesse uma lista organizada com todos os meus comandos.', inline=False)
        embed.add_field(name='💎 Servidor', value='https://discord.gg/9XYGv8sG7F', inline=False)
        embed.add_field(name='🛠️ Criadora', value='**Fui criada pela:** Lilithⁿᵗᵐ#0666', inline=False)
        embed.set_thumbnail(url=self.client.user.avatar_url)
        embed.set_footer(icon_url=ctx.author.avatar_url, text=f'{ctx.author}')
        await ctx.send(embed=embed)

    @commands.group(invoke_without_command=True, aliases=['commands'])
    async def comandos(self, ctx):
        embed = discord.Embed(title='Comandos', description='Bot em desenvolvimento', colour=0x030058, timestamp=ctx.message.created_at)
        embed.add_field(name='🔨**| Moderação (6)**', value='`kick`, `ban`, `adicionarcargo`, `removercargo`, `dm`, `apagar`', inline=False)
        embed.add_field(name='⚙️**| Gerenciamento (8)**', value='`lock`, `unlock`, `criar`, `criar cargo`, `criar chat`, `criar call`, `criar categoria`, `prefixo`', inline=False)
        embed.add_field(name='📋**| Informações (9)**', value='`uptime`, `serverinfo`, `userinfo`, `servericon`, `avatar`, `creditos`, `ping`, `servidor`, `comandos`', inline=False)
        embed.add_field(name='👤**| Diversão (9)**', value='`beijar`, `abraçar`, `tapa`, `socar`, `matar`, `coinflip`, `rip1`, `rip2`, `wanted`', inline=False)
        embed.add_field(name='🌎**| Chat Global (3)**', value='`chatglobal`, `chatglobal start`, `chatglobal stop`', inline=False)
        embed.add_field(name='🔖**| Utilidades (5)**', value='`lembrar`, `falar`, `embed`, `anônimo`, `convidar`', inline=False)
        embed.set_thumbnail(url=self.client.user.avatar_url)
        embed.set_footer(icon_url=ctx.author.avatar_url, text=f'{ctx.author}')
        await ctx.send(f'{ctx.author.mention}', embed=embed)


def setup(client):
    client.add_cog(Help(client))
