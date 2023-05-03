import logging
import os
import sys

import discord
import openai

intents = discord.Intents.all()
client = discord.Client(intents=intents)
openai.api_key = os.getenv('OPENAI_KEY')
discord_token = os.getenv('DISCORD_TOKEN')


def get_roast_response(user_id):
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt='Напиши креативное оскорбление и пошли подальше в стиле шекспира на русском языке используй '
                   'бранную речь',
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.6
        )
        response_str = response['choices'][0]['text'].replace('"', '')
        return f'{response_str} <:sirO:755463220264960080> <@{user_id}>'
    except Exception as e:
        sys.exit(e)


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


client.run(discord_token)
