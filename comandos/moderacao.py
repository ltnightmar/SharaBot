import discord
import asyncio
import json
from discord.ext import commands
from discord.ext.commands import has_permissions
from discord import DMChannel

class Moderacao(commands.Cog):

    def __init__(self, client):
        self.author = None
        self.client = client

    @commands.command()
    @has_permissions(administrator=True)
    async def dm(self, ctx, member: discord.Member, *, message):
        try:
            titulo = f'*Essa mensagem foi enviada por:* {ctx.author.name}'
            await DMChannel.send(member, f'{message}\n\n{titulo}')
            await ctx.send(f'<:ssim:850020125641408582> {ctx.author.mention}| Mensagem enviada')
        except:
            await ctx.send(f'<:nao:850020125927276641> {ctx.author.mention}| Mensagem não enviada')

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
        
    @commands.command(aliases=['banir'])
    @has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member=None, *, reason=None):
        if reason is None:
            reason = 'Nenhum motivo especificado'
        if member is None or member == ctx.author:
            return await ctx.send(f'<:nao:850020125927276641> {ctx.author.mention}| Você não pode banir a si mesmo!')

        message = await ctx.send(f'⚠| {ctx.author.mention} Você está prestes a banir o membro {member.mention} (`{member.name}#{member.discriminator}` – `{member.id}`) do seu servidor! Para confirmar, reaja com ✅')
        for emoji in ('✅'):
            await message.add_reaction(emoji) 

            try:
                def check(reaction, user):
                    return user.id == ctx.author.id and str(reaction) == '✅'
                reation, user = await self.client.wait_for("reaction_add", check=check)
                await member.ban(reason=reason)
                await ctx.send(f'<:ssim:850020125641408582> {ctx.author.mention}| O membro {member.mention} foi banido do servidor!')
                await discord.DMChannel.send(member, f'Você foi banido do servidor {ctx.guild.name}, por {ctx.author.mention}! **Motivo: {reason}.**')
            except:
                await ctx.send(f'<:nao:850020125927276641> {ctx.author.mention}| Não foi possível banir o membro {member.mention}!')

    @commands.command(aliases=['kickar', 'expulsar'])
    @has_permissions(ban_members=True)
    async def kick(self, ctx, member: discord.Member=None, *, reason=None):
        if reason is None:
            reason = 'Nenhum motivo especificado'
        if member is None or member == ctx.author:
            return await ctx.send(f'<:nao:850020125927276641> {ctx.author.mention}| Você não pode expulsar a si mesmo!')

        message = await ctx.send(f'⚠| {ctx.author.mention} Você está prestes a expulsar o membro {member.mention} (`{member.name}#{member.discriminator}` – `{member.id}`) do seu servidor! Para confirmar, reaja com ✅')
        for emoji in ('✅'):
            await message.add_reaction(emoji) 

            try:
                def check(reaction, user):
                    return user.id == ctx.author.id and str(reaction) == '✅'
                reation, user = await self.client.wait_for("reaction_add", check=check)
                await member.kick(reason=reason)
                await ctx.send(f'<:ssim:850020125641408582> {ctx.author.mention}| O membro {member.mention} foi expulso do servidor!')
                await discord.DMChannel.send(member, f'Você foi expulso do servidor {ctx.guild.name}, por {ctx.author.mention}! **Motivo: {reason}.**')
            except:
                await ctx.send(f'<:nao:850020125927276641> {ctx.author.mention}| Não foi possível expulsar o membro {member.mention}!')
    
    @commands.command(aliases=['clean', 'apagar', 'delete', 'deletar', 'excluir'])
    @has_permissions(manage_messages = True)
    async def clear(self, ctx, amount: int = None):
        if amount is None:
            return await ctx.send(f'<:nao:850020125927276641> {ctx.author.mention}| Você precisa especificar quantas mensagens quer apagar!')
        await ctx.channel.purge(limit=amount + 1)
        await ctx.send(f'<:ssim:850020125641408582> {ctx.author.mention}| Foram excluídas `{amount}` mensagens!')


def setup(client):
    client.add_cog(Moderacao(client))