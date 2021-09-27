import discord
from discord.ext import commands
import asyncio
from discord.app import Option, slash_command
import utils.save
import datetime
import json
import regex
import os


class Utilidades(commands.Cog):
    def __init__(self, client):
        self.author = None
        self.client = client
        
 
    @slash_command(description='〘 🛠️  Utilidades 〙Envia uma mensagem especificada pelo usuário')
    async def falar(self, ctx, 
                    mensagem: Option(str, description='Mensagem que deseja enviar', required=True, default=True),
                    membro: Option(discord.Member, description='Usuário pra quem deseja enviar a mensagem', required=False, default=None)):
        if membro == None:
            await ctx.respond(f'**@{ctx.author.name}** Disse:\n`{mensagem}`')
        else:
            await ctx.respond(f'**@{ctx.author.name}** Disse para {membro.mention}:\n`{mensagem}`')
    
    @slash_command(description='〘 🛠️  Utilidades 〙Cria uma embed personalizada')
    async def embed(self, ctx):
        await ctx.defer()
        try: 
            def check(message):
                return message.author == ctx.author and message.channel == ctx.channel 
            embed1 = discord.Embed(title='⚙ Configuração de Embed', description='🔨 Digite o título da sua embed')
            embed1.set_footer(text='Concluído: 1/4')
            em1 = await ctx.send(embed=embed1)
            await em1.add_reaction(utils.save.loading)
            title = await self.client.wait_for('message', timeout=60.0, check=check)
            await em1.delete()
            await title.delete()

            embed2 = discord.Embed(title='⚙ Configuração de Embed', description='🔨 Digite a descrição da sua embed')
            embed2.set_footer(text='Concluído: 2/4')
            em2 = await ctx.send(embed=embed2)
            await em2.add_reaction(utils.save.loading)
            desc = await self.client.wait_for('message', timeout=60.0, check=check)
            await em2.delete()
            await desc.delete()

            def check(reaction, user):
                return user == ctx.author and str(reaction.emoji) in utils.save.embed_colors
            embed3 = discord.Embed(title='⚙ Configuração de Embed', description='🔨 Reaja com a cor da sua embed')
            embed3.set_footer(text='Concluído: 3/4')
            em3 = await ctx.send(embed=embed3)

            await em3.add_reaction(utils.save.rosa)
            await em3.add_reaction(utils.save.vermelho)
            await em3.add_reaction(utils.save.laranja)
            await em3.add_reaction(utils.save.amarelo)
            await em3.add_reaction(utils.save.verde)
            await em3.add_reaction(utils.save.azulclaro)
            await em3.add_reaction(utils.save.azulescuro)
            await em3.add_reaction(utils.save.roxo)
            await em3.add_reaction(utils.save.marrom)
            await em3.add_reaction(utils.save.preto)
            await em3.add_reaction(utils.save.cinza)
            await em3.add_reaction(utils.save.branco)

            reaction, user = await self.client.wait_for('reaction_add', timeout=60.0, check=check)
            await em3.delete()

            if str(reaction.emoji) == utils.save.rosa:
                color = 0xff006e
            elif str(reaction.emoji) == utils.save.vermelho:
                color = 0xff0022
            elif str(reaction.emoji) == utils.save.laranja:
                color = 0xff5d00
            elif str(reaction.emoji) == utils.save.amarelo:
                color = 0xfbe500
            elif str(reaction.emoji) == utils.save.verde:
                color = 0x47ff00
            elif str(reaction.emoji) == utils.save.azulclaro:
                color = 0x00ece5
            elif str(reaction.emoji) == utils.save.azulescuro:
                color = 0x0000ff
            elif str(reaction.emoji) == utils.save.roxo:
                color = 0xa200c4
            elif str(reaction.emoji) == utils.save.marrom:
                color = 0x924d23
            elif str(reaction.emoji) == utils.save.preto:
                color = 0x000000
            elif str(reaction.emoji) == utils.save.cinza:
                color = 0x202225
            elif str(reaction.emoji) == utils.save.branco:
                color = 0xffffff

            embed = discord.Embed(title=title.content, description=desc.content, colour=color)

            def check(reaction, user):
                return user == ctx.author and str(reaction.emoji) in utils.save.sim_e_nao
            embed4 = discord.Embed(title='⚙ Configuração de Embed', description='🔨 Deseja que sua embed tenha mídia?')
            embed4.set_footer(text='Concluído: 4/4')
            em4 = await ctx.send(embed=embed4)

            await em4.add_reaction(utils.save.s)
            await em4.add_reaction(utils.save.n)

            reaction, user = await self.client.wait_for('reaction_add', timeout=60.0, check=check)

            await em4.delete()

            if str(reaction.emoji) == utils.save.s:
                def check(message):
                    return message.author == ctx.author and message.channel == ctx.channel
                embed5 = discord.Embed(title='⚙ Configuração de Embed', description='🔨 Envie a mídia')
                embed5.add_field(name='Não disponível:', value='・Links\n・Vídeos')
                embed5.add_field(name='Disponível:', value='・Gifs\n・Imagens')
                em5 = await ctx.send(embed=embed5)
                await em5.add_reaction(utils.save.loading)

                midia = await self.client.wait_for('message', timeout=60.0, check=check)

                await em5.delete()
                await midia.delete()

                if midia.attachments:
                    embed.set_image(url=midia.attachments[0].url)
                    if ctx.author.guild_permissions.administrator:
                        await ctx.respond(embed=embed)
                    else:
                        embed.timestamp = datetime.datetime.utcnow()
                        embed.set_footer(icon_url=ctx.author.avatar.url, text=ctx.author.name)
                        await ctx.respond(f'Embed enviada por: {ctx.author.mention}', embed=embed)
                else:
                    midia_err = await ctx.respond(embed=discord.Embed(description=f'Não consegui utilizar o arquivo enviado, tente novamente com outra mídia'))
                    await midia_err.add_reaction(utils.save.n)
                    if ctx.author.guild_permissions.administrator:
                        await ctx.respond(embed=embed)
                    else:
                        embed.timestamp = datetime.datetime.utcnow()
                        embed.set_footer(icon_url=ctx.author.avatar.url, text=ctx.author.name)
                        await ctx.respond(f'Embed enviada por: {ctx.author.mention}', embed=embed)

            elif str(reaction.emoji) == utils.save.n:
                if ctx.author.guild_permissions.administrator:
                    await ctx.respond(embed=embed)
                else:
                    embed.timestamp = datetime.datetime.utcnow()
                    embed.set_footer(icon_url=ctx.author.avatar.url, text=ctx.author.name)
                    await ctx.respond(f'Embed enviada por: {ctx.author.mention}', embed=embed)
    
        except asyncio.TimeoutError:
            msg = await ctx.respond(embed=discord.Embed(description=f'Você demorou demais para responder então eu cancelei o comando. Da próxima vez tente responder em menos de `1 minuto`.'))
            await msg.add_reaction(utils.save.n)
                

    @slash_command(description='〘 🛠️  Utilidades 〙Ativa o chat global no seu servidor')
    async def chatglobal_start(self, ctx, 
                    channel: Option(discord.TextChannel, description='Chat que deseja ativar o chat global', required=True, default=True)):
        await ctx.defer()
        if channel == None:
            channel = ctx.channel
        guild_id = ctx.guild.id
        channel_id = channel.id
        with open('./databases/global_chat.json', 'r') as file:
            global_chat_data = json.load(file)
            new_global_chat = str(guild_id)
            if new_global_chat in global_chat_data:
                msg = await ctx.respond(embed=discord.Embed(description=f'O `Chat Global` já foi atribuído anteriormente ao servidor!'))
                await msg.add_reaction(utils.save.n)
            else:
                global_chat_data[new_global_chat] = channel_id
                with open('./databases/global_chat.json', 'w') as new_global_chat:
                    json.dump(global_chat_data, new_global_chat, indent=4)
                msg = await ctx.respond(embed=discord.Embed(description=f'O `Chat Global` foi atribuído ao chat {channel.mention} com sucesso!'))
                await msg.add_reaction(utils.save.s)
    
    @commands.Cog.listener()
    async def on_message(self, message):
        
        if message.author.bot:
            if message.author.id == 800764726538797066:
                if 'portanto não foi enviada no chat global' in message.content:
                    return
                elif message.embeds is not None:
                    return
                else:
                    pass
            else:
                return 
            
        with open('./databases/global_chat.json', 'r') as file:
            global_chat_data = json.load(file)
        channel_id = list(global_chat_data.values())
        
        urls = regex.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', message.content.lower())
        if message.channel.id in channel_id:
            for ids in channel_id:
                if message.channel.id != ids:
                    
                    if message.author.id == 842741926071762944:
                        pass
                    else:
                        
                        if urls and message.channel.id in channel_id:
                            msg =  await message.reply(embed=discord.Embed(description='A mensagem contém um link, portanto não foi enviada no chat global!'))
                            return await msg.add_reaction(utils.save.n)
                        if 'discord.gg/' in message.content:
                            msg =  await message.reply(embed=discord.Embed(description='A mensagem contém um convite de servidor, portanto não foi enviada no chat global!'))
                            return await msg.add_reaction(utils.save.n)
                        elif 'dc.gg/' in message.content:
                            msg =  await message.reply(embed=discord.Embed(description='A mensagem contém um convite de servidor, portanto não foi enviada no chat global!'))
                            return await msg.add_reaction(utils.save.n)
                        elif 'dsc.gg/' in message.content:
                            msg =  await message.reply(embed=discord.Embed(description='A mensagem contém um convite de servidor, portanto não foi enviada no chat global!'))
                            return await msg.add_reaction(utils.save.n)
                        elif '@everyone' in message.content:
                            msg =  await message.reply(embed=discord.Embed(description='A mensagem contém uma menção global, portanto não foi enviada no chat global!'))
                            return await msg.add_reaction(utils.save.n)
                        elif '@here' in message.content:
                            msg =  await message.reply(embed=discord.Embed(description='A mensagem contém uma menção global, portanto não foi enviada no chat global!'))
                            return await msg.add_reaction(utils.save.n)
                        
                    tchannel = self.client.get_channel(ids)
                    webhoks = await tchannel.webhooks()
                    webhook = discord.utils.get(webhoks, name='Chat_Global')
                    if webhook is None:
                        webhook = await tchannel.create_webhook(name='Chat_Global')
                        
                    if message.reference is not None: # se a mensagem for uma resposta
                        msg = await message.channel.fetch_message(message.reference.message_id)
                        author = msg.author.name
                        if message.attachments: # se a mensagem tiver imagem
                            for attachment in message.attachments:
                                await attachment.save(f'./utils/images/{attachment.filename}')
                            await webhook.send(content=f'{msg.content}\n━━━━━━━━━\n**@{author}** {message.content}', username=message.author.name, avatar_url=message.author.avatar.url, file=discord.File(f'./utils/images/{attachment.filename}'))
                            os.remove(f'./utils/images/{attachment.filename}')
                        else: # se a mensagem não tiver imagem
                            await webhook.send(content=f'{msg.content}\n━━━━━━━━━\n**@{author}** {message.content}', username=message.author.name, avatar_url=message.author.avatar.url)
                        
                    elif message.reference is None: # se a mensagem não for uma resposta
                        if message.attachments: # se a mensagem tiver imagem
                            for attachment in message.attachments:
                                await attachment.save(f'./utils/images/{attachment.filename}')
                            await webhook.send(content=f'{message.content}', username=message.author.name, avatar_url=message.author.avatar.url, file=discord.File(f'./utils/images/{attachment.filename}'))
                            os.remove(f'./utils/images/{attachment.filename}')
                        else: # se a mensagem não tiver imagem
                            await webhook.send(content=f'{message.content}', username=message.author.name, avatar_url=message.author.avatar.url)
   
                                    
                                    
def setup(client):
    client.add_cog(Utilidades(client))