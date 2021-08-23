import discord
import asyncio
from discord.ext import commands

equipe = 825858060437946389

class Utilidades(commands.Cog):

    def __init__(self, client):
        self.author = None
        self.client = client

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

            await ctx.send('Criando a embed...')
            await asyncio.sleep(1)

            embed = discord.Embed(title=title.content, description=desc.content, color=0x030058, timestamp=ctx.message.created_at)
            embed.set_footer(icon_url=ctx.author.avatar_url, text=f'{ctx.author}')
            await ctx.send(f'Embed enviada por: {ctx.author.mention}', embed=embed)
        except asyncio.TimeoutError:
            await ctx.send(f'<:nao:850020125927276641> {ctx.author.mention}| *Se passou um minuto e você não respondeu, então o comando foi cancelado.*')

    @commands.command(aliases=['anônimo', 'anonymous', 'mensagemanonima', 'mensagem_anônima', 'anonymousmessage', 'anonymous_message'])
    async def anonimo(self, ctx):
        def check(message):
            return message.author == ctx.author and message.channel == ctx.channel
        try: 
            msg1 = await ctx.send('**Qual é o conteúdo da sua mensagem anônima?**')
            msg = await self.client.wait_for('message', timeout=60.0, check=check)
            
            file = discord.File('./assets/gifs/outros/anonimo.gif', filename='anonimo.gif')
            embed = discord.Embed(title='🕵️| Mensagem anônima', description=msg.content, color=0x030058, timestamp=ctx.message.created_at)
            embed.set_thumbnail(url='attachment://anonimo.gif')
            embed.set_footer(icon_url='attachment://anonimo.gif', text=f'Autor Anônimo')
            await msg1.delete()
            await ctx.send(f'Mensagem enviada por: **Anônimo**', file=file, embed=embed)
        except asyncio.TimeoutError:
            await ctx.send(f'<:nao:850020125927276641> {ctx.author.mention}| *Se passou um minuto e você não respondeu, então o comando foi cancelado.*')
    
    @commands.command(aliases=['lembrar', 'remind', 'remindme', 'lembrete'])
    async def reminder(self, ctx, *, reminder: str=None):
        if reminder is None:
            return await ctx.send(f'<:nao:850020125927276641> {ctx.author.mention}| Você deve dizer o que gostaria que eu te lembrasse!')
        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel

        await ctx.send(f'⏰ {ctx.author.mention}| Quando você irá querer que eu te lembre disso?\n(`30s`, `5m`, `2h`, `7d`, `10h 40m`, etc)')
        Time = await self.client.wait_for("message", check=check)
        times = str(Time.content)
        Times = times.split()

        seconds = 0
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
                return await ctx.send(f'<:nao:850020125927276641> {ctx.author.mention}| Especifique uma duração válida!')
            if seconds > 31536000:
                return await ctx.send(f'<:nao:850020125927276641> {ctx.author.mention}| A duração especificada é muito longa, o tempo escolhido deve ser menor do que 1 ano!')

        else:
            await ctx.send(f'<:ssim:850020125641408582> {ctx.author.mention}| Eu irei te lembrar de "`{reminder}`" daqui a **{counter}**')
            await asyncio.sleep(seconds)
            await ctx.send(f'⏰ {ctx.author.mention}| **Lembrete:** "`{reminder}`"')
    
    @commands.command(aliases=['invite', 'invitar', 'convite', 'comvideme', 'convide_me'])
    async def convidar(self, ctx):
        embed = discord.Embed(title='Convide-me', colour=0x030058, timestamp=ctx.message.created_at)
        embed.add_field(name=f'Me adicione à sua guild!', value='Quer me adicionar ao seu servidor? Aperte [aqui](https://discord.com/api/oauth2/authorize?client_id=800764726538797066&permissions=8&scope=bot)!', inline=False)
        embed.set_thumbnail(url=self.client.user.avatar_url)
        embed.set_footer(icon_url=ctx.author.avatar_url, text=f'{ctx.author}')
        await ctx.send(embed=embed)
    
    @commands.command()
    async def parceria(self, ctx):
        role = discord.utils.get(ctx.guild.roles, id=equipe)
        if role in ctx.author.roles:
            def check(message):
                return message.author == ctx.author and message.channel == ctx.channel
            try: 
                msg1 = await ctx.send('**Qual é o nome do servidor?**')
                server = await self.client.wait_for('message', timeout=60.0, check=check)
            
                msg2 = await ctx.send('**Mencione o representante da parceria:**')
                rep = await self.client.wait_for('message', timeout=60.0, check=check)

                embed=discord.Embed(title='<:heart:872863399996956702> Obrigado pela parceria!', description=f'💻 Servidor: {server.content}\n👑 Representante: {rep.content}')
                await ctx.message.delete()
                await msg1.delete()
                await server.delete()
                await msg2.delete()
                await rep.delete()
                parceria = await ctx.send('<@&822646385626972223>', embed=embed)
                emoji = '<:ssim:850020125641408582>'
                await parceria.add_reaction(emoji)
            except asyncio.TimeoutError:
                return
        

def setup(client):
    client.add_cog(Utilidades(client))