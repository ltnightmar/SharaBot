import json
import discord
import datetime
import regex
from discord.ext import commands


class GlobalChat(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.group(aliases=['chatglobal', 'chat_global', 'global_chat'], invoke_without_command=True)
    async def globalchat(self, ctx):
        with open('./databases/prefixes.json', 'r') as f:
            prefixes = json.load(f)
        pre = prefixes[str(ctx.guild.id)]
        return await ctx.send(f'{ctx.author.mention}\n**Comandos disponíveis:**\n> `{pre}chatglobal iniciar <#chat>`\n> `{pre}chatglobal finalizar`')

    @globalchat.command(aliases=['começar', 'comecar', 'iniciar'])
    @commands.has_permissions(manage_guild=True)
    async def start(self, ctx, channel=None):
        if channel is None:
            with open('./databases/prefixes.json', 'r') as f:
                prefixes = json.load(f)
            pre = prefixes[str(ctx.guild.id)]
            return await ctx.send(f'{ctx.author.mention}\n**Comandos disponíveis:**\n> `{pre}chatglobal iniciar <#chat>`\n> `{pre}chatglobal finalizar`')
        guild_id = ctx.message.guild.id
        channel_id = int(channel.strip('<>#'))

        with open('./databases/global_chat.json', 'r') as file:
            global_chat_data = json.load(file)
            new_global_chat = str(guild_id)

            if new_global_chat in global_chat_data:
                await ctx.send(f'<:nao:850020125927276641> {ctx.author.mention}| O `Chat Global` já foi atribuído anteriormente ao servidor!')

            else:
                global_chat_data[new_global_chat] = channel_id
                with open('./databases/global_chat.json', 'w') as new_global_chat:
                    json.dump(global_chat_data, new_global_chat, indent=4)
                with open('./databases/prefixes.json', 'r') as f:
                    prefixes = json.load(f)
                pre = prefixes[str(ctx.guild.id)]

                await ctx.send(f'<:ssim:850020125641408582> {ctx.author.mention}| O `Chat Global` foi atribuído ao canal mencionado!\n<:warn:865040919896391700> **Se um dia decidir apagar esse chat/servidor, execute o comando {pre}chatglobal stop**')

    @globalchat.command(aliases=['finalizar', 'parar', 'terminar'])
    @commands.has_permissions(manage_guild=True)
    async def stop(self, ctx):
        guild_id = ctx.message.guild.id

        with open('./databases/global_chat.json', 'r') as file:
            global_chat_data = json.load(file)

        global_chat_data.pop(str(guild_id))

        with open('./databases/global_chat.json', 'w') as update_global_chat_file:
            json.dump(global_chat_data, update_global_chat_file, indent=4)

        await ctx.send(f'<:ssim:850020125641408582> {ctx.author.mention}| O `Chat Global` foi desatribuído ao servidor!')

    @commands.Cog.listener()
    async def on_message(self, message):
        if not message.author.bot:
            if not message.content.startswith('#'):
                with open('./databases/global_chat.json', 'r') as file:
                    global_chat_data = json.load(file)

                channel_id = list(global_chat_data.values())

                urls = regex.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',message.content.lower())
                if urls and message.channel.id in channel_id:
                    return
                if message.content.startswith('discord.gg/'):
                    return
                if message.content.startswith('dc.gg/'):
                    return
                if message.channel.id in channel_id:
                    if not message.content:
                        message.content = 'ㅤ'

                    for ids in channel_id:
                        if message.channel.id != ids:
                            message_embed = discord.Embed()

                            message_embed.timestamp = datetime.datetime.utcnow()
                            message_embed.set_author(icon_url=message.author.avatar_url, name=f'{message.author}')
                            message_embed.add_field(name='Disse:', value=f'{message.content}')
                            if message.attachments:
                                message_embed.set_image(url=message.attachments[0].url)
                            message_embed.set_footer(icon_url=message.guild.icon_url, text=message.guild.name)

                            await self.client.get_channel(ids).send(embed=message_embed)


def setup(client):
    client.add_cog(GlobalChat(client))