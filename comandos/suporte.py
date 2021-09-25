from random import choice
import discord
from discord.ext import commands
from discord.app import Option, slash_command
import utils.save
import datetime

class Suporte(commands.Cog):
    def __init__(self, client):
        self.author = None
        self.client = client
        
    @slash_command(guild_ids = utils.save.ides, description='〘 🧰 Suporte 〙Envia sua sugestão sobre mim ao meu servidor de suporte')
    async def sugerir(self, ctx,
                      bot: Option(str, description='Bot que deseja enviar uma sugestão', required=True, choices=['Shara', 'Ophelia']),
                      sugestão: Option(str, description='Sugestão que deseja fazer', required=True)):
        embed=discord.Embed(title='💡 Sugestão')
        embed.set_author(icon_url=ctx.author.avatar.url, name=f'{ctx.author}')
        embed.add_field(name='Bot:', value=bot.capitalize(), inline=False)
        embed.add_field(name='Sugestão:', value=sugestão.capitalize(), inline=False)
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f'User ID: {ctx.author.id}')
        msg = await self.client.get_channel(889322005265014854).send(embed=embed)
        await ctx.defer()
        message = await ctx.respond(embed=discord.Embed(description=f'A sua sugestão foi enviada com sucesso!'))
        await message.add_reaction(utils.save.s)
        await msg.add_reaction(utils.save.s)
        await msg.add_reaction(utils.save.n)
    
    @slash_command(guild_ids = utils.save.ides, description='〘 🧰 Suporte 〙Envia sua denúncia sobre um membro ao meu servidor de suporte')
    async def denunciar(self, ctx,
                        motivo: Option(str, description='Motivo pelo qual está fazendo esse denúncia', required=True),
                        id: Option(str, description='ID do membro que deseja denunciar', required=True),
                        provas: Option(str, description='Anexe aqui o link das imagens que contém as provas da sua denúncia', required=True)):
        embed=discord.Embed(title=f'{utils.save.alert} Denúncia')
        embed.set_author(icon_url=ctx.author.avatar.url, name=f'{ctx.author}')
        embed.add_field(name='Motivo:', value=motivo.capitalize(), inline=False)
        embed.add_field(name='ID do denunciado:', value=id, inline=False)
        embed.add_field(name='Link das provas:', value=provas, inline=False)
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f'User ID: {ctx.author.id}')
        await self.client.get_channel(889320064342437958).send(embed=embed)
        await ctx.defer()
        message = await ctx.respond(embed=discord.Embed(description=f'A sua denúncia foi enviada com sucesso!'))
        await message.add_reaction(utils.save.s)
        
    @slash_command(guild_ids = utils.save.ides, description='〘 🧰 Suporte 〙Envia sua reportação de bug ao meu servidor de suporte')
    async def bug(self, ctx,
                  bot: Option(str, description='Bot onde encontrou o bug', required=True, choices=['Shara', 'Ophelia']),
                  bug: Option(str, description='Bug que deseja reportar', required=True),
                  imagem: Option(str, description='Link da imagem do bug', required=False)):
        embed=discord.Embed(title=f'{utils.save.no} Bug reportado')
        embed.set_author(icon_url=ctx.author.avatar.url, name=f'{ctx.author}')
        embed.add_field(name='Bot:', value=bot.capitalize(), inline=False)
        embed.add_field(name='Bug:', value=bug.capitalize(), inline=False)
        if imagem is not None:
            embed.add_field(name='Imagem do bug:', value=imagem, inline=False)
        else:
            pass
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f'User ID: {ctx.author.id}')
        await self.client.get_channel(889322942352207964).send(embed=embed)
        await ctx.defer()
        message = await ctx.respond(embed=discord.Embed(description=f'A sua reportação de bug foi enviada com sucesso!'))
        await message.add_reaction(utils.save.s)

def setup(client):
    client.add_cog(Suporte(client))