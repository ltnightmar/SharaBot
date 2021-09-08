import discord
from discord.ext import commands
import json

class Informacoes(commands.Cog):

    def __init__(self, client):
        self.author = None
        self.client = client
    
    @commands.command(aliases=['ajuda', 'comandos'])
    async def help(self, ctx):
        with open('./databases/prefixes.json', 'r') as f:
            prefixes = json.load(f)
        pre = prefixes[str(ctx.guild.id)]
        embed = discord.Embed(title='✉️ Menu de Ajuda', description=f'✨ Olá **{ctx.author.name}**, meu nome é Shara. Prazer em conhecer! O meu prefixo nesse servidor é: {pre}', colour=0x030058, timestamp=ctx.message.created_at)
        embed.add_field(name='📚 Comandos', value=f'Os comandos estão atualmente indisponíveis devido à manutenções', inline=False)
        embed.add_field(name='💎 Servidor', value='https://discord.gg/9XYGv8sG7F', inline=False)
        embed.add_field(name='🛠️ Criadora', value='**Fui criada pela:** Queen of Darkness#0666', inline=False)
        embed.set_thumbnail(url=self.client.user.avatar_url)
        embed.set_footer(icon_url=ctx.author.avatar_url, text=f'{ctx.author}')
        await ctx.send(ctx.author.mention, embed=embed)

def setup(client):
    client.add_cog(Informacoes(client))