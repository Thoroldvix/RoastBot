import logging
import os
import sys

import discord
import openai

intents = discord.Intents.all()
client = discord.Client(intents=intents)
openai.api_key = os.getenv('OPENAI_KEY')
discord_token = os.getenv('DISCORD_TOKEN')


def get_roast_response_classy(user_id):
    with open("sirO.png", "rb") as avatar_file:
        new_avatar = avatar_file.read()
        await client.user.edit(avatar=new_avatar)
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt='Напиши креативное оскорбление в стиле шекспира на русском языке используй слова '
                   'из этого списка: (хуй, еблан, даун)'
            ,
            temperature=1,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.6
        )
        response_str = response['choices'][0]['text'].replace('"', '')
        return f'{response_str} <:sirO:755463220264960080> <@{user_id}>'
    except Exception as e:
        sys.exit(e)


def get_roast_response_weeb(user_id):
    with open("ayaya.png", "rb") as avatar_file:
        new_avatar = avatar_file.read()
        await client.user.edit(avatar=new_avatar)
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt='write insult in japanese using romanized writing style'
            ,
            temperature=1,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.6
        )
        response_str = response['choices'][0]['text'].replace('"', '')
        return f'{response_str} <:AYAYA:1099327621738799184>  <@{user_id}>'
    except Exception as e:
        sys.exit(e)


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('🍷'))
    logging.log(logging.INFO, f'Bot online')


@client.event
async def on_reaction_add(reaction, user):
    logging.log(logging.INFO, f'{user.name} reacted with {reaction.emoji} on message {reaction.message.content}')
    siro_emoji = '<:sirO:755463220264960080>'
    ayaya_emoji = '<:AYAYA:1099327621738799184>'

    if str(reaction.emoji) == siro_emoji:
        channel = reaction.message.channel
        await channel.send(get_roast_response_classy(reaction.message.author.id))

    elif str(reaction.emoji) == ayaya_emoji:
        channel = reaction.message.channel
        await channel.send(get_roast_response_weeb(reaction.message.author.id))


client.run(discord_token)
