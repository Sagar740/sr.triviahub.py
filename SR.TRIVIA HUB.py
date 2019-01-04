import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import asyncio
import platform
import colorsys
import random
import os
import time
from discord.voice_client import VoiceClient
from discord import Game, Embed, Color, Status, ChannelType


Forbidden= discord.Embed(title="Permission Denied", description="1) Please check whether you have permission to perform this action or not. \n2) Please check whether my role has permission to perform this action in this channel or not. \n3) Please check my role position.", color=0x00ff00)
client = Bot(description="SAHIL RANA Bot is best", command_prefix=".", pm_help = True)
client.remove_command('help')


async def status_task():
    while True:
        await client.change_presence(game=discord.Game(name='with .help & SR.TRIVIA HUB  '))
        await asyncio.sleep(5)
        await client.change_presence(game=discord.Game(name='with '+str(len(set(client.get_all_members())))+' users'))
        await asyncio.sleep(5)

@client.event
async def on_ready():
    print('Bot is ready.')
    
@client.command(pass_context=True)
async def clear(ctx,amount=100):
    channel = ctx.message.channel
    message = []
    async for message in client.logs_from(channel,limit=int(amount)):
        messages.oppend(message)
    await client.delete_messages(messages)

@client.command()
async def a():
    embed = discord.Embed(
        title = '**__SUGGESTED BEST ANSWER__**',
        description = '**__BEST ANSWER BY SR.TRIVIA HUB.',
        colour = discord.colour.blue() 
    )
    
    embed.set_footer(text'▀▄▀▄▀▄[ RI▀█▀esh]▄▀▄▀▄▀#2150.'')
    embed.set_image(url='https://cdn.discordapp.com/attachments/492929616755949579/529219043874308096/JPEG_20181229_111253.jpg')
    embed.set_author('SUGGESTED ANSWER')
    icon_url('https://cdn.discordapp.com/attachments/492929616755949579/529219043874308096/JPEG_20181229_111253.jpg')
    embed.set_field(name='Option 1'),value='100%',inline=False)
    embed.set_field(name='Option 2'),value='0%',inline=True)
    embed.set_filed(name='Option 3'),value='0%',inline=False)
    embed.set_field(name='Best Answer'),value=':one:',inline=True)


client.run(os.getenv('Token'))
