import discord
import json
import regex
import asyncio
import datetime
from discord import utils
from discord.ext.commands import has_permissions
from discord import DMChannel
from discord.ext import commands

equipe = 878821582657687613

class Utilidades(commands.Cog):

    def __init__(self, client):
        self.author = None
        self.client = client

    @commands.group(aliases=['chatglobal', 'chat_global', 'global_chat'], invoke_without_command=True)
    async def globalchat(self, ctx):
        with open('./databases/prefixes.json', 'r') as f:
            prefixes = json.load(f)
        pre = prefixes[str(ctx.guild.id)]
        embed = discord.Embed(title='🌎 Chat Global')
        embed.add_field(name='⚙️ Comandos disponíveis', value=f'`{pre}chatglobal iniciar #chat` : Inicia o chat global no canal mencionado\n`{pre}chatglobal finalizar` : Finaliza o chat global no servidor')
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(icon_url=ctx.author.avatar_url, text=ctx.author.name)
        return await ctx.send(ctx.author.mention, embed=embed)
    
    @globalchat.command(aliases=['começar', 'comecar', 'iniciar'])
    @commands.has_permissions(manage_guild=True)
    async def start(self, ctx, channel=None):
        if channel is None:
            with open('./databases/prefixes.json', 'r') as f:
                prefixes = json.load(f)
            pre = prefixes[str(ctx.guild.id)]
            embed = discord.Embed(title='🌎 Chat Global')
            embed.add_field(name='⚙️ Comandos disponíveis', value=f'`{pre}chatglobal iniciar #chat` : Inicia o chat global no canal mencionado\n`{pre}chatglobal finalizar` : Finaliza o chat global no servidor')
            embed.timestamp = datetime.datetime.utcnow()
            embed.set_footer(icon_url=ctx.author.avatar_url, text=ctx.author.name)
            return await ctx.send(ctx.author.mention, embed=embed)

        guild_id = ctx.message.guild.id
        channel_id = int(channel.strip('<>#'))
        with open('./databases/global_chat.json', 'r') as file:
            global_chat_data = json.load(file)
            new_global_chat = str(guild_id)

            if new_global_chat in global_chat_data:
                msg = await ctx.send(ctx.author.mention, embed=discord.Embed(description=f'O `Chat Global` já foi atribuído anteriormente ao servidor!'))
                await msg.add_reaction('<:nao:850020125927276641>')
            else:
                global_chat_data[new_global_chat] = channel_id
                with open('./databases/global_chat.json', 'w') as new_global_chat:
                    json.dump(global_chat_data, new_global_chat, indent=4)
                with open('./databases/prefixes.json', 'r') as f:
                    prefixes = json.load(f)
                pre = prefixes[str(ctx.guild.id)]
                msg = await ctx.send(ctx.author.mention, embed=discord.Embed(description=f'O `Chat Global` foi atribuído ao chat {channel} com sucesso!'))
                await msg.add_reaction('<:ssim:850020125641408582>')

    @globalchat.command(aliases=['finalizar', 'parar', 'terminar'])
    @commands.has_permissions(manage_guild=True)
    async def stop(self, ctx):
        guild_id = ctx.message.guild.id
        with open('./databases/global_chat.json', 'r') as file:
            global_chat_data = json.load(file)
        global_chat_data.pop(str(guild_id))
        with open('./databases/global_chat.json', 'w') as update_global_chat_file:
            json.dump(global_chat_data, update_global_chat_file, indent=4)
        msg = await ctx.send(ctx.author.mention, embed=discord.Embed(description='O `Chat Global` foi desatribuído ao servidor!'))
        await msg.add_reaction('<:ssim:850020125641408582>')

    @commands.Cog.listener()
    async def on_message(self, message):
        if not message.author.bot:
            if not message.content.startswith('#'):
                with open('./databases/global_chat.json', 'r') as file:
                    global_chat_data = json.load(file)

                channel_id = list(global_chat_data.values())

                urls = regex.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',message.content.lower())
                if message.channel.id in channel_id:
                    for ids in channel_id:
                        if message.channel.id != ids:
                            if message.author.id == 842741926071762944:
                                pass
                            else:
                                if urls and message.channel.id in channel_id:
                                    return await self.client.get_channel(message.channel.id).send(f'{message.author.mention} A mensagem contém um link, portanto não foi enviada no chat global!')
                                if 'discord.gg/' in message.content:
                                    return await self.client.get_channel(message.channel.id).send(f'{message.author.mention} A mensagem contém um convite de servidor, portanto não foi enviada no chat global!')
                                if 'dc.gg/' in message.content:
                                    return await self.client.get_channel(message.channel.id).send(f'{message.author.mention} A mensagem contém um convite de servidor, portanto não foi enviada no chat global!')
                                if '@everyone' in message.content:
                                    return await self.client.get_channel(message.channel.id).send(f'{message.author.mention} A mensagem contém uma menção global, então não foi enviada no chat global!')
                                if '@here' in message.content:
                                    return await self.client.get_channel(message.channel.id).send(f'{message.author.mention} A mensagem contém uma menção global, então não foi enviada no chat global!')
                            tchannel = self.client.get_channel(ids)
                            webhooks = await tchannel.webhooks()
                            webhook = utils.get(webhooks, name='Chat Global')
                            if webhook is None:
                                webhook = await tchannel.create_webhook(name='Chat Global')
                            
                            if message.reference is not None:
                                if message.attachments:
                                    embed = discord.Embed()
                                    embed.set_image(url=message.attachments[0].url)
                                    msg = await message.channel.fetch_message(message.reference.message_id)
                                    author = msg.author.name
                                    if not message.content:
                                        await webhook.send(content=f'> {msg.content}\n**@{author}**', username=message.author.name, avatar_url=message.author.avatar_url, embed=embed)
                                    else:
                                        await webhook.send(content=f'> {msg.content}\n**@{author}** {message.content}', username=message.author.name, avatar_url=message.author.avatar_url, embed=embed)
                                else:
                                    msg = await message.channel.fetch_message(message.reference.message_id)
                                    author = msg.author.name
                                    await webhook.send(content=f'> {msg.content}\n**@{author}** {message.content}', username=message.author.name, avatar_url=message.author.avatar_url)

                            elif message.reference is None:
                                if message.attachments:
                                    embed = discord.Embed()
                                    embed.set_image(url=message.attachments[0].url)
                                    if not message.content:
                                        message.content = f'Mídia de **{message.author.name}**'
                                        await webhook.send(content=f'{message.content}', username=message.author.name, avatar_url=message.author.avatar_url, embed=embed)
                                    else:
                                        await webhook.send(content=f'{message.content}', username=message.author.name, avatar_url=message.author.avatar_url, embed=embed)
                                else:
                                    await webhook.send(content=f'{message.content}', username=message.author.name, avatar_url=message.author.avatar_url)                         

    @commands.command(aliases=['em'])
    async def embed(self, ctx):
        try: 
            def check(message):
                return message.author == ctx.author and message.channel == ctx.channel 
            embed1 = discord.Embed(title='⚙ Configuração de Embed', description='🔨 Digite o título da sua embed')
            embed1.set_footer(text='Concluído: 1/4')
            em1 = await ctx.send(embed=embed1)
            await em1.add_reaction('<a:loading:882835568529133588>')
            title = await self.client.wait_for('message', timeout=60.0, check=check)
            await em1.delete()
            await title.delete()

            embed2 = discord.Embed(title='⚙ Configuração de Embed', description='🔨 Digite a descrição da sua embed')
            embed2.set_footer(text='Concluído: 2/4')
            em2 = await ctx.send(embed=embed2)
            await em2.add_reaction('<a:loading:882835568529133588>')
            desc = await self.client.wait_for('message', timeout=60.0, check=check)
            await em2.delete()
            await desc.delete()

            rosa = '<:rosa:883061682786684969>'
            vermelho = '<:vermelho:883061682983805038>'
            laranja = '<:laranja:883061683004788737>'
            amarelo = '<:amarelo:883061682757308547>'
            verde = '<:verdeclaro:883061682895724555>'
            azulclaro = '<:azulclaro:883061701514256435>'
            azulescuro = '<:azulescuro:883061682795053117>'
            roxo = '<:roxo:883061682719555664>'
            marrom = '<:marrom:883061682757328926>'
            preto = '<:preto:883061682656669797>'
            cinza = '<:cinza:883061682652463187>'
            branco = '<:branco:883064495709253712>'

            reactions = ['<:rosa:883061682786684969>', '<:vermelho:883061682983805038>', '<:laranja:883061683004788737>', '<:amarelo:883061682757308547>', '<:verdeclaro:883061682895724555>', '<:azulclaro:883061701514256435>', '<:azulescuro:883061682795053117>', '<:roxo:883061682719555664>', '<:marrom:883061682757328926>', '<:preto:883061682656669797>', '<:cinza:883061682652463187>', '<:branco:883064495709253712>']

            def check(reaction, user):
                return user == ctx.author and str(reaction.emoji) in reactions
            embed3 = discord.Embed(title='⚙ Configuração de Embed', description='🔨 Reaja com a cor da sua embed')
            embed3.set_footer(text='Concluído: 3/4')
            em3 = await ctx.send(embed=embed3)
            

            await em3.add_reaction(rosa)
            await em3.add_reaction(vermelho)
            await em3.add_reaction(laranja)
            await em3.add_reaction(amarelo)
            await em3.add_reaction(verde)
            await em3.add_reaction(azulclaro)
            await em3.add_reaction(azulescuro)
            await em3.add_reaction(roxo)
            await em3.add_reaction(marrom)
            await em3.add_reaction(preto)
            await em3.add_reaction(cinza)
            await em3.add_reaction(branco)

            reaction, user = await self.client.wait_for('reaction_add', timeout=60.0, check=check)
            await em3.delete()

            if str(reaction.emoji) == rosa:
                color = 0xff006e
            elif str(reaction.emoji) == vermelho:
                color = 0xff0022
            elif str(reaction.emoji) == laranja:
                color = 0xff5d00
            elif str(reaction.emoji) == amarelo:
                color = 0xfbe500
            elif str(reaction.emoji) == verde:
                color = 0x47ff00
            elif str(reaction.emoji) == azulclaro:
                color = 0x00ece5
            elif str(reaction.emoji) == azulescuro:
                color = 0x0000ff
            elif str(reaction.emoji) == roxo:
                color = 0xa200c4
            elif str(reaction.emoji) == marrom:
                color = 0x924d23
            elif str(reaction.emoji) == preto:
                color = 0x000000
            elif str(reaction.emoji) == cinza:
                color = 0x202225
            elif str(reaction.emoji) == branco:
                color = 0xffffff

            embed = discord.Embed(title=title.content, description=desc.content, colour=color)
            
            sim = '<a:sim:843161552646963220>'
            nao = '<a:nao:843161602957770812>'
            
            reacoes = ['<a:sim:843161552646963220>', '<a:nao:843161602957770812>']

            def check(reaction, user):
                return user == ctx.author and str(reaction.emoji) in reacoes
            embed4 = discord.Embed(title='⚙ Configuração de Embed', description='🔨 Deseja que sua embed tenha mídia?')
            embed4.set_footer(text='Concluído: 4/4')
            em4 = await ctx.send(embed=embed4)

            await em4.add_reaction(sim)
            await em4.add_reaction(nao)

            reaction, user = await self.client.wait_for('reaction_add', timeout=60.0, check=check)

            await em4.delete()

            if str(reaction.emoji) == sim:
                def check(message):
                    return message.author == ctx.author and message.channel == ctx.channel
                embed5 = discord.Embed(title='⚙ Configuração de Embed', description='🔨 Envie a mídia')
                embed5.add_field(name='Não disponível:', value='・Links\n・Vídeos')
                embed5.add_field(name='Disponível:', value='・Gifs\n・Imagens')
                em5 = await ctx.send(embed=embed5)
                await em5.add_reaction('<a:loading:882835568529133588>')

                midia = await self.client.wait_for('message', timeout=60.0, check=check)

                await em5.delete()
                await midia.delete()

                if midia.attachments:
                    embed.timestamp = datetime.datetime.utcnow()
                    embed.set_footer(icon_url=ctx.author.avatar_url, text=ctx.author.name)
                    embed.set_image(url=midia.attachments[0].url)
                    if ctx.author.guild_permissions.administrator:
                        return await ctx.send(embed=embed)
                    else:
                        return await ctx.send(f'Embed enviada por: {ctx.author.mention}', embed=embed)
                else:
                    embed.timestamp = datetime.datetime.utcnow()
                    embed.set_footer(icon_url=ctx.author.avatar_url, text=ctx.author.name)
                    await ctx.send(f'<:nao:850020125927276641>| Não consegui utilizar o arquivo enviado, tente novamente com outra mídia')
                    if ctx.author.guild_permissions.administrator:
                        return await ctx.send(embed=embed)
                    else:
                        return await ctx.send(f'Embed enviada por: {ctx.author.mention}', embed=embed)

            elif str(reaction.emoji) == nao:
                embed.timestamp = datetime.datetime.utcnow()
                embed.set_footer(icon_url=ctx.author.avatar_url, text=ctx.author.name)
                if ctx.author.guild_permissions.administrator:
                    return await ctx.send(embed=embed)
                else:
                    return await ctx.send(f'Embed enviada por: {ctx.author.mention}', embed=embed)

        except asyncio.TimeoutError:
            await ctx.send(f'<:nao:850020125927276641>| Se passou um minuto e você não respondeu, então o comando foi cancelado.')


def setup(client):
    client.add_cog(Utilidades(client))