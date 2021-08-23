import discord
import asyncio
import random
import os
from PIL import Image
from io import BytesIO
from discord.ext import commands

class Diversao(commands.Cog):

    def __init__(self, client):
        self.author = None
        self.client = client


    @commands.command(aliases=['abraçar', 'abraço', 'abracar', 'abraco'])
    async def hug(self, ctx, member: discord.Member = None):
        if member is None:
            await ctx.send(f'<:nao:850020125927276641> {ctx.author.mention}| Você precisa mencionar alguém!')

        number = random.randint(1, 20)
        file = discord.File('./assets/gifs/hugs/hug{}.gif'.format(number), filename='hug{}.gif'.format(number))
        embed = discord.Embed(color=0x030058)
        embed.add_field(name='💖 ABRAÇO!', value=f'{ctx.author.mention} envolveu {member.mention} em um abraço!')
        embed.set_image(url='attachment://hug{}.gif'.format(number))
        embed.set_footer(text="Reaja com 💖 para retribuir")
        message = await ctx.send(file=file, embed=embed)
        for emoji in ('💖'):
            await message.add_reaction(emoji) 

            try:
                def check(rctn, user):
                    return user.id == member.id and str(rctn) == '💖'
                rctn, user = await self.client.wait_for("reaction_add", check=check, timeout=120)

                numbr = random.randint(1, 20)
                fil = discord.File('./assets/gifs/hugs/hug{}.gif'.format(numbr), filename='hug{}.gif'.format(numbr))
                embd = discord.Embed(color=0x030058)
                embd.add_field(name='💖 ABRAÇO!', value=f'{member.mention} envolveu {ctx.author.mention} em um abraço!')
                embd.set_image(url='attachment://hug{}.gif'.format(numbr))
                await ctx.send(file=fil, embed=embd)

            except asyncio.TimeoutError:
                print(' ')

    @commands.command(aliases=['beijo', 'beijar'])
    async def kiss(self, ctx, member: discord.Member = None):
        if member is None:
            await ctx.send(f'<:nao:850020125927276641> {ctx.author.mention}| Você precisa mencionar alguém!')

        number = random.randint(1, 20)
        file = discord.File('./assets/gifs/kisses/kiss{}.gif'.format(number), filename='kiss{}.gif'.format(number))
        embed = discord.Embed(color=0x030058)
        embed.add_field(name='💏 BEIJO!', value=f'{ctx.author.mention} deu um beijo em {member.mention}!')
        embed.set_image(url='attachment://kiss{}.gif'.format(number))
        embed.set_footer(text="Reaja com 💏 para retribuir")
        message = await ctx.send(file=file, embed=embed)
        for emoji in ('💏'):
            await message.add_reaction(emoji) 

            try:
                def check(rctn, user):
                    return user.id == member.id and str(rctn) == '💏'
                rctn, user = await self.client.wait_for("reaction_add", check=check, timeout=120)

                numbr = random.randint(1, 20)
                fil = discord.File('./assets/gifs/kisses/kiss{}.gif'.format(numbr), filename='kiss{}.gif'.format(numbr))
                embd = discord.Embed(color=0x030058)
                embd.add_field(name='💏 BEIJO!', value=f'{member.mention} deu um beijo em {ctx.author.mention}!')
                embd.set_image(url='attachment://kiss{}.gif'.format(numbr))
                await ctx.send(file=fil, embed=embd)

            except asyncio.TimeoutError:
                print(' ')

    @commands.command(aliases=['matar', 'assassinar', 'assassinato'])
    async def kill(self, ctx, member: discord.Member = None):
        if member is None:
            await ctx.send(f'<:nao:850020125927276641> {ctx.author.mention}| Você precisa mencionar alguém!')

        number = random.randint(1, 20)
        file = discord.File('./assets/gifs/kills/kill{}.gif'.format(number), filename='kill{}.gif'.format(number))
        embed = discord.Embed(color=0x030058)
        embed.add_field(name='🔫 ASSASSINATO!', value=f'{ctx.author.mention} matou {member.mention}!')
        embed.set_image(url='attachment://kill{}.gif'.format(number))
        embed.set_footer(text="Reaja com 🔫 para retribuir")
        message = await ctx.send(file=file, embed=embed)
        for emoji in ('🔫'):
            await message.add_reaction(emoji) 

            try:
                def check(rctn, user):
                    return user.id == member.id and str(rctn) == '🔫'
                rctn, user = await self.client.wait_for("reaction_add", check=check, timeout=120)

                numbr = random.randint(1, 20)
                fil = discord.File('./assets/gifs/kills/kill{}.gif'.format(numbr), filename='kill{}.gif'.format(numbr))
                embd = discord.Embed(color=0x030058)
                embd.add_field(name='🔫 ASSASSINATO!', value=f'{member.mention} matou {ctx.author.mention}!')
                embd.set_image(url='attachment://kill{}.gif'.format(numbr))
                await ctx.send(file=fil, embed=embd)

            except asyncio.TimeoutError:
                print(' ')


    @commands.command(aliases=['bofetar', 'bofetada', 'tapa'])
    async def slap(self, ctx, member: discord.Member = None):
        if member is None:
            await ctx.send(f'<:nao:850020125927276641> {ctx.author.mention}| Você precisa mencionar alguém!')

        number = random.randint(1, 18)
        file = discord.File('./assets/gifs/slaps/slap{}.gif'.format(number), filename='slap{}.gif'.format(number))
        embed = discord.Embed(color=0x030058)
        embed.add_field(name='💥 TAPA!', value=f'{ctx.author.mention} deu um tapa em {member.mention}!')
        embed.set_image(url='attachment://slap{}.gif'.format(number))
        embed.set_footer(text="Reaja com 💥 para retribuir")
        message = await ctx.send(file=file, embed=embed)
        for emoji in ('💥'):
            await message.add_reaction(emoji) 

            try:
                def check(rctn, user):
                    return user.id == member.id and str(rctn) == '💥'
                rctn, user = await self.client.wait_for("reaction_add", check=check, timeout=120)

                numbr = random.randint(1, 18)
                fil = discord.File('./assets/gifs/slaps/slap{}.gif'.format(numbr), filename='slap{}.gif'.format(numbr))
                embd = discord.Embed(color=0x030058)
                embd.add_field(name='💥 TAPA!', value=f'{member.mention} deu um tapa em {ctx.author.mention}!')
                embd.set_image(url='attachment://slap{}.gif'.format(numbr))
                await ctx.send(file=fil, embed=embd)

            except asyncio.TimeoutError:
                print(' ')

    @commands.command(aliases=['soco', 'socar', 'bater'])
    async def punch(self, ctx, member: discord.Member = None):
        number = random.randint(1, 20)
        file = discord.File('./assets/gifs/punches/punch{}.gif'.format(number), filename='punch{}.gif'.format(number))
        embed = discord.Embed(color=0x030058)
        embed.add_field(name='👊 SOCO!', value=f'{ctx.author.mention} deu um soco em {member.mention}!')
        embed.set_image(url='attachment://punch{}.gif'.format(number))
        embed.set_footer(text="Reaja com 👊 para retribuir")
        message = await ctx.send(file=file, embed=embed)
        for emoji in ('👊'):
            await message.add_reaction(emoji) 

            try:
                def check(rctn, user):
                    return user.id == member.id and str(rctn) == '👊'
                rctn, user = await self.client.wait_for("reaction_add", check=check, timeout=120)

                numbr = random.randint(1, 20)
                fil = discord.File('./assets/gifs/punches/punch{}.gif'.format(numbr), filename='punch{}.gif'.format(numbr))
                embd = discord.Embed(color=0x030058)
                embd.add_field(name='👊 SOCO!', value=f'{member.mention} deu um soco em {ctx.author.mention}!')
                embd.set_image(url='attachment://punch{}.gif'.format(numbr))
                await ctx.send(file=fil, embed=embd)

            except asyncio.TimeoutError:
                print(' ')

    @commands.command(aliases=['procurase', 'procura-se', 'procurado'])
    async def wanted(self, ctx, member: discord.Member = None):
        if member is None:
            member = ctx.author

        wanted = Image.open('./assets/imagens/wanted.jpg')
        asset = member.avatar_url_as(size=128)
        data = BytesIO(await asset.read())
        pfp = Image.open(data)
        pfp = pfp.resize((641, 600))
        wanted.paste(pfp, (178, 443))
        wanted.save('./assets/imagens/nwanted.jpg')
        await ctx.send(file = discord.File('./assets/imagens/nwanted.jpg'))
        os.remove('./assets/imagens/nwanted.jpg')

    @commands.command(aliases=['restinpeace', 'descanseempaz', 'rest_in_peace', 'descanse_em_paz', 'morreu'])
    async def rip1(self, ctx, member: discord.Member = None):
        if member is None:
            member = ctx.author
        
        wanted = Image.open('./assets/imagens/rip.jpg')
        asset = member.avatar_url_as(size=128)
        data = BytesIO(await asset.read())
        pfp = Image.open(data)
        pfp = pfp.resize((122, 107))
        wanted.paste(pfp, (132, 331))
        wanted.save('./assets/imagens/nrip.jpg')
        await ctx.send(file = discord.File('./assets/imagens/nrip.jpg'))
        os.remove('./assets/imagens/nrip.jpg')

    @commands.command(aliases=['restinpeace2', 'descanseempaz2', 'rest_in_peace2', 'descanse_em_paz2', 'morreu2'])
    async def rip2(self, ctx, member: discord.Member = None):
        if member is None:
            member = ctx.author

        wanted = Image.open('./assets/imagens/rip2.jpg')
        asset = member.avatar_url_as(size=128)
        data = BytesIO(await asset.read())
        pfp = Image.open(data)
        pfp = pfp.resize((148, 138))
        wanted.paste(pfp, (98, 220))
        wanted.save('./assets/imagens/nrip2.jpg')
        await ctx.send(file = discord.File('./assets/imagens/nrip2.jpg'))
        os.remove('./assets/imagens/nrip2.jpg')

    @commands.command(aliases=['caraecoroa', 'caraoucoroa', 'coroaecara', 'coroaoucara'])
    async def coinflip(self, ctx):
        moedas = [f'<:coroa:856319981049872404> {ctx.author.mention}**| Coroa!**', f'<:cara:856319978584408074> {ctx.author.mention}**| Cara!**']
        moeda = random.choice(moedas)
        await ctx.send(moeda)


def setup(client):
    client.add_cog(Diversao(client))
