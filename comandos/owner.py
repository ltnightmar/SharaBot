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
        await ctx.defer()
        message = ""
        for guild in self.client.guilds:
            message += f'**{guild.name}**, `{guild.id}`\n'
        await ctx.respond(f'----------\n{message}----------')
    
    @guilds.error
    async def on_command_error(self, ctx, error):
        await ctx.defer()
        if isinstance(error, commands.NotOwner):
            msg = await ctx.respond(embed=discord.Embed(description=f'Apenas a criadora do bot pode executar esse comando!'))
            await msg.add_reaction(utils.save.n)
        else:
            pass
			
    @slash_command(description='〘 👑 Owner 〙O bot sai da guild do id informado')
    @commands.is_owner()
    async def leave(self, ctx, id: Option(int, description='ID da guild que o bot irá sair', required=True)):
        await ctx.defer()
        guild = discord.utils.get(self.bot.guilds, id=id)
        await self.client.leave_guild(guild)
        await ctx.send(f":ok_hand: Left guild: {guild.name} ({guild.id})")
        
def setup(client):
    client.add_cog(Owner(client))