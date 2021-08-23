import discord
import asyncio
import random
import json
from discord.ext import commands
from discord.ext.commands import has_permissions

class Gerenciamento(commands.Cog):

    def __init__(self, client):
        self.author = None
        self.client = client

    @commands.command(aliases=['trancar', 'fechar'], pass_context=True)
    @has_permissions(manage_channels=True)
    async def lock(self, ctx, channel : discord.TextChannel=None):
        channel = channel or ctx.channel
        await channel.set_permissions(ctx.guild.default_role, send_messages=False)
        await ctx.send(f'<:ssim:850020125641408582> {ctx.author.mention}| O chat {channel.mention} foi bloqueado com sucesso!')
    
    @commands.command(aliases=['destrancar', 'abrir'], pass_context=True)
    @has_permissions(manage_channels=True)
    async def unlock(self, ctx, channel : discord.TextChannel=None):
        channel = channel or ctx.channel
        await channel.set_permissions(ctx.guild.default_role, send_messages=True)
        await ctx.send(f'<:ssim:850020125641408582> {ctx.author.mention}| O chat {channel.mention} foi desbloqueado com sucesso!')

    @commands.group(invoke_without_command=True, aliases=['create'])
    async def criar(self, ctx):
        await ctx.send(f'{ctx.author.mention}\n**Comandos disponíveis:**\n> `#criar cargo <nome>`\n> `#criar chat <nome>`\n> `#criar call <nome>`\n> `#criar categoria <nome>`')

    @criar.command(aliases=['role', 'roles', 'cargos'])
    @has_permissions(manage_channels=True)
    async def cargo(self, ctx, *, nome):
        await ctx.guild.create_role(name=nome)
        await ctx.send(f'<:ssim:850020125641408582> {ctx.author.mention}| Um cargo com o nome `@{nome}`, foi criado!')

    @criar.command(aliases=['channel', 'textchannel', 'text_channel'])
    @has_permissions(manage_channels=True)
    async def chat(self, ctx, *, nome):
        await ctx.guild.create_text_channel(name=nome)
        await ctx.send(f'<:ssim:850020125641408582> {ctx.author.mention}| Um chat com o nome `#{nome}`, foi criado!')

    @criar.command(aliases=['voicechannel', 'voice_channel'])
    @has_permissions(manage_channels=True)
    async def call(self, ctx, *, nome):
        await ctx.guild.create_voice_channel(name=nome)
        await ctx.send(f'<:ssim:850020125641408582> {ctx.author.mention}| Uma call com o nome `#{nome}`, foi criada!')

    @criar.command(aliases=['category',])
    @has_permissions(manage_channels=True)
    async def categoria(self, ctx, *, nome):
        await ctx.guild.create_category(name=nome)
        await ctx.send(f'<:ssim:850020125641408582> {ctx.author.mention}| Uma categoria com o nome `#{nome}`, foi criada!')
    
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
    client.add_cog(Gerenciamento(client))