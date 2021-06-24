import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import has_permissions
from discord import DMChannel

class Utilidades(commands.Cog):

    def __init__(self, client):
        self.author = None
        self.client = client

    @commands.command()
    @has_permissions(administrator=True)
    async def dm(self, ctx, member: discord.Member, *, message):
        try:
            await DMChannel.send(member, message)
            await ctx.send(f'<:ssim:850020125641408582> {ctx.author.mention}| Mensagem enviada')
        except:
            await ctx.send(f'<:nao:850020125927276641> {ctx.author.mention}| Mensagem não enviada')

    @commands.command(aliases=['falar', 'dizer', 'repeat', 'repetir'])
    async def say(self, ctx, *, message):
        if '@everyone' in ctx.message.content:
            if not ctx.author.guild_permissions.mention_everyone:
                await ctx.send(f'<:nao:850020125927276641> {ctx.author.mention}| Você não tem permissão de mencionar `@everyone`')
                return
        if '@here' in ctx.message.content:
            if not ctx.author.guild_permissions.mention_everyone:
                await ctx.send(f'<:nao:850020125927276641> {ctx.author.mention}| Você não tem permissão de mencionar `@here`')
                return
        titulo = f'*Essa mensagem foi enviada por:* {ctx.author.mention}'
        await ctx.send("{}\n\n{}".format(" {}".format(message), titulo))

    @commands.command()
    async def embed(self, ctx):
        def check(message):
            return message.author == ctx.author and message.channel == ctx.channel
        try: 
            await ctx.send('**Qual é o título da sua embed?**')
            title = await self.client.wait_for('message', timeout=60.0, check=check)
        
            await ctx.send('**Qual é a descrição da sua embed?**')
            desc = await self.client.wait_for('message', timeout=60.0, check=check)

            await ctx.send('Fazendo a embed...')
            await asyncio.sleep(1)

            embed = discord.Embed(title=title.content, description=desc.content, color=0x030058, timestamp=ctx.message.created_at)
            embed.set_footer(icon_url=ctx.author.avatar_url, text=f'{ctx.author}')
            await ctx.send(f'Embed enviada por: {ctx.author.mention}', embed=embed)
        except asyncio.TimeoutError:
            await ctx.send(f'<:nao:850020125927276641> {ctx.author.mention}| *Se passou um minuto e você não respondeu, então o comando foi cancelado.*')

    @commands.command()
    async def reminder(self, ctx, *, reminder: str):
        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel

        await ctx.send(f'⏰ {ctx.author.mention}| Quando você irá querer que eu te lembre disso?\n(`30s`, `5m`, `2h`, `7d`, `10h 40m`, etc)')
        Time = await self.client.wait_for("message", check=check)
        times = str(Time.content)
        Times = times.split()

        seconds = 0
        if reminder is None:
            await ctx.send(f'<:nao:850020125927276641> {ctx.author.mention}| Você deve dizer o que gostaria que eu te lembrasse!')
        for time in Times:
            if time.lower().endswith("d"):
                seconds += float(time[:-1]) * 60 * 60 * 24
                counter = f"{seconds // 60 // 60 // 24} dias"
            if time.lower().endswith("h"):
                seconds += float(time[:-1]) * 60 * 60
                counter = f"{seconds // 60 // 60} horas"
            if time.lower().endswith("m"):
                seconds += float(time[:-1]) * 60
                counter = f"{seconds // 60} minutos"
            if time.lower().endswith("s"):
                seconds += float(time[:-1])
                counter = f"{seconds} segundos"
            if seconds == 0:
                await ctx.send(f'<:nao:850020125927276641> {ctx.author.mention}| Especifique uma duração válida!')
            if seconds > 31536000:
                await ctx.send(f'<:nao:850020125927276641> {ctx.author.mention}| A duração especificada é muito longa, o tempo escolhido deve ser menor do que 1 ano!')

        else:
            await ctx.send(f'<:ssim:850020125641408582> {ctx.author.mention}| Eu irei te lembrar de "`{reminder}`" daqui a **{counter}**')
            await asyncio.sleep(seconds)
            await ctx.send(f'⏰ {ctx.author.mention}| **Lembrete:** "`{reminder}`"')
        

def setup(client):
    client.add_cog(Utilidades(client))