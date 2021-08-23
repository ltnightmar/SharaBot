import discord
import asyncio
import json
import datetime
from discord.ext import commands

class Infos(commands.Cog):

    def __init__(self, client):
        self.author = None
        self.client = client
    
    @commands.command(aliases=['usericon'])
    async def avatar(self, ctx, *, member: discord.Member = None):
        if member is None:
            member = ctx.author
        try:
            embed = discord.Embed(title=f'🖼️ {member.name}', description=f'Aperte [aqui]({member.avatar_url}) para baixar a imagem!', colour=0x030058, timestamp=ctx.message.created_at)
            embed.set_image(url=member.avatar_url)
            embed.set_footer(icon_url=ctx.author.avatar_url, text=f'{ctx.author}')
            await ctx.send(f'{ctx.author.mention}', embed=embed)
        except:
            await ctx.send(f'<:nao:850020125927276641> {ctx.author.mention}| Não foi possível enviar o avatar desse membro. Tenha certeza que o membro mencionado está no servidor!')

    @commands.command()
    async def userinfo(self, ctx, member: discord.Member=None):
        pages = 2
        cur_page = 1
        if member is None:
            member = ctx.author
        roles = [role for role in member.roles if role != ctx.guild.default_role]
        embed = discord.Embed(title=f'<:wumpus:851156952600018944> {member}', colour=0x030058,
                              timestamp=ctx.message.created_at)
        embed.set_thumbnail(url=member.avatar_url)
        embed.add_field(name='🔖 **Nome:**', value=f'`{member.name}#{member.discriminator}`', inline=True)
        embed.add_field(name='💻 **ID:**', value=f'`{member.id}`', inline=True)
        embed.add_field(name='📅 **Criado em:**', value=f'{member.created_at.strftime("%d/%m/%Y %H:%M")}', inline=True)
        embed.add_field(name='🌟 **Entrou em:**', value=f'{member.joined_at.strftime("%d/%m/%Y %H:%M")}', inline=True)
        embed.set_footer(icon_url=ctx.author.avatar_url, text=f'{ctx.author}')
        message = await ctx.send(f'{ctx.author.mention}', embed=embed)
        await message.add_reaction("▶️")
        
        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) in ["▶️"]

        while True:
            try:
                reaction, user = await self.client.wait_for("reaction_add", timeout=60, check=check)

                if str(reaction.emoji) == "▶️" and cur_page != pages:
                    cur_page += 1
                    embed = discord.Embed(title=f'<:wumpus:851156952600018944> {member}', colour=0x030058, timestamp=ctx.message.created_at)
                    embed.set_thumbnail(url=member.avatar_url)
                    embed.add_field(name=f'💼 **Cargos ({len(roles)})**', value=' '.join([role.mention for role in roles]), inline=False)
                    embed.set_footer(icon_url=ctx.author.avatar_url, text=f'{ctx.author}')
                    await message.delete()
                    await ctx.send(embed=embed)


                else:
                    await message.remove_reaction(reaction, user)

            except asyncio.TimeoutError:
                await message.delete()
                break

    @commands.command()
    async def servericon(self, ctx):
        embed = discord.Embed(title=f'🖼️ {ctx.guild.name}', description=f'Aperte [aqui]({ctx.guild.icon_url}) para baixar a imagem!', colour=0x030058, timestamp=ctx.message.created_at)
        embed.set_image(url=ctx.guild.icon_url)
        embed.set_footer(icon_url=ctx.author.avatar_url, text=f'{ctx.author}')
        await ctx.send(f'{ctx.author.mention}', embed=embed)
    
    @commands.command()
    async def serverinfo(self, ctx):
        guild = ctx.message.guild
        chats = len(ctx.guild.text_channels) + len(ctx.guild.voice_channels)
        embed = discord.Embed(title=f'<:discord:841348284660318218> {ctx.guild.name}', colour=0x030058,
                              timestamp=ctx.message.created_at)
        embed.set_thumbnail(url=guild.icon_url)
        embed.add_field(name='👑 **Dono(a)**', value=f'`{ctx.guild.owner}`\n({ctx.guild.owner_id})', inline=True)
        embed.add_field(name='💻 **ID**', value=f'{guild.id}', inline=True)
        embed.add_field(name='🌎 **Região:**', value=f'{str(guild.region).title()}', inline=True)
        embed.add_field(name=f'💬 **Canais ({chats})**', value=f'📄 **Texto:** {len(guild.text_channels)}\n🔊 '
                                                              f'**Voz:** {len(guild.voice_channels)}', inline=True)
        embed.add_field(name='📅 **Criado em:**', value=f'{guild.created_at.strftime("%d/%m/%y às %H:%M")}', inline=True)
        embed.add_field(name=f'👥 **Membros ({guild.member_count})**', value=f'⠀', inline=True)
        embed.set_footer(icon_url=ctx.author.avatar_url, text=f'{ctx.author}')
        await ctx.send(embed=embed)

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'🏓 **Pong!** | Latência: `{round(self.client.latency * 1000)}ms`')
    
    @commands.command(aliases=['server', 'guild'])
    async def servidor(self, ctx):
        embed = discord.Embed(title=f'Entre em meus servidores!', colour=0x030058, timestamp=ctx.message.created_at)
        embed.add_field(name='Gostaria de entrar em meus servidores? Acesse os links abaixo:',
                        value='⠀\n<:coracao:850021677396000779> Nightmare: https://discord.gg/nnightmare\n\nCaso queira'
                              ' reportar um bug ou dar alguma sugestão, entre em contato com minha criadora nesse '
                              'servidor.\n\n**Criadora: **<@842741926071762944>')
        embed.set_footer(icon_url=ctx.author.avatar_url, text=f'{ctx.author}')
        await ctx.send(f'{ctx.author.mention}', embed=embed)

    @commands.command(aliases=['créditos'])
    async def creditos(self, ctx):
        embed = discord.Embed(colour=0x030058, timestamp=ctx.message.created_at)
        embed.add_field(name='Créditos', value='Programado pela <@842741926071762944>\nLinguagem utilizada: `Python`\nAinda em desenvolvimento!\nPara sugestões, entre no nosso [servidor](https://discord.gg/nnightmare)!')
        embed.set_footer(icon_url=ctx.author.avatar_url, text=f'{ctx.author}')
        await ctx.send(f'{ctx.author.mention}', embed=embed)
        
    @commands.command()
    async def uptime(self, ctx):
        delta_uptime = datetime.datetime.utcnow() - self.client.launch_time
        hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24)
        file = discord.File('./assets/gifs/outros/clock.gif', filename='clock.gif')
        e = discord.Embed(title=f"Tempo ativo", colour=0x030058, timestamp=ctx.message.created_at)
        e.add_field(name='Estou acordada há:', value=f'🦋 {days} dias\n🦋 {hours} horas\n🦋 {minutes} minutos\n🦋 {seconds} segundos')
        e.set_footer(icon_url=ctx.author.avatar_url, text=f'{ctx.author}')
        e.set_thumbnail(url='attachment://clock.gif')
        await ctx.send(f'{ctx.author.mention}', file=file, embed=e)
    

def setup(client):
    client.add_cog(Infos(client))
