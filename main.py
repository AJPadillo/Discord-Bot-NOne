import discord

client = discord.Client()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

