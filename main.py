import logging
import os

import discord

from responses import get_roast_response

intents = discord.Intents.all()
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('🍷'))
    logging.log(logging.INFO, f'Bot online')


@client.event
async def on_reaction_add(reaction, user):
    logging.log(logging.INFO, f'{user.name} reacted with {reaction.emoji} on message {reaction.message.content}')
    emoji = '<:sirO:755463220264960080>'
    if str(reaction.emoji) == emoji:
        channel = reaction.message.channel
        await channel.send(get_roast_response(reaction.message.author.id))


client.run(os.getenv('DISCORD_TOKEN'))
