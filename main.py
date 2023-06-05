import logging
import os
import sys

import discord
import openai

intents = discord.Intents.all()
intents.message_content = True
client = discord.Client(intents=intents)
openai.api_key = os.getenv('OPENAI_KEY')
discord_token = os.getenv('DISCORD_TOKEN')
japanese_roast_reaction = os.getenv('JAPANESE_ROAST_REACTION')
classy_roast_reaction = os.getenv('CLASSY_ROAST_REACTION')


def get_roast_response(insult_prompt, user_id, guild, reaction_emoji):
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=insult_prompt,
            temperature=1,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.6
        )
        response_str = response['choices'][0]['text'].replace('"', '')
        for emoji in guild.emojis:
            if emoji.name == reaction_emoji:
                return f'{response_str} <:{emoji.name}:{emoji.id}> <@{user_id}>'
        return
    except Exception as e:
        sys.exit(e)


def get_roast_response_classy(user_id, guild):
    with open('prompts/classy_roast_prompt', 'r', encoding="utf-8") as file:
        insult_string = file.read()
    return get_roast_response(insult_string, user_id, guild, classy_roast_reaction)


def get_roast_response_weeb(user_id, guild):
    with open('prompts/weeb_roast_prompt', 'r') as file:
        insult_string = file.read()
    return get_roast_response(insult_string, user_id, guild, japanese_roast_reaction)


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('🍷'))
    logging.log(logging.INFO, f'Bot online')


@client.event
async def on_raw_reaction_add(payload):
    user = client.get_user(payload.user_id)
    channel = client.get_channel(payload.channel_id)
    message = await channel.fetch_message(payload.message_id)
    guild = client.get_guild(payload.guild_id)
    logging.log(logging.INFO, f'{user.name} reacted with {payload.emoji.name} on message {message}')

    if str(payload.emoji.name) == classy_roast_reaction:
        await channel.send(get_roast_response_classy(message.author.id, guild))

    elif str(payload.emoji.name) == japanese_roast_reaction:
        await channel.send(get_roast_response_weeb(message.author.id, guild))
    else:
        return


client.run(discord_token)
