import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import has_permissions

class Moderacao(commands.Cog):

    def __init__(self, client):
        self.author = None
        self.client = client

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

    @commands.command(aliases=['addcargo', 'addrole', 'addcargos', 'addroles', 'adicionar_cargo', 'add_role', 'add_roles'])
    @has_permissions(manage_roles=True, manage_permissions=True)
    async def adicionarcargo(self, ctx, member: discord.Member = None, *, role: discord.Role = None):
        if member is None:
            return await ctx.send(f'<:nao:850020125927276641> {ctx.author.mention}| Comando inválido, certifique-se de seguir o **modelo abaixo**:\n> `#adicionarcargo <@membro> <@cargo>`')
        if role is None:
            return await ctx.send(f'<:nao:850020125927276641> {ctx.author.mention}| Comando inválido, certifique-se de seguir o **modelo abaixo**:\n> `#adicionarcargo <@membro> <@cargo>`')
        if role.position > ctx.author.top_role.position: 
            return await ctx.send(f'<:nao:850020125927276641> {ctx.author.mention}| Não é possivel adicionar o cargo mencionado. Motivo: o cargo está acima da sua toprole') 
        if role in member.roles:
            await ctx.send(f'<:nao:850020125927276641> {ctx.author.mention}| Esse membro já tem o cargo mencionado!')
        else:
            await member.add_roles(role)
            await ctx.send(f"<:ssim:850020125641408582> {ctx.author.mention}| O cargo {role} foi adicionado ao membro {member.mention}")     

    @commands.command(aliases=['removerole', 'removercargos', 'removeroles','remover_cargo', 'remover_cargos', 'remove_role', 'remove_roles'])
    @has_permissions(manage_roles=True, manage_permissions=True)
    async def removercargo(self, ctx, member: discord.Member = None, *, role: discord.Role = None):
        if member is None:
            return await ctx.send(f'<:nao:850020125927276641> {ctx.author.mention}| Comando inválido, certifique-se de seguir o **modelo abaixo**:\n> `#removercargo <@membro> <@cargo>`')
        if role is None:
            return await ctx.send(f'<:nao:850020125927276641> {ctx.author.mention}| Comando inválido, certifique-se de seguir o **modelo abaixo**:\n> `#removercargo <@membro> <@cargo>`')
        if role.position > ctx.author.top_role.position:
            return await ctx.send(f'<:nao:850020125927276641> {ctx.author.mention}| Não é possivel adicionar o cargo mencionado. Motivo: o cargo está acima da sua toprole') 
        if role in member.roles:
            await member.remove_roles(role)
            await ctx.send(f"<:ssim:850020125641408582> {ctx.author.mention}| O cargo {role} foi removido do membro {member.mention}")
        else: 
            await ctx.send(f'<:nao:850020125927276641> {ctx.author.mention}| Esse membro não tem o cargo mencionado!') 
    
        
def setup(client):
    client.add_cog(Moderacao(client))