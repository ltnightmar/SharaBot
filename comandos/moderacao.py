import discord
from discord.ext import commands
import json

class Moderacao(commands.Cog):

    def __init__(self, client):
        self.author = None
        self.client = client

    @commands.command(aliases=['prefix'])
    async def prefixo(self, ctx, *, prefix=None):
        if prefix is None:
            with open('./databases/prefixes.json', 'r') as f:
                prefixes = json.load(f)
            pre = prefixes[str(ctx.guild.id)]
            return await ctx.send(f'{ctx.author.mention}| O prefixo do servidor é: `{pre}`')
        if ctx.author.guild_permissions.manage_guild:
            with open('./databases/prefixes.json', 'r') as f:
                prefixes = json.load(f)
            prefixes[str(ctx.guild.id)] = prefix
            await ctx.send(f'<:ssim:850020125641408582> {ctx.author.mention}| O prefixo do servidor foi alterado para: `{prefix}`')
            with open('./databases/prefixes.json', 'w') as f:
                json.dump(prefixes, f, indent=4)
        else:
            await ctx.send(f'<:nao:850020125927276641> {ctx.author.mention}| Para executar esse comando, você precisa ter permissão de `Gerenciar Servidor`!')


def setup(client):
    client.add_cog(Moderacao(client))