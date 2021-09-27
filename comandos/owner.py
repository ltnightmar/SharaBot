import discord
from discord.app import Option, slash_command
from discord.ext import commands
import utils.save

class Owner(commands.Cog):
    def __init__(self, client):
        self.author = None
        self.client = client
        
    @slash_command(description='〘 👑 Owner 〙Retorna o id e nome dos servidores do bot')
    @commands.is_owner()
    async def guilds(self, ctx):
        message = ""
        for guild in self.client.guilds:
            message += f'**{guild.name}**, `{guild.id}`\n'
        await ctx.respond(f'----------\n{message}----------')
    
    @guilds.error
    async def guilds_error(self, ctx, error):
        if isinstance(error, commands.NotOwner):
            await ctx.respond('Esse comando só pode ser utilizado pela minha dona!')
            return
        
    @slash_command(description='〘 👑 Owner 〙O bot sai da guild do id informado')
    @commands.is_owner()
    async def leave(self, ctx, id: Option(str, description='ID da guild que o bot irá sair', required=True)):
        await self.client.leave_guild(int(id))
        await ctx.respond(embed=discord.Embed(description=f'{utils.save.s} Eu saí desse servidor!'))
        
    @leave.error
    async def leave_error(self, ctx, error):
        if isinstance(error, commands.NotOwner):
            await ctx.respond('Esse comando só pode ser utilizado pela minha dona!')
            return
        
def setup(client):
    client.add_cog(Owner(client))