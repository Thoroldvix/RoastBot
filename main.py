import json
import discord

from responses import get_roast_response

file = open('config.json', 'r')
config = json.load(file)

intents = discord.Intents.all()
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('🍷'))
    print('Bot online')


@client.event
async def on_reaction_add(reaction, user):
    print(f'{user.name} reacted with {reaction.emoji} on message {reaction.message.content}')
    emoji = '<:sirO:755463220264960080>'
    if str(reaction.emoji) == emoji:
        channel = reaction.message.channel
        await channel.send(get_roast_response(reaction.message.author.id))


client.run(config['token_discord'])
